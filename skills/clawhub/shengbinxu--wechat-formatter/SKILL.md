---
name: wechat-formatter
description: Convert markdown articles to WeChat public account (微信公众号) formatted HTML using the mdnice library. This skill should be used when the user has a markdown file and wants to publish it on WeChat public account, or when the user asks to "微信公众号排版" or "convert to WeChat format". Supports 20+ themes, code highlighting, and Mac-style rendering.
agent_created: true
---

# WeChat Article Formatter

Convert markdown to WeChat public account styled HTML using the mdnice library with Playwright backend.

## When to Use

- User has a markdown article and asks to publish on WeChat public account
- User asks for "微信公众号排版", "公众号格式", "微信排版"
- User wants to convert markdown to WeChat-compatible styled HTML

## Workflow

### 1. Install Dependencies (if not already installed)

The conversion requires `mdnice`, `requests`, and Playwright's Chromium browser:

```bash
pip install mdnice requests
playwright install chromium
```

Use WorkBuddy's managed Python environment (the assistant will resolve the correct paths automatically):
- The assistant runs the script via the managed Python runtime
- Install dependencies into the managed venv: `pip install mdnice requests`

### 2. Convert Markdown

Run the conversion script:

```bash
python <skill_dir>/scripts/convert.py <markdown_file> [options]
```

Options:
- `--theme <name>`: Theme (default: `orangeHeart`). See themes section below.
- `--code-theme <name>`: Code highlight (default: `wechat`)
- `--output-dir <dir>`: Output directory (default: same as markdown)
- `--mac-style`: Enable Mac style (default: True)
- `--list-themes`: List all available themes

### 3. Deliver Result

After conversion, the generated HTML file will be at `<markdown_file>_wechat.html` in the output directory.

The conversion script automatically fixes fonts: mdnice defaults to light-weight fonts (PingFangSC-Light, STHeitiSC-Light) that are hard to read on mobile. The script replaces them with a readable Chinese font stack (PingFang SC, Hiragino Sans GB, Microsoft YaHei, Noto Sans CJK SC).

Present the HTML file to the user with the `present_files` tool. The HTML contains inline styles ready to copy-paste into the WeChat public account editor.

**Important**: Remind the user that WeChat public account articles do not allow external third-party links. If the markdown contains external links, the user should remove or replace them before publishing.

## Available Themes

Run `python <skill_dir>/scripts/convert.py --list-themes` to show all themes.

Common choices for different article styles:
- `orangeHeart` - Warm orange accent (default, friendly and modern)
- `wechatFormat` - Classic WeChat style
- `scienceBlue` - Tech article with blue accents
- `simple` - Minimal clean style
- `extremeBlack` - High contrast dark text
- `shanchui` - Warm yellow tones

Code themes: `wechat`, `atom-one-dark`, `atom-one-light`, `monokai`, `github`, `vs2015`, `xcode`

## Notes

- The conversion uses Playwright in headless mode to render the markdown in mdnice's online editor, then extracts the styled HTML via CDP
- This relies on external mdnice editor URLs (default + fallback). If both are unreachable, conversion will fail — check network connectivity
- The output HTML uses inline styles, which is what WeChat editor requires
- No image uploader is configured by default; images in the markdown will remain as local references
