---
name: image_to_ppt
description: 图片转PPT服务，将图片异步转换为 PPT 文件。
version: 1.0.0
author: SCNet
license: MIT
tags:
  - OCR
  - 文档转换
  - 图片转PPT

required_env_vars:
  - SCNET_API_KEY
optional_env_vars:
  - SCNET_API_BASE
  - SCNET_POLL_INTERVAL
  - SCNET_MAX_POLL_TIME
primary_credential: SCNET_API_KEY
dependencies:
  - python3
  - requests
input:
  - ocrType : 转换类型，IMAGE_TO_PPT
  - filePath : 待转换文件的本地路径
output: 转换后的 PPT（.pptx）文件下载地址
---
# Sugon-Scnet 图片转PPT服务技能

本技能封装了 Scnet OCR 服务，将图片异步转换为 PPT 文件，并通过轮询获取转换结果。

---

## 功能特性

- **图片转 PPT**：将图片内容转换为 `.pptx`。
- **异步任务 + 自动轮询**：提交任务后自动轮询状态，直到任务完成或超时。

## 前置配置

> **⚠️ 重要**：使用前需要申请 Scnet API Token

### 申请 API Token

1. 访问 [Scnet 官网](https://www.scnet.cn) 注册/登录
2. 在控制台申请 API 密钥（格式：`sc-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`）
3. 复制密钥备用

### 配置 Token

**手动配置（推荐）**
1. 在技能目录下创建 `config/.env` 文件，内容如下：
```ini
# =====  Sugon-Scnet 文档格式转化 API 配置 =====
# 申请地址：https://www.scnet.cn
SCNET_API_KEY=your_scnet_api_key_here

# API 基础地址（一般无需修改）
SCNET_API_BASE=https://api.scnet.cn/api/llm/v1

# 轮询配置（可选）
SCNET_POLL_INTERVAL=5
SCNET_MAX_POLL_TIME=600
```
2. 添加：`SCNET_API_KEY=你的密钥`
3. 设置文件权限为 600（仅所有者可读写）

**⚠️ 安全警告**：切勿将 API Key 直接粘贴到聊天对话中，否则可能被记录或泄露。

### Token 更新

Token 过期后调用会返回 401 或 403 错误。更新方法：重新申请 Token 并替换 config/.env 中的 SCNET_API_KEY。

### 依赖安装

本技能需要 Python 3.6+ 和 requests 库。请运行以下命令：

```bash
   pip install requests
```

---

## 使用方法

### 参数说明

| 参数名 | 类型 | 必填 | 描述 |
|--------|------|------|------|
| ocrType | string | 是 | 转换类型。必须为 IMAGE_TO_PPT（图片转 PPT） |
| filePath | string | 是 | 待转换文件的本地绝对路径。图片格式。 |

### 命令行调用示例

```bash
   python .claude/skills/image_to_ppt/scripts/main.py IMAGE_TO_PPT /path/to/image.png
```

### 在 AI 对话中使用

用户可以说：

- “把这张图片转换成 PPT，图片路径 /Users/name/Downloads/slide.png”

AI 会根据 description 中的关键词自动触发本技能。

### AI 调用建议

- 为避免触发 API 速率限制，请串行调用本技能，等待前一个任务完成后再发起下一个请求。
- 如果使用 OpenClaw 的 exec 工具，建议设置足够的 timeout，因为转换任务需要异步轮询。

### 配置选项

编辑 `config/.env` 文件：

| 变量名 | 默认值 | 说明 |
|--------|--------|------|
| SCNET_API_KEY | 必需 | Scnet API 密钥 |
| SCNET_API_BASE | https://api.scnet.cn/api/llm/v1 | API 基础地址（一般无需修改） |
| SCNET_POLL_INTERVAL | 5 | 轮询状态间隔（秒） |
| SCNET_MAX_POLL_TIME | 600 | 最大轮询等待时间（秒） |

### 输出

- 标准输出：转换成功时返回结果文件下载地址 JSON。
- 结果位于 `data[0].output.results` 中，为临时 MinIO 下载链接。
- 错误信息：如果发生错误，会输出以 `错误:` 开头的友好提示。

### 注意事项

- 输入文件必须与 `ocrType` 匹配：IMAGE_TO_PPT 输入图片。
- 下载地址为临时授权链接，请及时下载使用。
- 转换任务为异步处理，脚本会自动轮询直到完成或超时。

### 故障排除

| 问题 | 解决方案 |
|------|----------|
| 配置文件不存在 | 创建 config/.env 并填入 Token（参考前置配置） |
| API Key 无效/过期 | 重新申请 Token 并更新 `.env` 文件 |
| 文件不存在 | 检查提供的文件路径是否正确 |
| 网络连接失败 | 检查网络连接或防火墙设置 |
| 不支持的文件类型 | 确保文件扩展名为允许的类型（参考 API 文档） |
| 401/403/Unauthorized | Token 无效或过期，重新申请并配置 |
| 任务长时间 running | 可能是文件较大或服务繁忙，可增大 SCNET_MAX_POLL_TIME |
| 任务失败 | 查看返回的 error_code 和 error_message |
