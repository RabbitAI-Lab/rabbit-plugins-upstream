# Workflow Reference

## End-to-end multilingual template update process

### 1. Update local template

1. Read the existing template file (e.g. `kb-templates/common-responses.md`)
2. For each scenario section, add a new `### 🇫🇷 Français` (or target language) block
3. Translate all existing scenarios into the new language
4. Update the table of contents and "supported languages" line
5. Update the "最后更新" / last-updated date

### 2. Sync to Feishu Wiki

**Prerequisites:**
- Feishu app with wiki read/write permissions
- `FEISHU_APP_ID` and `FEISHU_APP_SECRET` env vars set
- Target wiki space ID and parent node token

**Steps:**
1. Run `scripts/sync-to-feishu.sh <file> <space-id> <parent-token>`
2. The script obtains a tenant access token, creates a new wiki node, and inserts content
3. For production use, enhance the markdown→Feishu blocks conversion (the script currently inserts raw text)
4. Verify the node appears in the Feishu Wiki UI

**Feishu API references:**
- Auth: `POST /open-apis/auth/v3/tenant_access_token/internal`
- Create wiki node: `POST /open-apis/wiki/v2/spaces/:space_id/nodes`
- Create doc blocks: `POST /open-apis/docx/v1/documents/:doc_id/blocks/:block_id/children`

### 3. Create GitHub issue

**Prerequisites:**
- `GITHUB_TOKEN` env var with repo scope
- Target repo in `owner/repo` format

**Steps:**
1. Write the issue body to a temp markdown file describing:
   - What languages were added
   - Which scenarios were translated
   - Link to the Feishu Wiki page
   - Any notes on translation quality
2. Run `scripts/create-github-issue.sh <owner/repo> "<title>" <body-file>`
3. The script returns the issue URL

### 4. Adding more languages later

1. Run `scripts/add_language.py <file> <lang-code> <lang-name> <flag>` to insert structural placeholders
2. Fill in translations for each `_TRANSLATE_` marker
3. Re-run sync and issue creation steps

## Language codes reference

| Language | Code | Flag |
|----------|------|------|
| Chinese  | zh   | 🇨🇳 |
| English  | en   | 🇬🇧 |
| French   | fr   | 🇫🇷 |
| Korean   | ko   | 🇰🇷 |
| Japanese | ja   | 🇯🇵 |
| German   | de   | 🇩🇪 |
| Spanish  | es   | 🇪🇸 |
| Portuguese | pt | 🇵🇹 |
| Russian  | ru   | 🇷🇺 |
| Arabic   | ar   | 🇸🇦 |

## Environment variables checklist

- [ ] `FEISHU_APP_ID`
- [ ] `FEISHU_APP_SECRET`
- [ ] `FEISHU_WIKI_SPACE_ID` (optional default)
- [ ] `FEISHU_PARENT_NODE_TOKEN` (optional default)
- [ ] `GITHUB_TOKEN`
- [ ] `GITHUB_REPO` (optional default, format: owner/repo)
