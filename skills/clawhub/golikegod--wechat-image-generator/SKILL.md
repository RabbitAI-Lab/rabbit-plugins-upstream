---
name: wechat-image-generator
description: ⚠️ DEPRECATED since 2026-07-05 — 已并入 yuanzi-wechat-suite。本技能不再维护，请改用 mega-package 一键装：写作 + 读稿 + 配图 + 发布 4 站流水线。
tags: [yuanzi, gzh, articles, wechat, image, suite:yuanzi-wechat-series, deprecated, redirect:yuanzi-wechat-suite]
version: 1.0.4
homepage: https://github.com/jingyu525/wechat-image-generator
metadata:
  openclaw: { "emoji": "🎨", "requires": { "bins": ["python3"] } }
  series: yuanzi-wechat-series
  series-position: 配图帆
  fork-of: wechat-image-generator@1.0.2 (jingyu525)
  deprecated: true
  deprecated-since: 2026-07-05
  redirect-to: yuanzi-wechat-suite
  redirect-version: 2.1.0
---

# WeChat Image Generator

> # ⚠️ DEPRECATED — 自 2026-07-05 起本技能已并入 `yuanzi-wechat-suite`
>
> **请改用 mega-package 一键装：**
>
> ```bash
> clawhub install yuanzi-wechat-suite
> ```
>
> 本技能的 `generate.py` / `auto_screenshot.py` 已迁入 `yuanzi-wechat-suite/scripts/image-gen/`，并接入 `yuanzi.py image` 总调度命令。零 token 配图不中断。

Generate beautiful images for WeChat articles with zero token cost and auto-screenshot.

## Quick Start

### 1. Cover Image (封面图)
```bash
python3 scripts/generate.py cover \
  --title "我的第一个开源项目" \
  --subtitle "Token 成本降低 90%" \
  --output output/cover.png
```

### 2. Comparison Image (对比图)
```bash
python3 scripts/generate.py compare \
  --left "# Markdown\n**Bold** text" \
  --right "HTML 渲染结果" \
  --label "1 秒转换" \
  --output output/compare.png
```

### 3. Chart Image (数据图)
```bash
python3 scripts/generate.py chart \
  --data "Token消耗:8000,650|生成耗时:20,1" \
  --labels "AI生成,预制模板" \
  --output output/chart.png
```

## Workflow

1. Run generator script with parameters
2. Script creates HTML with embedded data
3. Opens in browser via OpenClaw browser tool
4. Auto-screenshot and save to output folder

## Design Philosophy

**Zero token cost**: All templates are pre-built HTML/CSS
**Auto-screenshot**: Integrated with OpenClaw browser tool
**Customizable**: Easy to modify templates for different styles

## Token Cost Analysis

Per image generation:
- Read SKILL.md: ~500 tokens (first time only)
- Execute script: ~100 tokens
- Browser screenshot: ~50 tokens

**Total: ~650 tokens** vs DALL-E/Midjourney ~1000-5000 tokens per image.

## Requirements

- Python 3
- OpenClaw browser tool (for auto-screenshot)

---

## 📦 元子公众号图文系列

> 🦞 yuanzi-wechat-series · 第 3/4 站「配图帆」

**安装方式：** `clawhub install yuanzi-image-generator`

本技能属于「元子公众号图文系列」4 件套之一：
1. 写作舵 — `yuanzi-article-master`
2. 读稿锚 — `yuanzi-article-extractor`
3. **配图帆** — `yuanzi-image-generator`（本技能）
4. 发布桨 — `yuanzi-wechat-publisher`

**注：** 本技能另有 `wechat-image-generator` 同名发布（受 AMBIGUOUS_SKILL_SLUG 限制未合并），使用建议以 yuanzi- 前缀版为准。

推荐工作流：读稿 → 写作 → 配图 → 发布。

v1.0.3 元子系列升级：归 jingyu525 v1.0.2，加入元子系列 tag + 导航。

*🦞 元子公众号图文系列 v1.0.3 · 2026-07-04 · yuanzi- 前缀版*
