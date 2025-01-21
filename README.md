# Comfyui_Layer_blending_LeonGo
At present, I have not used the useful comfyui custom node about layer mixing, and I have written a comfyui runtime automatic pop-up window for layer editing node
# ComfyUI Web Canvas Node


想了很久，这个项目就叫，layersDiccc，哦算了，imgcanvas吧。
一个用于 ComfyUI 的交互式图像编辑节点扩展，提供了直观的 Web 画布界面，支持图像的实时编辑、混合和蒙版操作。
非pyqt项目，鉴于macos上运行pyqt项目总是莫名其妙出现一堆问题，我使用js和python后台进行了前后端项目的重构。
![image](https://github.com/user-attachments/assets/d29309f4-815c-4ac7-9faa-9b11bac019c9)

## 功能特点

- 🖼️ 交互式图像编辑界面
- 🔄 实时图像变换
  - 缩放
  - 旋转
  - 位移
- 🎭 自动蒙版生成
- 👆 直观的拖拽控制
- ⌨️ 快捷键支持
- 🎨 透明度调节
- 📏 精确的变换控制

## 安装方法

1. 进入 ComfyUI 的 `custom_nodes` 目录
2. 克隆本仓库：
```bash
git clone [repository_url] 
```
3. 重启 ComfyUI

## 使用方法

### 基本使用流程

1. 在节点图中添加 "Web Canvas" 节点
2. 连接输入：
   - `back_image`: 背景图像
   - `fore_image`: 前景图像
   - `fore_mask`(可选): 前景蒙版
   - `seed`: 随机种子值

### 界面控制

- **变换控制**：
  - 拖拽图像中心进行位移
  - 拖拽角点进行缩放
  - 拖拽顶部旋转手柄进行旋转
  - 按住 Shift 键可进行精确控制（15度旋转吸附/等比例缩放）

- **工具按钮**：
  - 重置变换
  - 设置缩放比例
  - 调节透明度
  - 确认/取消编辑

- **快捷键**：
  - `R`: 重置变换
  - `←`/`→`: 旋转调整
  - `+`/`-`: 缩放调整
  - `Enter`: 确认编辑
  - `Esc`: 取消编辑

## 技术细节

### 节点输入输出

- **输入**：
  - `back_image`: IMAGE 类型，背景图像
  - `fore_image`: IMAGE 类型，前景图像
  - `fore_mask`: MASK 类型（可选），前景蒙版
  - `seed`: INT 类型，随机种子值

- **输出**：
  - `image`: IMAGE 类型，编辑后的图像
  - `mask`: MASK 类型，生成的蒙版

### 主要组件

- `WebCanvasNode`: 核心节点类，处理图像处理和数据流
- `TransformBox`: 前端变换控制组件，处理用户交互
- `dialog.js`: Web 界面实现，包含所有交互逻辑

## 注意事项

1. 图像编辑会在浏览器中进行，确保有足够的内存
2. 编辑超时时间为 60 秒，请在此时间内完成编辑
3. 所有变换操作都是可逆的，可以随时重置或取消

## 贡献指南
感谢前辈的一些源代码贡献，实在忘记了哪个项目。

欢迎提交 Issue 和 Pull Request 来改进这个项目。在提交代码前，请确保：

1. 代码风格保持一致
2. 添加必要的注释和文档
3. 测试所有功能正常工作

## 许可证

[许可证类型]

## 更新日志

## 欢迎请我喝豆浆，谢谢

### v1.0.0
- 初始版本发布
- 实现基本的图像编辑功能
- 添加交互式 Web 界面
![image](https://github.com/user-attachments/assets/3e0d40ba-65ff-4fae-9c3d-c27099a23107)
![image](https://github.com/user-attachments/assets/7a155747-be10-4017-8da9-4e13af923dc5)
![image](https://github.com/user-attachments/assets/46724ae2-9866-4326-a25e-9a44e78282c0)



# 当然我还做了一个专业的大杯版本，支持10张图的自由混合，图层顺序挑换，等等等功能。
![image](https://github.com/user-attachments/assets/db851ad3-cea2-4b53-aadc-d1b61501647b)
![image](https://github.com/user-attachments/assets/70769a18-9f1b-4ccd-9e36-12f3c96b77b0)
![image](https://github.com/user-attachments/assets/32f4f6a8-06bd-4c6a-85f8-0e72f17db764)

