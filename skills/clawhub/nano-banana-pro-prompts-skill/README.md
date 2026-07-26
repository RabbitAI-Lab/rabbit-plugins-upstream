# AI Image Prompt Recommender — 26,000+ Nano Banana Pro Prompts

[![Prompts](https://img.shields.io/badge/Prompts-26624-brightgreen)](https://huggingface.co/datasets/Goku-OpenLab/nano-banana-pro-prompts-datasets)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-orange)](https://github.com/gokuscraper/nano-banana-pro-prompts-skill)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![English](https://img.shields.io/badge/English-blue)](README.md) [![简体中文](https://img.shields.io/badge/简体中文-red)](README.zh.md)

> **Stop spending hours hunting for the right AI image prompt.** Tell your AI assistant what you need in one sentence — it searches 26,000+ curated Nano Banana Pro prompts and returns the top 3 matches with sample images, ready to use.
>
> 🖼️ [Browse the Dataset →](https://huggingface.co/datasets/Goku-OpenLab/nano-banana-pro-prompts-datasets)

![Demo](public/cover.png)

## What Is This?

An **AI agent skill** that gives Claude, OpenClaw, Cursor, and other AI assistants the ability to intelligently search a curated library of **26,000+ Nano Banana Pro (Gemini image model) prompts**, recommend the best matches for your use case, and even customize prompts based on your content.

**Nano Banana Pro** is Google's Gemini image generation model — one of the most capable AI image generators available today. High-quality prompts are the key to great results.

## Why Use This Skill?

- ✅ **26,000+ prompts** — massive library covering diverse use cases
- ✅ **Every prompt includes sample images** — see the result before you copy
- ✅ **Smart semantic search** — describe what you need, the AI finds the match
- ✅ **Content remix mode** — paste your article or video script, get a custom prompt
- ✅ **Multi-language** — responds in your language, always provides English prompt for generation
- ✅ **Bilingual data** — prompts available in both English and Chinese

---

## Installation

### OpenClaw (Recommended)

```bash
clawhub install nano-banana-pro-prompts-skill
```

Or search inside OpenClaw chat:

> "Install the nano banana pro prompts skill from clawhub"

### Claude Code

```bash
npx skills i gokuscraper/nano-banana-pro-prompts-skill
```

### Other AI Assistants (Cursor, Codex, Gemini CLI, Windsurf)

```bash
# Universal installer — auto-detects your AI assistant
npx skills i gokuscraper/nano-banana-pro-prompts-skill
```

### Manual / openskills

```bash
npx openskills install gokuscraper/nano-banana-pro-prompts-skill
```

---

## How to Use

### Mode 1: Direct Search

Just describe what you need:

```
"Find me a cyberpunk-style avatar prompt"
"I need prompts for travel blog article covers"
"Looking for a product photo on white background"
"Help me find a YouTube thumbnail for a tech review video"
```

You'll get up to 3 recommendations with:
- Translated title & description (in your language)
- The exact English prompt to copy
- Sample images to preview the style

### Mode 2: Content Illustration (Remix)

Paste your content and ask for a matching illustration:

```
"Here's my article about startup failure — help me create a cover image:
[paste article text]"

"I need a thumbnail for this video script: [paste script]"

"Generate an illustration for this podcast episode about AI: [paste notes]"
```

The skill will:
1. Recommend matching style templates
2. Ask a few questions to personalize (gender, mood, setting)
3. Generate a customized prompt tailored to your content

---

## Data Overview

| Item | Details |
|------|---------|
| Total Prompts | 26,624 |
| Languages | English, Chinese (bilingual) |
| Source | [GokuOpenLab Dataset](https://huggingface.co/datasets/Goku-OpenLab/nano-banana-pro-prompts-datasets) |
| License | Skill: MIT · Dataset: CC BY 4.0 |
| Format | JSONL (one prompt per line) |

---

## How It Works

```
User describes need
      ↓
Searches prompt library (token-efficient grep, never loads full file)
      ↓
Returns top 3 prompts with images + translated descriptions
      ↓
[Optional] User picks one → Skill remixes it to match their content
```

**Token-efficient by design**: The skill never loads the full prompt file. It uses grep-style search to extract only matching prompts, keeping token usage minimal even with 26,000+ prompts in the library.

---

## Data Source

Prompts are curated from the open community, sourced from the [GokuOpenLab dataset](https://huggingface.co/datasets/Goku-OpenLab/nano-banana-pro-prompts-datasets) on HuggingFace — 26,624 prompts with full metadata, preview images, and bilingual (EN/ZH) support.

*Prompts curated from the open community by [GokuOpenLab](https://prompthub.gokuscraper.com/) ❤️*

---

## Frequently Asked Questions

**Q: What is Nano Banana Pro?**
Nano Banana Pro is Google's Gemini image generation model (model ID: `gemini-3-pro-image-preview`). It produces high-quality, photorealistic and artistic images from text prompts.

**Q: Do I need an account to use this skill?**
No. The skill is completely free and works with any AI assistant that supports custom skills (Claude Code, OpenClaw, Cursor, Codex, Gemini CLI).

**Q: How is this different from just searching Twitter for prompts?**
The library is pre-structured with 26,000+ entries — you don't have to scroll through noise. Every prompt includes sample images so you know what you're getting. The remix mode lets you personalize a template to match your specific content.

**Q: Can I contribute prompts?**
The source dataset is CC BY 4.0; this skill code is MIT. Visit the [HuggingFace dataset](https://huggingface.co/datasets/Goku-OpenLab/nano-banana-pro-prompts-datasets) to learn more.

**Q: How often is the library updated?**
The dataset on HuggingFace is updated regularly by the GokuOpenLab community.

**Q: Does this work with other image generation models?**
The prompts are optimized for Nano Banana Pro (Gemini), but many work well with other models like GPT Image, Midjourney, DALL-E, Flux, and Stable Diffusion.

**Q: What's the difference between OpenClaw and Claude Code installation?**
OpenClaw uses the `clawhub install` command and integrates directly into your OpenClaw agent workspace. Claude Code uses `npx skills i` and installs into your Claude project context. Both use the same SKILL.md and prompt library.

---

## Project Structure

```
nano-banana-pro-prompts-skill/
├── SKILL.md                 # Skill instructions (works with Claude Code, OpenClaw, Cursor, etc.)
├── README.md
├── README.zh.md
├── package.json
├── scripts/
│   └── setup.js             # Downloads prompt library from HuggingFace
├── references/              # Auto-downloaded prompt data
│   ├── .gitkeep
│   └── metadata.jsonl       # 26,000+ prompts (generated by setup.js)
└── .claude-plugin/
    └── marketplace.json
```

---

## Development

### Prerequisites

- Node.js 18+

### Setup

```bash
pnpm install
```

This automatically downloads the prompt library from HuggingFace. To manually update:

```bash
node scripts/setup.js --force
```

---

## Related Projects

- 🖼️ [GokuOpenLab Dataset](https://huggingface.co/datasets/Goku-OpenLab/nano-banana-pro-prompts-datasets) — Source dataset on HuggingFace (26,000+ prompts, images, metadata)

## Related Tools

- [Claude Code](https://claude.com/claude-code) — Anthropic's terminal-native AI agent
- [OpenClaw](https://openclaw.ai) — AI agent platform with skill ecosystem
- [skills CLI](https://www.npmjs.com/package/skills) — Universal AI skills installer

---

## License

MIT © [GokuOpenLab](https://huggingface.co/Goku-OpenLab)
