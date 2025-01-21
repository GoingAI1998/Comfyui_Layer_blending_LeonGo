"""Web canvas extension for ComfyUI"""
from .nodes.web_canvas import WebCanvasNode
from aiohttp import web
import json
from server import PromptServer

NODE_CLASS_MAPPINGS = {
    "WebCanvas": WebCanvasNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "WebCanvas": "Web Canvas"
}

WEB_DIRECTORY = "./web"

active_canvas = None

@PromptServer.instance.routes.post("/canvas/save")
async def save_canvas(request):
    """Save canvas data endpoint"""
    global active_canvas
    try:
        if active_canvas is None:
            return web.Response(status=400, text="No active canvas instance")
            
        data = await request.json()
        
        active_canvas.edited_data = data
        print("Edited data saved")
        
        active_canvas.save_event.set()
        print("Save event set")
        
        return web.json_response({"status": "success"})
    except Exception as e:
        return web.Response(status=500, text=str(e))
print("\n\033[93m 【Success】Leon image canvas extension initialized\033[0m\n")

def setup():
    try:
        print(" Leon image canvas extension initialized")
    except Exception as e:
        print(f"Error setting up web canvas extension")

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY", "setup"]