# Wechat Content Studio Workflow

## 1. Article

Create an article Markdown file with frontmatter:

```markdown
---
title: 文章标题
cover: ./output/imagegen/article-cover.png
---
```

Create a separate self-check file. Record:

- H/K/R topic judgment.
- Article archetype.
- AI role boundary.
- L1-L4 checks.

Run a simple scan for banned terms and punctuation before continuing.

## 2. Cover

Draft first:

```powershell
.\image2-workflow.ps1 -Mode Draft -Request "公众号文章封面，主题是..." -Slug "article-cover"
```

After user confirmation:

```powershell
.\image2-workflow.ps1 -Mode Generate `
  -PromptFile .\output\imagegen\prompts\article-cover.prompt.txt `
  -Out .\output\imagegen\article-cover.png
```

## 3. gzh-design Typesetting

Use the `gzh-design` skill and its theme components. For high-density workflow, methodology, operations, or internal memo articles, `橄榄手记` is usually a good default. For product analysis or strong opinions, choose a more suitable theme from `theme-index.md`.

Validate:

```powershell
python -X utf8 C:\Users\26240\.codex\skills\gzh-design\scripts\validate_gzh_html.py .\article_排版_主题.html
```

Generate preview:

```powershell
python -X utf8 C:\Users\26240\.codex\skills\gzh-design\scripts\wrap_preview.py .\article_排版_主题.html
```

Proceed only when validation reports no errors or warnings.

## 4. Publish

Preflight:

```powershell
.\publish-via-server.ps1 -PreflightOnly -ArticlePath .\article.md -HtmlPath .\article_排版_主题.html
```

Publish:

```powershell
.\publish-via-server.ps1 -ArticlePath .\article.md -HtmlPath .\article_排版_主题.html
```

Verify:

```powershell
.\publish-via-server.ps1 -VerifyOnly -KnownDraftMediaId "MEDIA_ID"
```

Success condition:

```text
DRAFT_EXISTS
Articles:
- 文章标题
```

## 5. Common Failures

- `invalid media_id`: clear WenYan upload cache and retry once.
- `access_token is invalid or not latest`: clear WenYan token cache and retry once.
- `40164 invalid ip`: do not retry blindly. Sync WeChat backend IP whitelist and local `credentials/wechat.json`.
- Existing draft found: do not republish unless the user explicitly wants a replacement.
