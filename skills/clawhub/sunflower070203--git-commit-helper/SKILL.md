---
name: git-commit-helper
description: Analyze the current git changes, generate a Conventional Commits message, confirm with the user, then commit. 当用户说「帮我提交代码」「提交一下」「commit this」「commit my changes」时使用。Use when asked to commit code after changes are made.
---

# git-commit-helper

## When to use

Use when the user asks to commit code: "帮我提交代码", "提交一下", "commit this", "commit my changes", "commit".

## Prerequisites

- `git` and `powershell` available on PATH.
- The helper script `scripts/git-commit-helper.ps1` lives in this skill directory. Resolve paths relative to this directory.

## Hard rules

1. NEVER run `git commit` before the user explicitly confirms BOTH the scope and the message.
2. NEVER commit files outside the scope the user confirmed.
3. If the helper script reports an error, show the raw error to the user. Do not guess, retry, or work around it.
4. If the repository documents its own commit conventions (CONTRIBUTING.md, commitlint config, etc.), follow those over the defaults below.

## Workflow

### Step 1: Analyze

Run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "scripts/git-commit-helper.ps1" analyze
```

The output is a fixed-format block, for example:

```text
[git-commit-helper] branch: main
[git-commit-helper] initial-commit: no
[git-commit-helper] merge-in-progress: no
[git-commit-helper] staged:
[git-commit-helper]   A  src/new.py  (+12/-0)
[git-commit-helper] unstaged:
[git-commit-helper]    M src/foo.py  (+5/-2)
[git-commit-helper] untracked:
[git-commit-helper]   ?? docs/note.md
[git-commit-helper] total: 3 files, +17/-2
```

- If `total: 0 files` appears: tell the user there is nothing to commit and STOP.
- If `merge-in-progress: yes` appears: ask the user how to proceed before continuing.

### Step 2: Show scope

Show the user the full output block verbatim. Do not summarize.

Ask: commit everything, exclude files, or cancel.

- Everything: continue with all files.
- Exclude: note the exact paths the user wants excluded, continue with the remaining files only.
- Cancel: stop.

### Step 3: Generate the message

Follow this decision tree.

#### Type (pick exactly one)

| Type | Use when |
| --- | --- |
| feat | New user-facing feature |
| fix | Bug fix |
| refactor | Behavior-preserving code change |
| docs | Documentation only |
| style | Formatting/whitespace, no behavior change |
| test | Adding or fixing tests |
| perf | Performance improvement |
| build | Build system or dependency changes |
| ci | CI configuration changes |
| chore | Maintenance, tooling, or misc |

If changes span multiple types, pick the dominant one. If still tied, prefer in this order: feat, fix, refactor, docs, chore.

#### Scope

- If the repository documents a scope convention, follow it.
- Otherwise use the top-level directory of the main changed files, e.g. `feat(api): ...`.
- If no single directory dominates, omit the scope.

#### Subject

- Imperative mood, e.g. "add login", not "added login".
- 50 characters or fewer.
- Lowercase first letter, no trailing period.

#### Body

- Write a body ONLY when there is a "why": motivation, trade-offs, impact.
- Never list changed files one by one.
- Use blank line between subject and body.

#### Breaking change

If the change is breaking, add `!` after the type/scope in the subject (e.g. `feat(api)!: ...`) and include a `BREAKING CHANGE: <description>` line in the body footer.

### Step 4: Write the message to a file

Compose the full message in a variable, normalize line endings to LF, then write UTF-8 WITHOUT BOM:

```powershell
$msg = $msg -replace "`r`n", "`n"
[IO.File]::WriteAllText("$env:TEMP\gch-msg.txt", $msg, (New-Object System.Text.UTF8Encoding($false)))
```

### Step 5: Confirm with the user

Show the user the confirmed scope summary AND the full message. Wait for explicit approval. If the user edits the message, update the file and show it again.

### Step 6: Commit

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "scripts/git-commit-helper.ps1" commit -MessageFile "$env:TEMP\gch-msg.txt"
```

If the user excluded files, pass them explicitly:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "scripts/git-commit-helper.ps1" commit -MessageFile "$env:TEMP\gch-msg.txt" -Paths "path/to/a.txt" "path/to/b.txt"
```

Omit `-Paths` when committing everything.

### Step 7: Verify

Run `git log -1 --stat` and report the result to the user.
