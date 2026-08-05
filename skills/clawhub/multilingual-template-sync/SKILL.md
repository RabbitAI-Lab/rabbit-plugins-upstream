---
name: multilingual-template-sync
description: Update multilingual customer service response templates and sync them across platforms. Use when adding new languages to response templates, translating KB templates, syncing template files to Feishu Wiki, creating GitHub issues for documentation/i18n updates, or any workflow that combines local template editing with Feishu Wiki publishing and GitHub issue tracking. Triggers on phrases like "add language to templates", "sync to Feishu Wiki", "update customer service responses", "translate templates", "publish to wiki", or "i18n template update".
---

# Multilingual Template Sync

Update multilingual customer service templates, sync to Feishu Wiki, and track changes on GitHub.

## Workflow

1. **Update local template** — Add new language translations to the markdown template file
2. **Sync to Feishu Wiki** — Publish the updated file to the customer service knowledge base
3. **Create GitHub issue** — Document the change for tracking
4. **Repeat** — Use the helper script to add more languages structurally

## Quick start

### Adding a new language

1. Read the template file (e.g. `kb-templates/common-responses.md`)
2. For each `## N. Scenario` section, add a `### 🇫🇷 Français` block with the translation
3. Update the TOC, supported-languages line, and last-updated date
4. For structural scaffolding (inserts `_TRANSLATE_` placeholders), run:
   ```bash
   python3 scripts/add_language.py <file> <lang-code> <lang-name> <flag>
   ```

### Sync to Feishu Wiki

```bash
export FEISHU_APP_ID=... FEISHU_APP_SECRET=...
bash scripts/sync-to-feishu.sh <file-path> <wiki-space-id> <parent-node-token>
```

Requires Feishu app credentials with wiki write access. See [references/workflow.md](references/workflow.md) for API details.

### Create GitHub issue

```bash
export GITHUB_TOKEN=...
bash scripts/create-github-issue.sh <owner/repo> "<issue title>" <body.md>
```

### Adding more languages later

Use `scripts/add_language.py` to insert structural placeholders, then fill in translations.

## Reference

- **[references/workflow.md](references/workflow.md)** — Full workflow, API references, environment variable checklist, language code table

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/sync-to-feishu.sh` | Upload markdown to Feishu Wiki via open API |
| `scripts/create-github-issue.sh` | Create a GitHub issue with title/body/labels |
| `scripts/add_language.py` | Insert new language placeholders into template sections |

## Translation quality

- Keep tone consistent: polite, professional, concise
- Match formality level across languages (use formal register for customer service)
- Preserve placeholders, numbers, and timeframes exactly
- Flag uncertain translations rather than guessing
