# Feishu/Lark Permission Configuration — stock-alert

This skill can publish or archive its alert reports to Feishu/Lark documents
(e.g. a "Daily Stock Alerts" doc or a team folder). The following permission
configuration follows the project's **Feishu Permission Management** standard
(`skills/feishu-perm`). Apply it to any doc/folder this skill writes to.

## 1. Permission levels (standard)

| Level       | Who                                  | Rationale                                   |
|-------------|--------------------------------------|---------------------------------------------|
| Can manage  | Skill owner / finance ops lead       | Manage sharing, rotate access               |
| Can edit    | The Feishu app bot (alert writer)    | Append daily alerts to the report doc       |
| Can view    | Finance team / alert subscribers     | Read alerts; comment only                   |
| No access   | Everyone else (default)              | Alerts may contain a curated watchlist      |

## 2. Grant the bot write access (group-based, preferred)

Per the standard, prefer group-based sharing over individual grants:

1. Create a dedicated group, e.g. **"Stock Alert Bot Access"**.
2. Add the Feishu app bot to the group.
3. Share the target report doc/folder with the group at **Can edit**.
4. Test: ask the bot to append a line to the doc.

## 3. External sharing

- **Disabled by default.** Stock alert reports stay internal.
- Only enable "Allow content to be shared externally" if a specific external
  stakeholder needs it, and then prefer adding them as a named **Can view**
  collaborator over an open "Internet with link" share.

## 4. Folder inheritance

- Place the report doc inside a **"Finance Alerts"** team folder.
- Set permissions **once at the folder level** and let docs inherit, to keep
  management simple as new daily/weekly reports are added.

## 5. Audit checklist (run periodically)

- [ ] Bot retains exactly **Can edit** (not manage).
- [ ] No stale individual collaborators; subscribers are **Can view** only.
- [ ] External sharing is **off** unless explicitly required and documented.
- [ ] Folder inheritance is intact (no per-doc permission drift).

## 6. WhatsApp delivery constraint (related)

Delivery access is governed separately by `config/wacli_config.yaml`:
- `finance-alerts@g.us` → `full` (may receive sends)
- all other `*@g.us` → `read`
- default → `none`

Keep the WhatsApp recipient allowlist as tight as the Feishu viewer list.
