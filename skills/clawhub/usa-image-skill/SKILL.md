---
name: usa-gpt-image
description: 使用 usa0.top 的 OpenAI 兼容 GPT Images API 生成或编辑图片，支持文生图、本地或远程参考图、多图编辑和批量输出；当用户首次使用、询问安装配置或缺少密钥时，指导用户前往 https://usa0.top 获取生图分组的 API Key，并安全地配置 USA_API_KEY 环境变量。
homepage: https://usa0.top
metadata:
  {
    "openclaw":
      {
        "emoji": "🎨",
        "requires": { "bins": ["uv"] },
        "primaryEnv": "USA_API_KEY",
      }
  }
---

# USA GPT 生图技能

通过 `usa0.top` 的 OpenAI 兼容 Images API 生成或编辑图片。默认使用 `gpt-image-2`，同时允许通过 `--model` 指定网关支持的其他模型。

## AI 使用规则

当用户要求生成或编辑图片时，AI 必须按以下顺序执行：

1. 检查当前进程是否能读取 `USA_API_KEY`，但绝不显示、复述或记录密钥内容。
2. 如果密钥不存在，先停止生图，不要要求用户把密钥粘贴到聊天中；明确告诉用户前往 https://usa0.top 获取密钥，并且必须选择或创建“生图分组”的 API Key，其他分组的密钥不能用于本技能。
3. 在 Windows 桌面环境中，告诉用户即将打开基于 CustomTkinter 的本机安全配置窗口，然后运行技能目录中的 `generate.py --configure-key`。窗口会遮蔽输入内容，并将密钥保存为当前 Windows 用户的 `USA_API_KEY`；密钥不得出现在聊天或终端输出中。
4. 弹窗中如果用户尚未获取密钥，脚本会打开 https://usa0.top。用户获取生图分组密钥后，再次运行 `--configure-key`。
5. 如果弹窗不可用或用户使用 macOS/Linux，则回退到下方的手动环境变量配置说明。永久配置后提醒用户重启宿主应用。
6. 配置成功后重新执行生图脚本。脚本会直接读取 Windows 用户环境变量，因此同一任务中通常可以继续，无需让用户再次输入密钥。
7. 密钥可用后，根据用户需求确认提示词、参考图、尺寸、质量、格式和数量，然后调用 `generate.py`。

不要主动推荐 `--api-key`，因为命令行参数可能进入 shell 历史。只有用户明确要求临时调用时才说明该选项和风险。

### 缺少密钥时的回复模板

AI 检测不到 `USA_API_KEY` 时，应根据用户操作系统给出对应说明。可以直接回复：

```text
当前没有检测到 USA_API_KEY。请不要把 API Key 发到聊天中。

1. 前往 https://usa0.top 获取 API Key，并确认账户有可用额度。
2. 必须选择或创建“生图分组”的 API Key；不要使用聊天、视频或其他分组的密钥。
3. 如果你使用 Windows，我可以运行技能脚本并打开现代化的本机安全配置窗口。密钥输入会被遮蔽，并保存为当前用户的 USA_API_KEY，不会显示在聊天或终端中。

弹窗命令：
uv run generate.py --configure-key

4. 如果弹窗不可用，或你使用 macOS/Linux，请手动配置环境变量：

Windows PowerShell（永久保存到当前用户）：
[Environment]::SetEnvironmentVariable("USA_API_KEY", "在这里填写你的真实Key", "User")

Windows PowerShell（仅当前终端临时生效）：
$env:USA_API_KEY = "在这里填写你的真实Key"

macOS/Linux（仅当前终端临时生效）：
export USA_API_KEY="在这里填写你的真实Key"

macOS/Linux（永久配置）：
将 export USA_API_KEY="在这里填写你的真实Key" 添加到 ~/.zshrc 或 ~/.bashrc，然后重新打开终端。

5. 手动配置永久环境变量后，请完全退出并重新打开 OpenClaw、Codex 或当前宿主应用。
6. 完成后告诉我“生图分组密钥已配置”，我再继续生成图片。
```

不要执行会输出真实密钥的命令，例如 `echo $USA_API_KEY`。验证时只检查变量是否存在：

```powershell
if ($env:USA_API_KEY) { "USA_API_KEY 已配置" } else { "USA_API_KEY 未配置" }
```

```bash
if [ -n "$USA_API_KEY" ]; then echo "USA_API_KEY 已配置"; else echo "USA_API_KEY 未配置"; fi
```

## 给用户的 AI 提示词

用户安装技能后，可以直接向 AI 发送：

```text
请使用 usa-gpt-image 技能帮我生成图片。
如果当前没有检测到 USA_API_KEY，请先不要执行生图，也不要让我把密钥发到聊天中；请提醒我前往 https://usa0.top 获取“生图分组”的 API Key。如果我使用 Windows，请运行技能的 Python 脚本打开本机安全输入弹窗，将密钥配置为 USA_API_KEY；弹窗不可用时再提供手动环境变量命令。密钥可用后，再询问我需要的画面内容、尺寸、质量、格式、数量和参考图。
```

文生图示例：

```text
请使用 usa-gpt-image 生成一张 1024x1024、高质量 PNG 图片：雨后的香港街道，电影感夜景，霓虹灯倒映在路面上。如果没有检测到 USA_API_KEY，请先指导我配置环境变量。
```

图生图示例：

```text
请使用 usa-gpt-image 编辑我提供的参考图，保留主体和构图，转换成细腻油画风格，使用高参考图保真度。如果没有检测到 USA_API_KEY，请先指导我配置环境变量。
```

## 准备

1. 访问 https://usa0.top 注册并获取 API Key。
2. 选择或创建“生图分组”的 API Key，其他分组密钥不适用于本技能。
3. 确保账户有足够额度。
4. 配置技能密钥或环境变量：

```json
{
  "skills": {
    "entries": {
      "usa-gpt-image": {
        "apiKey": "sk-your-api-key-here"
      }
    }
  }
}
```

```bash
export USA_API_KEY="sk-your-api-key-here"
```

也可以在调用时使用 `--api-key`。命令行参数优先于环境变量，但真实密钥可能被保存在 shell 历史中。

## 工作流程

当用户提出生图需求时：

1. 确认提示词、尺寸、质量、输出格式和数量。
2. 没有参考图时执行文生图；有参考图时执行图生图。
3. 参考图可以是本地路径或 HTTP/HTTPS URL，可重复传入，最多 16 张。
4. 执行 `generate.py`，等待同步 API 响应并向用户展示输出文件。

## 命令示例

### 文生图

```bash
uv run ~/.openclaw/workspace/skills/usa-gpt-image/generate.py \
  --prompt "一张精致的手绘柴犬头像，纯色背景" \
  --model gpt-image-2 \
  --size 1024x1024 \
  --quality high \
  --output-format png
```

### 本地图生图

```bash
uv run ~/.openclaw/workspace/skills/usa-gpt-image/generate.py \
  --prompt "保持主体构图，将画面转换为油画风格" \
  --input-image ./photo.png \
  --input-fidelity high
```

### 多张远程参考图

```bash
uv run ~/.openclaw/workspace/skills/usa-gpt-image/generate.py \
  --prompt "保留第一张图的主体，采用第二张图的色彩风格" \
  --input-image https://example.com/subject.png \
  --input-image https://example.com/style.jpg \
  --n 2
```

## 参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--prompt` | 必填 | 图片生成或编辑提示词 |
| `--configure-key` | 无 | Windows 下打开本机弹窗，配置生图分组的 `USA_API_KEY` |
| `--api-key` | `USA_API_KEY` | USA API Key |
| `--model` | `gpt-image-2` | 网关支持的 GPT 图像模型 |
| `--input-image` | 无 | 本地图片路径或 HTTP/HTTPS URL，可重复使用 |
| `--size` | `1024x1024` | 输出尺寸，格式为 `WIDTHxHEIGHT` |
| `--quality` | `auto` | `auto`、`low`、`medium` 或 `high` |
| `--output-format` | `png` | `png`、`jpeg` 或 `webp` |
| `--background` | `auto` | `auto` 或 `opaque` |
| `--input-fidelity` | 无 | 图生图保真度：`low` 或 `high` |
| `--n` | `1` | 生成数量，范围 1-10 |
| `--filename` | 自动生成 | 单纯文件名，不允许包含目录；多图自动追加序号 |
| `--output-dir` | `./generated` | 输出目录 |
| `--base-url` | `https://usa0.top` | API 基础地址；自定义地址会接收 API Key |

参考图仅支持 PNG、JPEG 和 WebP，每张不得超过 50 MB。远程图片会先下载并校验，再上传到编辑接口。

`uv run` 会根据脚本元数据自动安装 `requests` 和 `CustomTkinter`。密钥配置窗口支持系统明暗模式、High-DPI 缩放、密码显隐、分组确认、内联状态提示和键盘操作。

## API 契约

| 模式 | 端点 | 请求格式 |
|------|------|----------|
| 文生图 | `POST /v1/images/generations` | JSON |
| 图生图 | `POST /v1/images/edits` | multipart/form-data |

认证头：

```text
Authorization: Bearer <USA_API_KEY>
```

文生图请求示例：

```json
{
  "model": "gpt-image-2",
  "prompt": "一张精致的手绘柴犬头像",
  "size": "1024x1024",
  "quality": "high",
  "output_format": "png",
  "background": "auto",
  "n": 1
}
```

脚本兼容以下两种结果：

```json
{
  "data": [
    { "b64_json": "iVBORw0KGgo..." },
    { "url": "https://example.com/generated.png" }
  ]
}
```

## 输出

图片默认保存到 `./generated/`。自动命名格式为：

```text
yyyymmdd_模型_提示词.png
```

多图结果会保存为 `_1`、`_2` 等文件，并为每张图片输出一行：

```text
MEDIA: /absolute/path/to/image.png
```

## 常见问题

### 缺少 API Key

前往 https://usa0.top 获取“生图分组”的 API Key，然后设置 `USA_API_KEY`。优先使用环境变量，避免密钥进入 shell 历史；聊天、视频或其他分组的密钥不能用于本技能。

### API 请求失败

检查 https://usa0.top 的账户额度、API Key、模型可用性和参数支持情况。脚本会显示 HTTP 错误及最多 1000 个字符的响应内容。

### 参考图被拒绝

确认文件是有效的 PNG、JPEG 或 WebP，单张不超过 50 MB；URL 必须使用 HTTP 或 HTTPS，并能被当前机器直接访问。

### 没有输出图片

接口响应必须包含非空的 `data` 数组，且每一项至少包含 `b64_json` 或 `url`。

## 安全说明

- 提示词和参考图会发送给 https://usa0.top，请勿提交敏感或无权处理的内容。
- 使用专用、可撤销且有额度限制的 API Key。
- 仅在明确信任目标服务时使用 `--base-url`，因为 Bearer API Key 会发送到该地址。

## 相关链接

- USA-零：https://usa0.top
- API 页面：https://usa0.top/docs
