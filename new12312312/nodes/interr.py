import threading
import queue
import time
import ctypes
import functools
import comfy.model_management as model_management

def interruptible(timeout=60.0):
    """
    作者：Leon
    装饰器：使函数可中断
    超时或中断时会抛出异常
    超时时间：60秒
    功能：中断时返回None
    目前状态：静默中断
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            result_queue = queue.Queue()
            
            def worker():
                try:
                    result = func(self, *args, **kwargs)
                    result_queue.put(("success", result))
                except Exception as e:
                    result_queue.put(("error", e))
            
            thread = threading.Thread(target=worker)
            thread.daemon = True
            thread.start()
            
            def terminate_thread():
                if not thread.is_alive():
                    return
                exc = ctypes.py_object(SystemExit)
                res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
                    ctypes.c_long(thread.ident), exc)
                if res > 1:
                    ctypes.pythonapi.PyThreadState_SetAsyncExc(
                        ctypes.c_long(thread.ident), None)
            
            try:
                start_time = time.time()
                while thread.is_alive():
                    try:
                        status, result = result_queue.get(timeout=0.1)
                        if status == "success":
                            return result
                        else:
                            raise result
                    except queue.Empty:
                        # 检查超时
                        if time.time() - start_time > timeout:
                            terminate_thread()

                            return None
                        
                        # 静默中断
                        model_management.throw_exception_if_processing_interrupted()

            finally:
                terminate_thread()
            
        return wrapper
    return decorator