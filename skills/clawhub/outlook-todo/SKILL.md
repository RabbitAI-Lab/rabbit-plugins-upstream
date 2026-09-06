---
name: outlook-todo
license: MIT
description: "Read Microsoft To Do task lists and tasks via shared Outlook Graph auth."
metadata:
  openclaw:
    emoji: "✅"
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

# Outlook To Do

Use this skill to read the signed-in user's Microsoft To Do / Outlook.com task lists through Microsoft Graph.

This is a separate skill from `outlook-calendar`, but it shares the same auth/config under:

```text
~/.outlook-graph/config.json
~/.outlook-graph/tokens.json
```

## Current permission policy

To Do read/write permission is authorized, but writes require explicit confirmation:

- `offline_access`
- `https://graph.microsoft.com/User.Read`
- `https://graph.microsoft.com/Calendars.ReadWrite` (for the calendar skill)
- `https://graph.microsoft.com/Tasks.ReadWrite`

No mail, files, contacts, or directory scopes.

Read operations may be automatic. Creating, updating, completing, or deleting tasks must require explicit user confirmation.

## First-time / upgrade setup

This skill uses the same public client app as `outlook-calendar`. For personal Outlook.com accounts, Azure Portal "API permissions" preconfiguration is usually optional because Microsoft delegated OAuth supports dynamic consent: the setup script explicitly requests `Tasks.ReadWrite`, and the user consents during device-code login.

Re-run shared setup after the scope list changes:

```bash
cd ~/.openclaw/skills/outlook-calendar
./scripts/setup-device-code.sh --client-id <YOUR_CLIENT_ID> --tenant-id common --force
```

For work/school tenants that disable user consent, an administrator may still need to preconfigure Microsoft Graph delegated permission `Tasks.ReadWrite` and grant admin consent.

Azure app registration steps: see `outlook-calendar` SKILL.md → **First-time setup** (same shared app covers this skill).

## Read task lists

```bash
~/.openclaw/skills/outlook-todo/scripts/todo-read.sh lists --format summary
```

## Read tasks

```bash
# Default task list if Microsoft marks one as wellKnownListName=defaultList
~/.openclaw/skills/outlook-todo/scripts/todo-read.sh tasks --format summary

# Specific list by name or id
~/.openclaw/skills/outlook-todo/scripts/todo-read.sh tasks --list-name "Tasks" --format summary
~/.openclaw/skills/outlook-todo/scripts/todo-read.sh tasks --list-id '<LIST_ID>' --format json

# Include completed tasks
~/.openclaw/skills/outlook-todo/scripts/todo-read.sh tasks --status all --format summary
```

Formats: `summary`, `json`, `ids`, `raw`.
