---
name: zai-image-understanding
description: 图片理解技能，使用 Z.ai (智谱 AI) GLM-4V Vision API 进行图片分析。
metadata:
  short-description: Z.ai 图片理解
---

# zai-image-understanding Skill

Linux 环境下的图片理解技能，专门使用 **Z.ai (智谱 AI) GLM-4V Vision API** 进行图片分析。

## 功能

- ✅ **Z.ai GLM-4V Vision API 支持**：使用智谱 AI 的 GLM-4.1V-thinking-flash 模型
- ✅ **多种输入方式**：本地文件路径、HTTP/HTTPS URL、Base64 Data URI
- ✅ **自动图片预处理**：尺寸调整、格式转换以适应模型限制
- ✅ **可配置提示词和模型**：通过 JSON 配置文件自定义行为
- ✅ **Markdown 输出保存**：自动保存分析结果为可读的 Markdown 文件
- ✅ **批处理能力**：可通过 Python API 进行大规模图片处理
- ✅ **标准库仅依赖**：核心逻辑仅依赖 Python 标准库，仅 requests 和 Pillow 为外部依赖

## 安装

```bash
# 克隆或复制技能到技能目录
mkdir -p ~/.openclaw/workspace/skills/zai-image-understanding
cp -r /path/to/skill/* ~/.openclaw/workspace/skills/zai-image-understanding/

# 安装依赖
pip install -r ~/.openclaw/workspace/skills/zai-image-understanding/requirements.txt
```

## 配置

### 1. 获取 Z.ai API Key

前往 [智谱 AI 开放平台](https://open.bigmodel.cn/) 获取 API Key。

### 2. 设置环境变量（推荐）

在您的 shell 配置文件中添加（如 `~/.bashrc`、`~/.zshrc` 或 `~/.profile`）：

```bash
# 智谱 AI API Key
export ZAI_API_KEY="your-zai-api-key-here"
```

然后重新加载配置：

```bash
source ~/.bashrc  # 或 source ~/.zshrc
```

### 3. 临时设置（仅当前终端有效）

```bash
export ZAI_API_KEY="your-zai-api-key-here"
```

### 4. 配置文件（可选）

首次运行时会自动创建默认配置文件：
`~/.config/zai-image-understanding/config.json`

```json
{
  "mode": "cloud",
  "cloud": {
    "provider": "zai",
    "model": "glm-4.1v-thinking-flash",
    "api_key_env": "ZAI_API_KEY",
    "base_url": "https://open.bigmodel.cn/api/paas/v4",
    "timeout_seconds": 60
  },
  "default_prompt": "请详细描述这张图片的内容，包括主要物体、场景、文字、颜色、构图等信息。"
}
```

## 使用方法

### 命令行界面

```bash
# 基本使用
python -m zai_image_understanding.analyze -i /path/to/image.jpg

# 指定提示词
python -m zai_image_understanding.analyze -i image.jpg -p "提取图片中的所有文字内容"

# 指定配置文件
python -m zai_image_understanding.analyze -i image.jpg -c /path/to/custom/config.json

# 保存结果为 Markdown
python -m zai_image_understanding.analyze -i image.jpg --save-markdown

# 创建默认配置
python -m zai_image_understanding.analyze --init-config

# 查看当前配置
python -m zai_image_understanding.analyze --show-config
```

### Python API

```python
from zai_image_understanding import analyze_image, load_config

# 简单调用
result = analyze_image("/path/to/image.jpg")

if result["status"] == "success":
    print(result["result"])
    print(f"使用模型: {result['model']}")
    print(f"Token 使用: {result['tokens']}")
else:
    print(f"错误: {result['error']}")

# 高级用法
config = load_config("/custom/path/config.json")
result = analyze_image(
    image_path="https://example.com/image.png",
    prompt="描述这张图片的主要情感和氛围",
    config_path="/custom/path/config.json"
)
```

## 输出格式

命令行默认输出 JSON：
```json
{
  "status": "success",
  "result": "图片中显示的是一只橘色的猫坐在阳光明媚的窗台上，背景是模糊的绿色植物...",
  "model": "glm-4.1v-thinking-flash",
  "tokens": {
    "prompt": 150,
    "completion": 85,
    "total": 235
  }
}
```

当使用 `--save-markdown` 时，会在 `~/.local/share/zai-image-understanding/outputs/` 目录下生成类似：
```
vlm_abc123_1721400000.md
```

## 依赖

- Python 3.8+
- requests>=2.31.0
- Pillow>=10.0.0
- python-dotenv>=1.0.0 (可选，用于加载 .env 文件)

## 故障排除

| 问题 | 解决方案 |
|------|----------|
| API key not set | 设置环境变量 `ZAI_API_KEY` |
| Connection timeout | 增加配置中的 `timeout_seconds` 值 |
| Image too large | 系统会自动调整大小，也可手动预处理图片 |
| Model not found | 确认模型名称正确，默认为 `glm-4.1v-thinking-flash` |

## 许可证

MIT License