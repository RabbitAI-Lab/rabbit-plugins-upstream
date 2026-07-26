# text-to-elegant-image

> Turn Markdown or plain text into beautifully typeset, high-resolution long images (share cards / posters) — with 18 built-in visual styles.

Generates a self-contained HTML file and renders it to a crisp PNG via headless Chrome (Puppeteer). Designed for AI agents (OpenClaw / Claude Code / Cursor, etc.) as a skill, but the scripts also run standalone.

## Features

- **18 built-in visual styles** — Cyberpunk/Tech, Minimalist, Apple Premium, Cowork Light-Tech, Newspaper, Bloomberg Terminal, Ink Scroll, Steampunk, XiaoHongShu/REDNote, Morandi, Glassmorphism, Palace, Fresh, Earthy, Dreamy, Macaron, Carbon, Vivid.
- **High-DPI output** — 2× `deviceScaleFactor` for retina-sharp PNGs.
- **Auto height cropping** — measures the real content height and trims trailing whitespace precisely.
- **No external assets** — icons are pure CSS/inline SVG; nothing loads over the network, so rendering never breaks.
- **Cross-platform Chrome detection** — Linux / macOS / WSL, no manual config.
- **Configurable output dir** — via `T2EI_OUTPUT_DIR` env var (defaults to `./output`).
- **Footer control** — default footer, custom author line, or no footer.

## Requirements

- **Node.js** ≥ 18
- **Chrome / Chromium** (any recent build; auto-detected)
- **puppeteer-core** (installed on first run via `setup.sh`)

## Quick Start

```bash
# Clone
git clone https://github.com/Songhonglei/text-to-elegant-image.git
cd text-to-elegant-image

# Install dependency (puppeteer-core)
bash scripts/setup.sh

# Render an HTML file to PNG
node scripts/export_image.js /path/to/page.html ./output/card.png 600
```

As an AI-agent skill, point your agent at `SKILL.md` — it describes the full workflow (parse content → pick a style from `resources/styles_reference.md` → generate HTML → screenshot).

## Output directory

Resolved in this priority order:

1. Path passed explicitly on the command line
2. `T2EI_OUTPUT_DIR` environment variable
3. Default: `./output`

```bash
export T2EI_OUTPUT_DIR="$HOME/my-images"   # optional, persist in ~/.bashrc
```

## Styles

All 18 styles ship with complete CSS + HTML skeletons in [`resources/styles_reference.md`](./resources/styles_reference.md). Each uses a `.container` base plus a namespaced class set (e.g. `.mo-*` for Morandi, `.gl-*` for Glass), so styles never collide.

> ⚠️ **No emoji in generated HTML** — headless Chrome lacks color-emoji fonts and renders them as tofu boxes. Use CSS shapes / inline SVG instead. (Enforced in `SKILL.md`.)

## Image delivery

This open-source edition focuses purely on **text → elegant image** generation and returns a local PNG path. Auto-pushing images to IM channels (WeChat / Telegram / Slack, etc.) is **not built in** — wire up your platform's Bot/API downstream if you need it (optional adapters may come in a future version).

## Install in your AI agent

| Agent | Install |
|---|---|
| OpenClaw | `clawhub install text-to-elegant-image` |
| Claude Code | Manual: copy to `~/.claude/skills/` |
| Cursor | Manual: copy to `.cursor/skills/` |

## License

MIT — see [LICENSE](./LICENSE).

## Author

Evan Song · [github.com/Songhonglei](https://github.com/Songhonglei)

## Changelog

### v1.0.0 (2026-07-13)

- Initial public release: 18 visual styles, high-DPI headless-Chrome rendering, configurable output dir.
