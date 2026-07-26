---
name: wechat-content-studio
description: "End-to-end WeChat Official Account article studio for Chinese公众号内容. Use when asked to write, test, package, typeset, generate covers for, publish, or verify WeChat articles or drafts. Enforces the full workflow: H/K/R topic check, article archetype, L1-L4 writing self-check, confirmed gpt-image-2 cover generation via LuisClaw relay, gzh-design HTML typesetting and validation, server-aware publishing, and draft verification. Applies even to test drafts or 'just run it once' requests."
---

# Wechat Content Studio

Use this skill to produce and publish 微信公众号 articles with the same full workflow every time. Treat test drafts, smoke tests, and temporary articles as real publishing work.

## Core Rule

Do not skip steps because the user says “试试”, “跑一遍”, “随便写一篇”, or “测试一下”. The article may be shorter, but the workflow remains complete.

## Required Workflow

1. Write the article.
   - Run H/K/R topic judgment: Happy, Knowledge, Resonance.
   - Pick one archetype: investigation, product experience, phenomenon analysis, tool sharing, or methodology sharing.
   - Write in a short-paragraph, human, first-person公众号 style.
   - Save a self-check record using `assets/templates/selfcheck-template.md`.
   - Run L1-L4 checks: banned words and punctuation, style consistency, content quality, human feeling.

2. Generate the cover.
   - Read `references/image2-policy.md`.
   - Use the project `image2-workflow.ps1 -Mode Draft` first.
   - Ask the user to confirm the prompt.
   - Only after confirmation, run `image2-workflow.ps1 -Mode Generate`.
   - Use `OPENAI_BASE_URL=https://luisclaw.cloud/v1` and `model=gpt-image-2`.

3. Typeset the body.
   - Use the local `gzh-design` skill.
   - Read the `gzh-design` SKILL.md before typesetting.
   - Generate a clean `<section>...</section>` HTML fragment.
   - Run `validate_gzh_html.py`; `ERROR` and body half-width punctuation `WARNING` must be zero.
   - Run `wrap_preview.py`.

4. Publish.
   - Prefer `publish-via-server.ps1`.
   - For gzh-design output, publish with `-ArticlePath <article.md> -HtmlPath <clean.html>`.
   - Run preflight before publishing.
   - After publishing, verify the returned `Media ID` with `-VerifyOnly` or `verify-draft.ps1`.

## Writing Rules

- Start from a concrete event, not a macro trend.
- Use short paragraphs and conversational rhythm.
- Avoid these phrases: `说白了`, `意味着什么`, `这意味着`, `本质上`, `换句话说`, `不可否认`, `综上所述`, `总的来说`, `首先`, `其次`, `最后`.
- Avoid Chinese body punctuation `：`, `——`, straight double quotes, and Chinese double quotes when the house style says to use corner quotes or no quotes.
- Use exact tool names such as Codex, OpenClaw, gzh-design, image2, and gpt-image-2.

## Publishing Safety

- Never package or write real AppSecret, API keys, server IPs, SSH users, account names, or logs into deliverables.
- Never publish if preflight fails.
- Never republish when draft verification says `DRAFT_EXISTS` unless the user explicitly confirms deleting or replacing that draft.
- Clear stale WenYan upload or token cache if WeChat returns `invalid media_id` or `access_token is invalid or not latest`, then retry once.

## Resources

- `references/workflow.md`: full command sequence and responsibilities.
- `references/image2-policy.md`: project-specific cover generation policy.
- `assets/templates/article-template.md`: starter article Markdown.
- `assets/templates/selfcheck-template.md`: writing self-check template.
- `assets/examples/`: a complete sample article, self-check, cover prompt, cover image, validated HTML, and preview.
