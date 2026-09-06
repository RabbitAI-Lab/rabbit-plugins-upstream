---
name: outlook-contacts
license: MIT
description: |
  Read and write the signed-in user's Microsoft 365 / Outlook.com personal contacts via Microsoft Graph.
  No mail, no files, no directory access.
  Use when the user wants to list/search Outlook.com contacts, find phone numbers, or look up email addresses.
  Trigger keywords: "outlook contacts", "ms contacts", "graph contacts", "我的联系人", "查联系人", "outlook 联系人".
metadata:
  openclaw:
    emoji: "👤"
    requires:
      bins: ["bash", "jq", "curl", "python3"]
    network:
      allow:
        - "https://login.microsoftonline.com"
        - "https://graph.microsoft.com"
    files:
      read:
        - "~/.outlook-graph/"
---

# Outlook Contacts (Microsoft Graph, read & write)

A **contacts read-and-write** Microsoft Graph skill. Reads and writes the signed-in user's personal contacts
through `/me/contacts`. **Does not access mail/files/directory.**

All write operations (create, update, delete) default to **dry-run**; you must pass `--apply` to execute.

## ⚠️ Shared auth with outlook-calendar & outlook-todo

This skill reuses the same config and tokens under `~/.outlook-graph/`, but it needs the
**`Contacts.ReadWrite`** scope (in addition to the existing scopes from the calendar/todo skills).

If you already have outlook-calendar set up, you'll need to re-authenticate once to add
the `Contacts.ReadWrite` permission. Run the combined setup:

```bash
cd ~/.openclaw/skills/outlook-calendar
./scripts/setup-device-code.sh --client-id <YOUR_CLIENT_ID> --tenant-id common --force
```

> ⚠️ This will ask you to re-consent with an extended scope that includes `Contacts.ReadWrite`.

For personal Outlook.com accounts, Azure Portal preconfiguration is usually unnecessary —
Microsoft supports dynamic consent, and the setup script will request the new scope at login.

## Scopes required

| Scope | Why |
|---|---|
| `offline_access` | refresh_token for headless operation |
| `https://graph.microsoft.com/User.Read` | display signed-in account UPN |
| `https://graph.microsoft.com/Contacts.ReadWrite` | read and write personal contacts |

The existing setup-device-code.sh in outlook-calendar also includes `Calendars.ReadWrite`
and `Tasks.ReadWrite` for the calendar/todo skills. They coexist in the same token.

## Reading contacts

```bash
# List all contacts (paginated, max 200 per page)
./scripts/contacts-read.sh list --format summary

# Search contacts by name, email, or company
./scripts/contacts-read.sh search "jane" --format summary

# Filter by specific field
./scripts/contacts-read.sh list --filter "contains(displayName,'Zhang')" --format json

# Limit results
./scripts/contacts-read.sh list --limit 20 --format summary

# Raw JSON output
./scripts/contacts-read.sh list --format raw
```

`--format` options:

- `summary` (default) — compact table: name, email, phone, company, title
- `json` — pretty-printed full Graph JSON
- `simple` — one line per contact: "name <email> 📞phone"
- `raw` — single-line JSON array

### Format examples

**summary** (default):
```
NAME                 EMAIL                        PHONE            COMPANY         TITLE
----------------------------------------------------------------------------------------------------

Zhang San            zhang@example.com            13812345678      ABC Corp        Manager
Li Si                li@example.com               13987654321      -               -

Total: 2 contacts
```

**simple** — one line per contact with optional phone icon:
```
Zhang San <zhang@example.com> 📞13812345678
Li Si <li@example.com>
```

### Search syntax

The `search` subcommand uses Microsoft Graph's `$search` query parameter on the
`displayName` and `emailAddresses` fields:

```bash
./scripts/contacts-read.sh search "Wang" --format simple
./scripts/contacts-read.sh search "gmail.com" --format summary
```

### Filtering

The `--filter` option passes an OData `$filter` expression directly:

```bash
./scripts/contacts-read.sh list --filter "jobTitle eq 'Professor'" --format summary
./scripts/contacts-read.sh list --filter "startswith(givenName,'X')" --format json
```

## Writing contacts

**⚠️ Safety: every write defaults to dry-run. Pass `--apply` to execute.**

```bash
# Get a single contact (read-only, no --apply needed)
./scripts/contacts-write.sh get --contact-id "AAMk..."

# Update a contact (dry-run by default; see payload before applying)
./scripts/contacts-write.sh update --contact-id "AAMk..." \
  --email "new@example.com" --phone "13812345678"

# Actually update (after confirming dry-run output looks correct)
./scripts/contacts-write.sh update --contact-id "AAMk..." \
  --email "new@example.com" --phone "13812345678" --apply

# Create a new contact
./scripts/contacts-write.sh create --display-name "Zhang San" \
  --email "zhang@example.com" --phone "13912345678" --apply

# Delete a contact (always shows the contact first, then asks for YES confirmation)
./scripts/contacts-write.sh delete --contact-id "AAMk..." --apply
```

### Update fields available

- `--display-name` — full display name
- `--given-name` — first name
- `--surname` — last name
- `--email` — primary email (replaces existing email array)
- `--phone` — mobile phone number
- `--company` — company name
- `--job-title` — job title
- `--notes` — personal notes

## Files in this skill

| Path | Purpose |
|---|---|
| `SKILL.md` | this file |
| `scripts/contacts-read.sh` | `list` / `search` contacts via `/me/contacts` |
| `scripts/contacts-write.sh` | `get` / `update` / `create` / `delete` contacts |

## Troubleshooting

- **`token scope does not include Contacts.ReadWrite`** — you need to re-run the outlook-calendar
  setup script with `--force` to re-authenticate and get the extended scope.
- **Empty results** — check that contacts exist in Outlook.com under "People".
- **`401 Unauthorized`** — run `scripts/token.sh refresh` in the outlook-calendar skill.
