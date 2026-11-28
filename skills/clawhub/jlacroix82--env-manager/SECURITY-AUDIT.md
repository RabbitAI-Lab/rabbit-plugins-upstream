# Risk model — env-manager

## Scope

The skill has two operations:

1. **Write starter files** to a project directory using `fs.writeFileSync` and `fs.mkdirSync`. This happens unconditionally on every call to `setupEnvironment`.
2. **Return a list of toolchain commands** as structured objects. The agent (not the skill) executes them.

The skill does not invoke a shell, run binaries, or start any external process. There is no code path that launches a subprocess.

## Input validation

Both `--setup` arguments are validated **before any path is constructed and before any
file is written**. Rejected input leaves the filesystem untouched.

- `type` must be one of `python`, `node`, `docker`, `go`, `rust` (`INVALID_TYPE` otherwise).
  This is a path control, not only a template selector: when `name` is omitted, the
  environment directory is named `<type>-env-<timestamp>`, so the type reaches
  `path.join`.
- `name` must match `^[a-z0-9_.-]+$`, be 1-64 characters, and contain no
  parent-directory references (`INVALID_NAME` otherwise).

Independently of the above, every path is re-resolved and checked for workspace
containment immediately before each `mkdir`/`write` (`PATH_ESCAPE` otherwise). The
two layers are deliberately redundant: input validation can be bypassed by a caller
using the exported functions directly, containment cannot.

## Trust boundaries

- **File writes** are limited to a project directory inside the project workspace (repo root) — `<workspace>/environments/<name>/` — and a state directory (`<workspace>/memory/environments/`). An optional `ENV_MANAGER_WORKSPACE` env var can relocate the workspace, but only to a descendant of the repo root; paths outside the repo are rejected.
- **No runtime path redirection via CLI.** The skill does not read or accept `ENV_DIR` and does not support a `--dir` flag. The only path override is the confined `ENV_MANAGER_WORKSPACE` env var described above.
- **No network calls.** The skill does not perform HTTP, fetch, or DNS.
- **No environment-variable consumption beyond `PATH`** for the binary allowlist (which only collects resolved paths, never executes them).

## What the calling agent should know

- Every call to `setupEnvironment` writes files. There is no preview step.
- The skill cannot be used to run a command. It returns commands.
- `commands[]` entries with `status === "ready"` are validated against a built-in allowlist of well-known toolchain binaries. The agent should still inspect them before running.
- `commands[]` entries with `status === "blocked"` were rejected by the allowlist. The agent should not run them.
- `commands[]` entries with `status === "not_found"` reference binaries not on `PATH`. The agent should not run them until the binary is installed.

## Audit history

**v3.0.9 — path confinement (fixes the v3.0.8 ClawHub audit finding).** In v3.0.8 the
`type` argument to `--setup` / `setupEnvironment()` was never validated. When no `name`
was supplied, the environment directory name was built as `` `${type}-env-${timestamp}` ``
and passed to `path.join()`, so a type containing path separators escaped the workspace
— e.g. `--setup '../../../../evil'` created a directory four levels above the repo root.
The directory was created before the downstream name check threw, so the write happened
even though the call ended in an uncaught exception. v3.0.9 validates `type` against a
fixed allowlist before any path is built, and adds an independent containment assertion
in front of every `mkdir`/`write`. The same release fixes a `ReferenceError` that made
`--commands` crash, and makes invalid `--setup` input exit non-zero instead of throwing.

Earlier versions of the skill included a shell-execution layer with allowlists, dry-run, and an `--audit` command. That layer was removed because the LLM-based security scanner cannot distinguish safe argv-based execution from unsafe string-based execution, and reviews kept flagging the skill. The current code is a pure file scaffolder with command generation.

## Reporting issues

If you find a security issue, please open a GitHub issue or contact the maintainer.
