# 跨平台适配指南（English Edition）

本文件说明 `book-video-generator-en`（三分钟精读一本书 · 英文版）技能在各 AI Agent 平台上的安装与工具适配方法。

技能遵循 [Agent Skills 开放标准](https://agentskills.io)，核心组件（`SKILL.md` 格式、LLM 提示词、Python 脚本）**跨平台通用**，仅需适配平台专有工具（主要是图像生成）。

---

## 平台兼容性总览

| 组件 | WorkBuddy | OpenClaw | Codex CLI | TRAE Work | Claude Code |
|------|-----------|----------|-----------|-----------|-------------|
| SKILL.md 格式 | 原生 | 兼容 | 兼容 | 兼容 | 兼容 |
| LLM 提示词（英文） | 直接用 | 直接用 | 直接用 | 直接用 | 直接用 |
| Python 脚本 | 直接用 | 直接用 | 直接用 | 直接用 | 直接用 |
| 联网搜索 | WebSearch | 内置 | Shell/MCP | 内置 | 内置 |
| 图像生成 | ImageGen（内置） | 插件 / generate_image.py | generate_image.py | MCP / generate_image.py | 内置 / generate_image.py |
| 英文 TTS | edge-tts（默认） | edge-tts | edge-tts | edge-tts | edge-tts |
| 技能目录 | ~/.workbuddy/skills/ | ~/.openclaw/skills/ | ~/.codex/skills/ | ~/.trae/skills/ | ~/.claude/skills/ |

> 核心脚本**无任何平台硬编码路径**，统一使用 `os.path.join` / `pathlib.Path` 与 `sys.executable`，在 Windows / macOS / Linux 均可直接运行。

---

## 1. WorkBuddy（当前平台）

无需额外配置，技能已安装。

- 联网搜索：内置 `WebSearch` 工具
- 图像生成：内置 `ImageGen` 延迟工具（通过 ToolSearch + DeferExecuteTool 调用，Tencent Hunyuan）
- 英文 TTS：`generate_audio.py` 默认 `en-US-AriaNeural`（edge-tts，免费、无需 Key）
- Python 运行：托管 Python `C:/Users/chenjun/.workbuddy/binaries/python/versions/3.13.12/python.exe`

---

## 2. OpenClaw

### 安装

```bash
# 方式一：直接复制
cp -r ~/.workbuddy/skills/book-video-generator-en ~/.openclaw/skills/

# 方式二：通过 ClawHub 安装（需先发布）
openclaw skills install book-video-generator-en

# 方式三：从 Git 仓库安装
openclaw skills install git:yourname/book-video-generator-en
```

### 工具适配

OpenClaw 支持在 `SKILL.md` frontmatter 中声明 `tools`。如需原生图像生成，可声明一个指向 `scripts/generate_image.py` 的 handler；否则 CLI 阶段直接调用该脚本即可。

联网搜索：OpenClaw 内置 web search，无需配置。

图像生成：

```bash
# 任选一种 API（需对应 Key）
export GEMINI_API_KEY="..."      # 或 AGNES_API_KEY / OPENAI_API_KEY / ARK_API_KEY
python3 scripts/generate_image.py --prompt "flat illustration ..." --output images/scene_000.png --api gemini
# 批量（从 storyboard.json）
python3 scripts/generate_image.py --batch storyboard.json --output-dir images/ --api gemini
```

### 验证

```bash
openclaw skills verify book-video-generator-en
```

---

## 3. Codex CLI（OpenAI）

### 安装

```bash
# 1. 开启 Skills 功能（config.toml）
cat >> ~/.codex/config.toml << 'EOF'
[features]
skills = true
EOF

# 2. 复制技能目录
cp -r ~/.workbuddy/skills/book-video-generator-en ~/.codex/skills/

# 3. 重启 Codex CLI
# 4. 验证：在 Codex CLI 输入 /skills，确认 book-video-generator-en 出现
```

### 工具适配

**联网搜索**：Codex CLI 无内置搜索，两种方案：

方案 A — Shell 命令搜索（免安装）：
```bash
curl -s "https://www.google.com/search?q=book+title+author+summary" | python3 -c "..."
```
方案 B — 安装搜索 MCP 插件。

**图像生成**：Codex CLI 无内置图像生成，使用 `scripts/generate_image.py`（见上方 OpenClaw 示例）。`IMAGE_API` 环境变量可设默认 API（默认 `gemini`）。

**英文 TTS**：`generate_audio.py` 默认走 edge-tts，免费且无需 Key，联网即用。

### 注意事项

- Codex CLI 的 `SKILL.md` frontmatter 支持 `metadata.short-description`
- 技能也可放在项目级 `.codex/skills/` 或仓库根 `.agents/skills/`
- 渐进式披露：启动时仅加载 name + description

---

## 4. TRAE Work（字节跳动）

### 安装

```
1. 打开 TRAE Work IDE
2. 进入「规则和技能 → 技能 → 创建」
3. 选择「导入文件」，上传 SKILL.md
4. 将 scripts/ 和 references/ 目录复制到技能目录下
```

技能目录结构（TRAE 只扫描一级子目录）：
```
~/.trae/skills/
  book-video-generator-en/
    SKILL.md
    scripts/
      compose_video.py
      generate_audio.py
      generate_image.py
      generate_cover.py
    references/
      prompts.md
      CROSS_PLATFORM.md
      workflow-original.yaml
```

### 工具适配

- 联网搜索：TRAE Work 内置，直接可用。
- 图像生成：通过 MCP 接入图像服务，或用 `scripts/generate_image.py` + 环境变量。
- 英文 TTS：edge-tts 直接可用。

---

## 5. 其他兼容平台

Agent Skills 开放标准还被以下平台支持，本技能同样适用：

- **Claude Code** — `~/.claude/skills/`，与 WorkBuddy 格式几乎一致
- **Cursor** — 支持 Agent Skills 标准
- **GitHub Copilot** — 支持 Agent Skills 标准
- **VS Code** — 通过 Agent Skills 扩展
- **Letta** — 支持 Agent Skills 标准

安装方式统一为：将技能目录复制到对应平台的 skills 目录下。

---

## 通用注意事项

### Python 环境

所有平台执行脚本时使用 `python3`（Windows 上为 `python`）。确保依赖已安装：

```bash
pip install edge-tts imageio-ffmpeg pillow
```

如使用 `generate_image.py` 的火山引擎 / Gemini 后端，按需安装：
```bash
pip install volcengine-python-sdk[ark] google-genai   # 仅对应后端需要
```

### 英文 TTS（跨平台一致）

- 默认 `en-US-AriaNeural`（edge-tts，免费、无需 Key，联网即用）。
- 可选火山引擎英文音色 `en_us_amy` 等（需 `VOLC_TTS_API_KEY`）；未配置时自动回退 edge-tts。

### 字体（英文）

视频字幕烧录与封面图均使用英文/拉丁字体，脚本已内置跨平台自动检测：

| 系统 | 字体路径 | FontName |
|------|----------|----------|
| Windows | C:/Windows/Fonts/arial.ttf | Arial |
| macOS | /System/Library/Fonts/Supplemental/Arial.ttf | Arial / Helvetica |
| Linux | /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf | DejaVu Sans |

兜底顺序：优先检测上述路径 → `fc-list :lang=en` → 最后返回 `"Sans"`（交给 ffmpeg/libass 默认）。无中文字体需求，纯英文渲染无障碍。

### 路径分隔符

Python 脚本统一使用 `os.path.join()` 与 `pathlib.Path`，自动适配不同 OS 路径分隔符；ffmpeg 的 `subtitles` 滤镜对 Windows 路径已做特殊处理。

### 合成性能注意（重要）

`compose_video.py` 会对全部分镜做完整重编码（1080p + libx264 + libass 字幕烧录 + BGM/转场混音）。在**资源受限的沙箱/容器**中，整段重编码可能被静默杀进程（无报错、无输出）。

- 若在本机/有完整资源的终端运行，正常完成（约 2–3 分钟）。
- 若在受限沙箱运行失败，请在**关闭沙箱/资源不受限**的环境下重新执行合成步骤（仅本地 ffmpeg，无需联网）。
- 分步排错：可先单独跑 `make_ass` 看字幕、再单独跑短片段烧录验证滤镜，最后跑完整合成。

---

## 版本历史

| 日期 | 版本 | 变更 |
|------|------|------|
| 2026-07-29 | 1.0 | 从中文版 book-video-generator 派生英文版：提示词/字幕/配音全英文，字体改 Arial/Helvetica/DejaVu |
| 2026-07-29 | 1.1 | 补充跨平台适配文档（OpenClaw / Codex CLI / TRAE Work / Claude Code 等） |
