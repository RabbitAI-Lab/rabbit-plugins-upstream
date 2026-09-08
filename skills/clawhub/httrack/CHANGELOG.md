# Changelog — httrack

## v2.0.1 (2026-09-06) — registry-hardening

Version-sync test no longer requires `skill-card.md` (ClawHub strips publisher
metadata from install bundles); check is presence-tolerant. No behavior change.


## v2.0.0 (2026-09-06) — agent-grade rewrite

Headline: the skill now executes safely and reports machine-verifiable results
instead of handing the model raw CLI folklore. New:

- `scripts/mirror.py` — `doctor | snapshot URL | mirror URL`, strict http/https
  allowlist, polite defaults (robots=always `-s2`, 2 sockets, same-address
  travel), `--allow/--deny` scan-rule witching done by the wrapper, `--resume`
  (`-i`), `--max-time` (`-E`), `--max-mb` (`-M`), `$HTTRACK_BIN` override.
- JSON contracts `httrack.doctor.v1` / `httrack.report.v1` (files/bytes/pages/
  exit/log_tail), exit-code map 0/2/3/4, documented in `manifest.json`.
- Real snapshot recipe (page + inline assets, no link following), grounded in
  HTTrack forum + SO consensus — the v1 `-r0` snapshot lost all assets.
- `docs/recipes.md`, `docs/evidence.md` (every emitted flag cited to the
  HTTrack manpage), offline `scripts/selftest.sh` (stub httrack — no net/sudo),
  version strings synced across SKILL.md/manifest/README/card, `.clawhubignore`
  (no bytecode leaks).

Hallucination fixes (evidence: docs/evidence.md):

- `-Y` is `--mirrorlinks`, NOT “update existing mirror” → replaced with `-i`.
- `-A "*.pdf,*.zip"` was not a valid filter → `--allow/--deny` (bare `+/-` rules).
- `--robots=1` meant “sometimes obey” → default `-s2` (always obey).
- `-%v` is display-filenames, not “verbose”.

## v1.0.2 (legacy)

Original three-file guide (SKILL.md + mirror.sh + README); recipes documented
but unverified; several flag rows misdescribed (see fixes above); frontmatter
version drifted from registry (1.0.0 vs 1.0.2); no tests, no machine output.
