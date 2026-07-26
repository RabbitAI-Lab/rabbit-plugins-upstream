---
name: yuque-doc-push
description: Use this skill when a user wants to create, update, delete, or list documents in a Yuque knowledge base, or manage Yuque repository table of contents. Use it for pushing local content to Yuque, syncing document changes, or inspecting what exists in a Yuque repo. Do not use it when the user wants general knowledge-base management unrelated to Yuque, or when they need to manage Yuque team members, permissions, or repository settings.
---

# Yuque Document Push

Manage documents in a Yuque knowledge base through the OpenAPI. Owns create, read, update, delete of documents and TOC inspection.

## What this skill owns

- CRUD operations on documents within a single Yuque knowledge base.
- Automatic TOC insertion after document creation.
- Reading and displaying the knowledge base table of contents.

This skill does NOT own:
- Yuque repository or team management (create/delete repos, manage members).
- Cross-repo operations or batch migration.
- Yuque authentication setup (the user must provide a valid token).

## Prerequisites

1. Python 3.8+ with `requests` and `python-dotenv` installed.
2. A `.env` file in the project root (created via the setup flow below).

## First-time setup

If the user has not configured this skill yet (no `.env` file, or `list` returns a config error), follow this flow:

1. **Ask for the knowledge base URL.** Tell the user:
   > Please paste your Yuque knowledge base URL, for example: `https://xxx.yuque.com/group/book`
   >
   > You can find it by opening your knowledge base in the browser and copying the address bar URL.

2. **Ask for the API token.** Tell the user:
   > Please paste your Yuque API token.
   >
   > To create one: open Yuque -> click your avatar (top right) -> "Account Settings" -> "Tokens" -> "Create new token". Grant it read/write access to your target knowledge base.
   >
   > Token page: https://www.yuque.com/settings/tokens

3. **Run the setup command.** The script auto-parses the URL and validates the connection:
   ```bash
   python scripts/yuque_cli.py setup --url "<user_url>" --token "<user_token>"
   ```
   - On success: `.env` is written, connection is verified, `.gitignore` is checked.
   - On failure: the script prints the exact error (bad token, wrong URL, etc.). Fix and retry.
   - Use `--force` to overwrite an existing `.env`.

4. **Confirm** by running `python scripts/yuque_cli.py list`.

### Security rules

- **NEVER** echo, print, or include the token in your text responses to the user. Pass it only as a CLI argument to the setup script.
- **NEVER** commit `.env` to git. The setup script checks `.gitignore` and warns if `.env` is not excluded.
- **NEVER** hardcode the token in any file other than `.env`.
- If the user pastes a token in chat, immediately use it in the setup command and do not repeat it back.

## Default path

1. **Validate prerequisites.** Run `python scripts/yuque_cli.py list` to confirm token and repo are valid.
2. **Identify the action.** Determine whether the user wants to create, update, delete, or inspect.
3. **Execute the action** using `scripts/yuque_cli.py` with the matching subcommand.
4. **Verify the result.** Use `list`, `get`, or `toc` to confirm the operation succeeded.
5. **Report** the outcome: doc ID, title, slug, and any errors.

### Command reference

| Action | Command | Key flags |
|--------|---------|-----------|
| Setup | `python scripts/yuque_cli.py setup --url URL --token TOKEN` | `--force`, `--env-path` |
| List | `python scripts/yuque_cli.py list` | `--offset`, `--limit` |
| Get | `python scripts/yuque_cli.py get <id_or_slug>` | |
| Create | `python scripts/yuque_cli.py create -t "Title" -b "Body"` | `-f FILE`, `--no-toc`, `--format`, `--slug` |
| Update | `python scripts/yuque_cli.py update <id_or_slug> -t "T"` | `-b`, `-f FILE`, `--format` |
| Delete | `python scripts/yuque_cli.py delete <id_or_slug> --confirm` | `--confirm` required (not optional) |
| TOC | `python scripts/yuque_cli.py toc` | |
| Sync | `python scripts/yuque_cli.py sync` | `--check`, `--root`, `--layout`, `--on-missing` |
| Pull | `python scripts/yuque_cli.py pull --slug <slug>` | `--all`, `--overwrite`, `--root`, `--layout` |
| Status | `python scripts/yuque_cli.py status` | `--root`, `--layout` |

Global flags available on all commands: `--json` (machine-readable output), `--dry-run` (preview without executing).

> **Dry-run mode always outputs JSON** regardless of the `--json` flag. Use it to inspect the payload before committing.

## Sync workflow

Use `sync` for "push only what actually changed" instead of blind `update`. The script maintains `.yuque-sync.json` (auto-added to `.gitignore`) tracking each doc's local content hash and remote `latest_version_id`, so unchanged docs are skipped without any GET-detail call.

### First-time init

When the user runs `sync`/`pull`/`status` and no state file exists, the script auto-detects the local layout from `.md` files under `--root` (default cwd):

- **flat** — all `.md` files at top level. Slug = file stem.
- **nested** — `.md` files under subdirectories. Slug = file stem (subdirs are organizational only; they do not create TOC groups).
- **frontmatter** — every file has `--- slug: xxx ---` frontmatter at the top. Slug = frontmatter value.
- **empty** — no `.md` files yet; suggest `pull --all` to seed locally.

If layouts are mixed or partially-frontmatter, the script errors and asks the user to pass `--layout flat|nested|frontmatter` or normalize the directory.

### Frontmatter fields (frontmatter layout)

In `frontmatter` layout, each `.md` file begins with a YAML block. Supported fields:

- `slug` (required) — the Yuque document slug (URL identifier). Usually English kebab-case, e.g. `create-draft-task`.
- `title` (optional) — the document title pushed to Yuque. Useful when the file name or H1 should not be used as the title.

Example:
```markdown
---
slug: create-draft-task
title: 创建起草任务
---

# 创建起草任务
正文内容。
```

The YAML frontmatter is **stripped before pushing** to Yuque — it never appears in the rendered document body.

### Title extraction priority

When `sync` pushes a document, the title sent to Yuque is resolved in this order:

1. Frontmatter `title` field (if present)
2. First H1 heading (`# Heading`) in the body
3. File name stem (without `.md` extension)
4. Slug (last resort)

When the title falls back to the file name or slug (steps 3–4), `sync --check` / `status` lists these docs under a **"Title fallback"** section so you know to add an H1 or frontmatter `title`.

Use `sync --force-title` to always use the file name stem as the title, ignoring H1 and frontmatter `title`. This is useful when upstream-generated titles are unreliable.

### Automatic body transformations on push

During `sync` push, the following transformations are applied to the body before sending it to Yuque:

1. **Frontmatter stripping** — YAML frontmatter is removed (frontmatter layout only).
2. **Inter-document link rewriting** — `[text](file.md)` links are converted to `[text](slug)` using the local slug map, so they resolve correctly on Yuque. External URLs (`http://...`), anchors (`#section`), and non-`.md` links are left untouched. Unresolved links are kept as-is and reported as warnings.
3. **Bold format fix** — `**标签：**值` (bold-close marker directly followed by a non-space character) is rewritten to `**标签：** 值`, because Yuque's renderer requires a trailing space to recognize the bold-close marker. Already-correct `**标签：** 值` is not affected.

On `pull`, the reverse transformation is applied: slug links are converted back to local file-name links when a matching local file is known.

### Sync flow per run

1. Lists all remote docs once (with `optional_properties=latest_version_id`) — no per-doc GET.
2. For each local file, compares normalized SHA-256 of the body and the remote `latest_version_id` to the values stored in `.yuque-sync.json`.
3. Pushes:
   - `create` for local files with no remote counterpart (auto-adds to TOC).
   - `update` for local files whose body changed and remote did not.
   - **Skips** unchanged, conflicts (both sides changed, or remote moved), and non-markdown remotes (with a warning).
4. After push, if any tracked doc has gone missing locally, **stops with exit code 2** and prints a confirmation block (see below). Never auto-deletes remote docs.

### Confirmation handling (exit code 2)

`sync` exits **2** when local files that were previously synced are now missing. This is **not an error** — it means the script needs an explicit choice from the user. The stdout block describes three options, each with the exact flag to re-run with:

- `--on-missing delete` — delete on Yuque too
- `--on-missing pull` — restore locally from Yuque
- `--on-missing forget` — keep on Yuque, drop from local state

When you see exit code 2, **show the printed block to the user** (translated to their query language; see Language section), then re-invoke `sync --on-missing <choice>` once they pick.

### Conflicts

If a doc was changed both locally and remotely (or remote moved while local stayed), `sync` lists it under "Conflicts" and skips it. Resolve manually:

- `pull --slug <slug> --overwrite` — accept remote version locally.
- `update <slug> -f path/to/file.md` — overwrite remote with local version.

After resolution, the next `sync` run will reconcile the state file.

## Language

The CLI emits English in fixed-format blocks for stability. **When relaying CLI output to the user — especially the `sync` confirmation block, status sections, and error messages — translate the human-readable text into the user's query language.** Keep the following literal and untranslated:

- CLI flag names and values (e.g. `--on-missing delete`, `--layout flat`).
- Doc slugs, IDs, file paths.
- Section keys in JSON output.

## Failure handling

- **Missing .env or token**: Stop. Run the first-time setup flow above. Do NOT ask the user to manually edit `.env`.
- **Invalid YUQUE_REPO format**: Stop. Re-run `setup` with the correct URL.
- **.gitignore missing .env entry**: Warn the user immediately. Do not proceed with any API calls until `.env` is protected.
- **401 Unauthorized**: Stop. Token is invalid or expired — ask the user to regenerate it.
- **404 Not Found**: Stop. The repo path or doc ID/slug is wrong — ask the user to verify.
- **429 Rate Limited**: Wait briefly and retry once. If it fails again, stop and inform the user.
- **No fields provided on update**: Stop. At least one of `--title`, `--body`, `--body-file`, `--slug`, `--format`, `--public` must be given.
- **Delete without --confirm**: The script refuses. This is intentional — always pass `--confirm`.
- **`sync` exit code 2**: Not an error. Confirmation required for missing-local files. Show the block to the user, get their choice, re-run with `--on-missing <choice>`.
- **Layout ambiguous on first sync**: Show the script's suggestion to the user; do NOT pick `--layout` for them — ask which structure they intend.

Do NOT guess doc IDs or slugs. If unknown, run `list`, `toc`, or `status` first to find the target.

## Resource navigation

- `scripts/yuque_cli.py` — the CLI tool. Run it; do not read it unless debugging.
- `scripts/yuque_cli.py --help` and `scripts/yuque_cli.py <cmd> --help` for full flag details.
- The project root `.env` file holds credentials (never commit it).

## High-value pitfalls

1. **Creating a document does NOT auto-add it to the TOC.** The script handles this by default via `append_doc_to_toc`. Use `--no-toc` only if you explicitly want an unlisted document.
2. **The `id` parameter in get/update/delete can be either an integer doc ID or a string slug.** Both work, but slugs are more readable.
3. **Body content with shell-special characters**: Use `--body-file` instead of `--body` for any non-trivial content to avoid shell quoting issues.
4. **The Yuque Lake format is proprietary.** Always use `--format markdown` (the default) unless the user specifically needs Lake format.
5. **TOC insertion always appends to the repo root as a child node.** There is no way to specify a parent node or insert at a specific position via this skill. If the user needs custom TOC structure, they must reorder it manually in the Yuque UI.
6. **`sync` ignores remote drafts (`body_draft`).** Change detection is based on `latest_version_id` (the last published version). If a teammate is editing in the Yuque web editor without publishing, that draft will be overwritten by `sync update`. If you suspect this, use `pull --slug <slug> --overwrite` to inspect remote first.
7. **Never auto-delete remote docs.** `sync` will only delete remotely when the user explicitly passes `--on-missing delete` after seeing the confirmation block. Do not pass `delete` on the user's behalf without an unambiguous yes.
