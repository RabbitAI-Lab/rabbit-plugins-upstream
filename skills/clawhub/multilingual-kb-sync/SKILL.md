---
name: multilingual-kb-sync
description: "Add new language translations to customer service response templates and sync them across platforms. Use when: (1) adding new languages to kb-templates/common-responses.md, (2) updating multilingual customer service templates, (3) syncing template changes to Feishu Wiki knowledge base, (4) creating GitHub issues for template updates, (5) maintaining multilingual customer service response templates. Triggers on phrases like 'add language to customer service templates', 'update multilingual responses', 'sync KB templates', 'translate customer service replies'."
---

# Multilingual KB Template Sync

Maintain and propagate multilingual customer service response templates across local files, Feishu Wiki, and GitHub.

## Workflow

### 1. Update Local Template

Edit `kb-templates/common-responses.md` (workspace-relative).

- Each template section has language subsections: `🇨🇳 中文`, `🇬🇧 English`, `🇫🇷 Français`, `🇰🇷 한국어`, etc.
- When adding a new language, add a subsection under **every** existing template with the translated text.
- Keep the section numbering and emoji flags consistent.
- Update the metadata table at the bottom: `支持语言`, `模板数量`, `最后更新`.
- Verify all templates have the same number of language subsections (no missing translations).

### 2. Sync to Feishu Wiki

Run `scripts/sync-feishu.sh` with required env vars:

```bash
FEISHU_APP_ID=xxx FEISHU_APP_SECRET=xxx FEISHU_WIKI_SPACE_ID=xxx FEISHU_DOC_TOKEN=xxx \
  bash scripts/sync-feishu.sh <path-to-common-responses.md>
```

The script:
1. Obtains a tenant access token from Feishu Open API.
2. Reads the local markdown file.
3. Creates or updates the target Wiki document via the Feishu Wiki API (`/open-apis/wiki/v2/spaces/{space_id}/nodes`).
4. Converts markdown to Feishu docx blocks (simple conversion: headings → heading blocks, paragraphs → text blocks).

If the document already exists (FEISHU_DOC_TOKEN set), it updates; otherwise it creates a new node under the space.

**Prerequisites:** Feishu app with `wiki:wiki` and `docx:document` permissions. Set `channels.feishu.enabled=true` in OpenClaw config or provide credentials via env vars.

### 3. Create GitHub Issue

Run `scripts/create-github-issue.sh`:

```bash
GITHUB_TOKEN=ghp_xxx GITHUB_REPO=owner/repo \
  bash scripts/create-github-issue.sh <path-to-common-responses.md> <changelog-summary>
```

The script:
1. Reads the template file to extract metadata (languages, template count, last updated).
2. Generates an issue title like `[i18n] Add XX/YY translations to common-responses.md`.
3. Generates a body with changelog and metadata.
4. Creates the issue via `gh api` or direct REST call.

**Prerequisites:** `gh` CLI installed and authenticated, or `GITHUB_TOKEN` env var with repo scope.

### 4. Commit and Push (optional)

```bash
git add kb-templates/common-responses.md
git commit -m "i18n: add <languages> to common-responses.md"
git push
```

## Adding a New Language (Checklist)

1. Translate all template sections in `common-responses.md`.
2. Add flag emoji and language name heading for each section.
3. Update metadata table.
4. Run Feishu sync script.
5. Run GitHub issue script.
6. Commit changes.

## Supported Languages

| Code | Language | Flag |
|------|----------|------|
| zh | 中文 | 🇨🇳 |
| en | English | 🇬🇧 |
| fr | Français | 🇫🇷 |
| ko | 한국어 | 🇰🇷 |

Add more by appending to this table and to every template section.

## Scripts

- `scripts/sync-feishu.sh` — Sync markdown to Feishu Wiki
- `scripts/create-github-issue.sh` — Open a GitHub issue for the update

## References

- `references/feishu-api.md` — Feishu Wiki API notes
- `references/translation-guide.md` — Translation quality guidelines
