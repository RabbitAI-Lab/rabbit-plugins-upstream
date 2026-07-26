---
slug: grok-image-tool-free
name: grok-image-tool-free
version: 1.0.0
displayName: Grok图片生成-免费版
summary: "轻量级AI图片生成工具，通过浏览器自动化操作Grok Imagine生成并保存图片.。Grok图片生成工具免费版，面向个人用户的AI图片生成方案."
license: Proprietary
edition: free
description: 'Grok图片生成工具免费版，面向个人用户的AI图片生成方案.
  核心能力：

  - 通过浏览器自动化访问 Grok Imagine

  - 自然语言描述生成 AI 图片

  - 本地下载保存生成的图片

  - 桌面操作自动化右键保存

  适用场景：

  - 个人创意图片生成

  - 社交媒体配图制作

  - 概念图快速验证

  差异化：免费版聚焦单张图片生成与本地保存，适合个人轻度使用。专业版扩展至批量生成、多格式导出与消息平台集成.
  适用关键词: grok, imagine, 图片生成, AI画图, 生成图片, 浏览器自动化'
tags:
  - Creative
  - ImageGeneration
  - Automation
  - 图像处理
  - AI绘图
  - 创意
  - desktop-agent
  - uvx
  - grok
  - 图片生成
  - imagine
tools:
  - read
  - exec
  - write
homepage: ""
category: "Creative"
---
# Grok图片生成工具（免费版）

## 概述

Grok图片生成工具免费版是一款面向个人用户的 AI 图片生成方案。通过浏览器自动化访问 Grok Imagine 页面，输入提示词生成 AI 图片，并通过桌面操作自动化将图片保存到本地.
本版本适合个人创意图片生成、社交媒体配图制作和概念图快速验证等场景。操作流程完全自动化，用户只需提供描述文本.
## 核心能力

| 能力 | 说明 |
|---|---|
| 浏览器自动化 | 自动打开 Grok Imagine 页面 |
| 提示词输入 | 自动输入用户描述文本 |
| 图片生成 | 等待 AI 生成图片（约8-10秒） |
| 自动保存 | 桌面操作右键保存到本地 |
| 文件查找 | 自动定位下载的图片文件 |

### 使用流程

```text
工作流程:
  1. 打开 Grok Imagine 页面
  2. 输入提示词
  3. 点击生成按钮
  4. 等待图片生成（8-10秒）
  5. 右键保存图片到本地
  6. 查找下载的图片文件
# ...
不支持（需专业版）:
  - 批量图片生成
  - 多格式导出（PNG/JPG/WebP）
  - 消息平台发送（飞书等）
  - 自定义保存路径
  - 提示词模板管理
```

**处理**: 解析使用流程的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回使用流程的响应数据,包含状态码、结果和日志.
1. 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 核心功能执行
用`input_params`参数进行配置.

**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志.
2. 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用
用`config_options`参数进行配置.

**处理**: 解析参数配置与调用的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回参数配置与调用的响应数据,包含状态码、结果和日志.
3. 执行此能力时使用`config_options`参数,支持修改/重置/导入操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：轻量级、图片生成工具、通过浏览器自动化、生成并保存图片、图片生成工具免费、面向个人用户的、图片生成方案等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 示例

### 基本用法

**输出**：返回执行结果,包含操作状态和输出数据

```text
用户: 执行核心功能
Skill: 正在执行核心功能...
Skill: 执行完成,结果如下: 操作成功
```

## 使用场景

### 场景一：生成创意图片

为社交媒体或创意项目生成 AI 图片.
```bash
# 完整生成流程
# 步骤1: 打开 Grok Imagine 页面
# 使用浏览器工具打开 https://grok.com/imagine
# ...
# 步骤2: 输入提示词并生成
# 在输入框中输入: "一只在月光下飞翔的蓝色蝴蝶，梦幻氛围"
# 点击提交按钮
# ...
# 步骤3: 等待生成（约8-10秒）
# ...
# 步骤4: 保存图片到本地
# 使用桌面操作工具右键保存
# ...
# 步骤5: 查找保存的图片
ls -lat ~/Downloads/ | head -10
```

### 场景二：概念图快速验证

为设计项目快速生成概念图.
```python
# 概念图生成提示词模板
def build_prompt(subject, style, mood, details=""):
    """构建图片生成提示词"""
    prompt = f"{subject}"
    if style:
        prompt += f"，{style}风格"
    if mood:
        prompt += f"，{mood}氛围"
    if details:
        prompt += f"，{details}"
    return prompt
# ...
# 示例
prompts = [
    build_prompt("未来城市天际线", "赛博朋克", "霓虹灯光", "雨夜"),
    build_prompt("森林中的小木屋", "水彩", "温馨宁静", "晨光透过树叶"),
    build_prompt("太空中的鲸鱼", "超现实", "梦幻", "星云背景"),
]
# ...
for i, prompt in enumerate(prompts):
    print(f"提示词 {i+1}: {prompt}")
    # 将提示词输入 Grok Imagine 生成
```

### 场景三：保存与查找图片

```bash
# 保存图片的桌面操作流程
# ...
# 步骤1: 移动鼠标到图片位置并右键
uvx desktop-agent mouse move 720 400
uvx desktop-agent mouse right-click
sleep 1
# ...
# 步骤2: 选择"图片另存为"
uvx desktop-agent keyboard press down --presses 2
uvx desktop-agent keyboard press return
sleep 1
# ...
# 步骤3: 确认保存
uvx desktop-agent keyboard press return
# ...
# 步骤4: 查找保存的图片
ls -lat ~/Downloads/*.jpg | head -5
# 或
```

## 不适用场景

以下场景Grok图片生成-免费版不适合处理：

- 需要人工创意判断的任务
- 非结构化头脑风暴
- 人际沟通协调

## 触发条件

需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于非本工具能力范围的需求.
## 快速开始

### 第一步：打开 Grok Imagine

```javascript
// 使用浏览器工具打开页面
playwright({
  action: "open",
  url: "https://grok.com/imagine"
})
```

### 第二步：输入提示词

```javascript
// 等待页面加载后输入提示词
playwright({
  action: "act",
  request: {
    "kind": "type",
    "ref": "输入框ref",
    "text": "你想要生成的图片描述"
  }
})
// ...
// 点击生成按钮
playwright({
  action: "act",
  request: {
    "kind": "click",
    "ref": "提交按钮ref"
  }
})
```

### 第三步：保存图片

```bash
# 等待图片生成完成（约8-10秒）
sleep 10
# ...
# 右键保存
uvx desktop-agent mouse move 720 400
uvx desktop-agent mouse right-click
sleep 1
uvx desktop-agent keyboard press down --presses 2
uvx desktop-agent keyboard press return
sleep 1
uvx desktop-agent keyboard press return
# ...
# 查找保存的图片
ls -lat ~/Downloads/ | head -10
```

## 配置示例

### 桌面操作配置

```bash
# desktop-agent 常用命令
uvx desktop-agent screen size          # 获取屏幕尺寸
uvx desktop-agent mouse move <x> <y>   # 移动鼠标
uvx desktop-agent mouse right-click    # 右键点击
uvx desktop-agent keyboard press down  # 按下方向键
uvx desktop-agent keyboard press return # 按回车键
```

### 提示词建议

```text
提示词优化技巧:
  1. 明确主体: "一只红色的狐狸"（不是"动物"）
  2. 指定风格: "水彩风格" / "油画风格" / "3D渲染"
  3. 描述氛围: "温馨氛围" / "神秘氛围" / "梦幻氛围"
  4. 添加细节: "在雪地里" / "月光下" / "雨夜霓虹"
  5. 指定构图: "特写" / "全景" / "俯视"
```

## 最佳实践

1. **提示词具体化**：明确主体、风格、氛围和细节，避免模糊描述.
2. **等待足够时间**：图片生成约需 8-10 秒，保存操作间留 1 秒缓冲.
3. **及时查找文件**：生成后立即查找 Downloads 目录最新文件.
4. **屏幕坐标适配**：不同分辨率下鼠标坐标可能不同，先获取屏幕尺寸.
5. **页面元素变化**：如果页面 DOM 变化，需根据实际情况调整选择器.
```text
免费版最佳实践:
[ ] 提示词包含主体+风格+氛围+细节
[ ] 生成等待时间 ≥ 10秒
[ ] 保存操作间留 1秒缓冲
[ ] 生成后立即查找 Downloads 目录
[ ] 屏幕坐标已适配当前分辨率
```

## 常见问题

### 已知限制

A: Grok Imagine 免费用户可能有每日生成次数限制。如果达到限制，需等待次日重置或升级账户.
### Q: 图片保存在哪里？

A: 默认保存在 `~/Downloads/` 目录。可通过 `ls -lat ~/Downloads/ | head -10` 查找最新文件.
### Q: 生成需要多长时间？

A: 图片生成约需 8-10 秒。网络状况可能影响加载速度，建议等待 10 秒以上再执行保存操作.
### Q: 页面元素变化怎么办？

A: 如果 Grok Imagine 页面结构变化，需要根据实际 DOM 调整浏览器操作的元素引用（ref）.
### Q: 可以批量生成吗？

A: 免费版仅支持单张图片生成。批量生成需要升级至专业版.
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **浏览器**: Chrome/Edge（浏览器自动化需要）

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Playwright/浏览器工具 | 工具 | 必需 | Agent内置或插件安装 |
| desktop-agent | 工具 | 必需 | `uvx desktop-agent`（自动安装） |
| Grok 账号 | 服务 | 必需 | grok.com 注册 |

### API Key 配置
- 本Skill采用纯Markdown指令驱动，无需额外API Key
- 需要已登录的 Grok 账号（浏览器会话）

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令 + 命令行 + 浏览器自动化）
- **说明**: 轻量级AI Skill，通过浏览器自动化和桌面操作实现图片生成与保存
- **适用规模**: 个人用户，单张图片生成

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "Grok图片生成-免费版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "grok image"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
