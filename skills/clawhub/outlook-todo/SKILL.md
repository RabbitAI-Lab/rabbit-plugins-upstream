---
name: outlook-todo
license: MIT
description: "Read and write Microsoft To Do via shared Outlook Graph auth: enumerate task lists, read/filter tasks, and create, update, complete, or delete tasks (writes require --apply plus a typed-YES prompt or an explicit --yes flag)."
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

Use this skill to read and write the signed-in user's Microsoft To Do / Outlook.com task
lists and tasks through Microsoft Graph.

This is a separate skill from `outlook-calendar`, but it shares the same auth/config under:

```text
~/.outlook-graph/config.json
~/.outlook-graph/tokens.json
```

## Current permission policy

The shared family consent requests exactly **five** delegated scopes (one login covers
calendar, To Do, and contacts — full rationale in `outlook-calendar` SKILL.md):

- `offline_access`
- `https://graph.microsoft.com/User.Read`
- `https://graph.microsoft.com/Calendars.ReadWrite` (`outlook-calendar` skill)
- `https://graph.microsoft.com/Tasks.ReadWrite` (this skill)
- `https://graph.microsoft.com/Contacts.ReadWrite` (`outlook-contacts` skill)

Mail, files, notes, directory, and Teams scopes are never requested.

Read operations may be automatic. Creating, updating, completing, or deleting tasks must require explicit user confirmation.
Non-interactive (agent) use must pass the explicit `--yes` flag — there is no
environment-variable bypass.

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

## Write tasks (explicit confirmation required)

`todo-write.sh` supports **create / update / complete / delete**. Every write defaults to
**dry-run** (prints the JSON payload; may perform read-only Graph lookups such as
resolving the default list or fetching the task to display — never writes).
Dry-run is not an offline mode. Pass `--apply` to execute.
Interactive runs are prompted to type `YES`; non-interactive runs must pass `--yes`.

```bash
# Create (dry-run preview, then real call)
~/.openclaw/skills/outlook-todo/scripts/todo-write.sh create --title "Buy milk" --due 2026-06-24
~/.openclaw/skills/outlook-todo/scripts/todo-write.sh create --title "Buy milk" --due 2026-06-24 --apply

# Update fields
~/.openclaw/skills/outlook-todo/scripts/todo-write.sh update --task-id '<ID>' --title "New title" --apply --yes

# Mark completed
~/.openclaw/skills/outlook-todo/scripts/todo-write.sh complete --task-id '<ID>' --apply --yes

# Delete (shows the task first)
~/.openclaw/skills/outlook-todo/scripts/todo-write.sh delete --task-id '<ID>' --apply --yes
```
