# maybeai-sheet-cli-skill

Agent skill for the `mbs` CLI from `maybeai-sheet-cli`.

It covers workbook/worksheet/table operations, safe full worksheet data
refreshes that retain headers and formulas, worksheet styling, Base-backed
field style metadata, floating chart-like image objects, and worksheet-scoped
dashboard orchestration. It also documents the guarded one-way migration of an
existing Sheet-backed worksheet to Base with `mbs worksheet convert-to-base`.

For that migration, select one worksheet by `--gid` or `--worksheet-name`, run
`--dry-run` first, then execute with `--yes --verify`. Source Sheet-engine cell
content is scrubbed by default while styles are retained; use
`--keep-sheet-source` only when that content must remain.

This repository owns agent-facing assets:

- `SKILL.md` — routing, playbooks, core rules
- `references/` — topic docs and `cli-commands.md` command catalog
- `agents/` — agent metadata
- `artifacts/` — demo datasets and reusable example specs

CLI implementation lives separately:

- `../maybeai-sheet-cli`

Install the CLI: `pip install maybeai-sheet-cli`

To get a MaybeAI API token, register at [maybe.ai](https://www.maybe.ai/), then
open [My Plan](https://www.maybe.ai/user/my-plan) and copy a token from the
**API Token** section.

Set `MAYBEAI_API_TOKEN`, then run `mbs --help`:

```bash
export MAYBEAI_API_TOKEN="your-api-token"
mbs --help
```

## Sync after CLI release

After `../maybeai-sheet-cli` is published to PyPI, sync this skill's version
frontmatter from the released CLI metadata:

```bash
python scripts/sync_cli_release.py --cli-repo ../maybeai-sheet-cli
```

The hook verifies that the CLI repo version fields agree and that the same
version exists on PyPI before updating `SKILL.md`. Use `--skip-pypi-check` only
for local draft docs before a package release.
