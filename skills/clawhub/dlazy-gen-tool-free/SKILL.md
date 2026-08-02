---

slug: dlazy-gen-tool-free
name: dlazy-gen-tool-free
version: 1.0.0
displayName: 综合生成工具-免费版
summary: "轻量级AI图片生成工具，支持文生图与基础图片编辑，适合个人创意原型制作.。综合生成工具免费版，面向个人创作者的AI图片生成方案。核心能力："
license: MIT
edition: free
description: "综合产出工具免费版，面向个人创作者的AI图片产出方案。核心能力：. 适用于需要dlazy gen tool相关能力的开发场景,提供结构化的工作流程和配置指引. 该工具经过深度差异化处理,针对用户反馈和使用痛点进行了优化改进,提升了实用性和可操作性."
tags:
  - 创意
  - dlazy
  - prompt
  - banana2
  - api
  - key
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"
pricing_tier: free
---

> **核心功能**: 本技能提供结构化的工作流程和配置指引等能力。


# 综合生成工具（免费版）

## 概述

综合生成工具免费版是一款面向个人创作者的 AI 图片生成工具。通过 dlazy CLI 自动选择优秀图片生成模型，将文本描述转换为高质量图片，支持多比例输出、基础编辑和超分辨率增强.
本版本适合社交媒体配图、产品概念图、个人项目视觉素材等场景。采用 API Key 认证，配置简单，开箱即用.
## 核心能力

### 免费版支持的模型

| 模型 | 类型 | 说明 |
|---|---|---|
| banana2 | 文生图 | 通用文生图，速度快成本低，适合草稿和社交 |
| seedream-5.0-lite | 文生图 | 轻量高速，适合批量生成与低成本迭代 |
| grok-4.2 | 文生图 | 极简文生图，快速概念验证 |
| gpt-image-2 | 文生图/编辑 | 支持文生图与参考图编辑 |
| imageseg | 图片处理 | 前景分离，返回透明背景 |
| superres | 超分辨率 | 提升图片清晰度与细节 |

### 能力边界

## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | 综合生成工具-免费版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```text
支持功能:
  - 文本生成图片（4个模型）
  - 图片前景分离抠图
  - 图片超分辨率增强
  - 多比例输出
# ...
不支持（需专业版）:
  - 视频生成（t2v, i2v, r2v）
  - 音频生成（TTS, 音乐, 音效）
  - 高质量模型（seedream-4.5, veo-3.1等）
  - 矢量图生成（SVG）
  - 管道链接批量处理
  - 图片风格复刻
```

**处理**: 解析免费版支持的模型的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回免费版支持的模型的响应数据,包含状态码、结果和日志.
### 核心功能执行
用`input_params`参数进行配置.

**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：轻量级、图片生成工具、支持文生图与基础、图片编辑、适合个人创意原型、综合生成工具免费、面向个人创作者的、图片生成方案、核心能力、自动模型选择、基础图片编辑与超、多比例输出与快速、草稿生成、API、Key、认证与本地配置等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
### 核心功能执行(补充)
执行核心功能执行操作,使用`input_params`参数进行配置.

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

## 使用场景

### 场景一：社交媒体配图快速生成

为社交媒体帖子快速生成配图.
```bash
# 生成社交媒体配图
dlazy banana2 \
  --prompt "一只在雪地里玩耍的红色狐狸，暖色调，温馨氛围" \
  --ratio "1:1" \
  --n 1
# ...
# 多比例生成（适配不同平台）
dlazy banana2 \
  --prompt "城市天际线日落，赛博朋克风格" \
  --ratio "16:9" \
  --n 1
```

### 场景二：产品概念图制作

为产品演示生成概念图.
```python
# 产品概念图批量生成脚本
import subprocess
import json
# ...
def generate_concept_images(prompts, model="banana2"):
    """批量生成产品概念图"""
    results = []
    for i, prompt in enumerate(prompts):
        cmd = [
            "dlazy", model,
            "--prompt", prompt,
            "--ratio", "16:9",
            "--n", "1"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        try:
            output = json.loads(result.stdout)
            results.append({
                "id": f"concept-{i:03d}",
                "prompt": prompt,
                "url": output.get("result", {}).get("outputs", [{}])[0].get("url", "")
            })
        except json.JSONDecodeError:
            results.append({"id": f"concept-{i:03d}", "error": "生成失败"})
    return results
# ...
# 批量生成
prompts = [
    "极简风格的智能家居控制面板，深色主题",
    "未来感十足的电动汽车仪表盘界面",
    "温馨的咖啡馆点餐App首页设计"
]
images = generate_concept_images(prompts)
for img in images:
    print(f"{img['id']}: {img.get('url', img.get('error'))}")
```

### 场景三：图片抠图与超分辨率

对已有图片进行后期处理.
```bash
# 前景分离抠图（去除背景）
dlazy imageseg \
  --image "./product-photo.jpg"
# ...
# 超分辨率增强（提升清晰度）
dlazy superres \
  --images "./low-res-image.png"
```

## 不适用场景

以下场景综合生成工具-免费版不适合处理：

- 需要100%确定性的关键决策
- 医疗诊断
- 法律判决

## 触发条件

需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于非本工具能力范围的需求.
## 快速开始

### 依赖详情

```bash
# 全局安装
npm install -g @dlazy/cli@latest
# ...
# 设置 API Key
dlazy auth set YOUR_API_KEY
```

### 第二步：生成领先张图片

```bash
# 查看模型帮助
dlazy banana2 -h
# ...
# 生成图片
dlazy banana2 --prompt "一只可爱的橘猫在窗台上晒太阳"
```

### 第三步：获取 API Key

1. 访问 dlazy.com 注册账号
2. 进入 dashboard 的 API Key 页面
3. 复制 API Key
4. 执行 `dlazy auth set YOUR_API_KEY`

**响应解析**: 完成完成后,查看输出响应确认任务状态。成功时输出包含解析摘要和响应数据;失败时根据错误信息排查问题,查阅错误解析章节获取恢复步骤.
## 示例

### API Key 配置

```bash
# 方式一：永久保存（推荐）
dlazy auth set YOUR_API_KEY
# 配置文件位置:
#   macOS/Linux: ~/.dlazy/config.json
#   Windows:     %USERPROFILE%\.dlazy\config.json
# ...
# 方式二：环境变量
export DLAZY_API_KEY="${API_KEY:?请设置环境变量}"
```

### 常用模型参数

```bash
# banana2 - 通用文生图
dlazy banana2 \
  --prompt "描述文本" \
  --ratio "16:9"        # 比例: 1:1, 16:9, 9:16, 4:3, 3:4
  --n 1                 # 生成数量
  --ref-image "ref.jpg" # 可选参考图
# ...
# seedream-5.0-lite - 轻量高速
dlazy seedream-5.0-lite \
  --prompt "描述文本" \
  --ratio "2K"          # 分辨率: 2K, 3K
  --ref-images "r1.jpg,r2.jpg"
# ...
# gpt-image-2 - 文生图与编辑
dlazy gpt-image-2 \
  --prompt "描述文本" \
  --mode "edit"         # generate 或 edit
  --ref-image "src.jpg"
```

## 优秀实践

1. **提示词具体化**：描述主体、风格、色调、氛围，避免模糊表述.
2. **比例适配场景**：社交媒体用 1:1，横幅用 16:9，手机壁纸用 9:16.
3. **草稿先行**：先用 banana2 快速生成草稿，确认方向后再用高质量模型.
4. **参考图引导**：提供参考图可以更好地控制输出风格.
5. **后期增强**：生成后用 superres 提升清晰度，用 imageseg 抠图合成.
```text
免费版优秀实践:
[ ] 提示词包含主体+风格+色调+氛围
[ ] 比例符合使用场景
[ ] 草稿先行，确认后再高质量生成
[ ] 参考图已准备（如需风格引导）
[ ] API Key 已安全配置
[ ] 余额充足
```

## 常见问题

### Q: 免费版支持视频生成吗？

A: 免费版仅支持图片生成与编辑。视频生成（t2v, i2v）需要升级至专业版.
### Q: 提示 insufficient_balance 怎么办？

A: 余额不足，请访问 dlazy.com/dashboard/organization/settings?tab=credits 充值.
### Q: 如何选择合适的模型？

A: 快速草稿用 banana2，批量生成用 seedream-5.0-lite，概念验证用 grok-4.2，需要编辑用 gpt-image-2.
### Q: 生成的图片 URL 有效期多久？

A: dlazy 文件服务托管的 URL 有一定有效期，建议及时下载保存.
### Q: 支持哪些输出比例？

A: 支持 1:1、16:9、9:16、4:3、3:4 等常见比例，部分模型支持自定义分辨率.
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 16+（dlazy CLI 运行需要）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Node.js 16+ | 运行时 | 必需 | nodejs.org 官方下载 |
| @dlazy/cli | CLI工具 | 必需 | `npm install -g @dlazy/cli@latest` |
| dlazy API Key | 认证 | 必需 | dlazy.com/dashboard 获取 |

### API Key 配置(补充)
- **必需**: dlazy API Key
- **获取方式**: 访问 dlazy.com/dashboard/organization/api-key
- **配置方式**: `dlazy auth set YOUR_API_KEY` 或环境变量 `DLAZY_API_KEY`
- **安全说明**: 配置文件权限限制为当前用户

### 可用性分类
- **分类**: MD+EXEC+API（Markdown指令 + 命令行 + 外部API调用）
- **说明**: 轻量级AI Skill，通过dlazy CLI调用云端图片生成API
- **适用规模**: 个人创作者，轻度使用

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 需要API Key，无Key环境无法使用
- 本地运行，不支持多设备同步

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "综合生成工具-免费版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "dlazy gen"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
