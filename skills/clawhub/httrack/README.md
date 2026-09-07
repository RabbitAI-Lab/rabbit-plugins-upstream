# 🕸️ httrack — v2.0.1

Offline website mirroring with HTTrack — snapshot a page (with its assets) or
mirror a bounded site to disk, with polite defaults and machine-readable
JSON reports. Full guide: `SKILL.md`. Recipes: `docs/recipes.md`.

## Requirements

- `httrack` binary (Debian/Ubuntu: `sudo apt install httrack`; macOS:
  `brew install httrack`) — verified at runtime by `mirror.py doctor`.
- Python 3.8+ (stdlib only) for the wrapper.
- Outbound http/https to the sites you mirror.

## Permissions, security & privacy

- **Reads:** public/unauthenticated content served by the URLs you supply.
- **Writes:** only inside the output directory you pass with `-o`.
- **Network:** outbound http/https only to the supplied URLs. No relays, no
  third parties, no telemetry. No API keys or secrets are used or stored.
- **Shell:** never — all subprocess calls use argument lists (`shell=False`
  equivalent); scan-rule patterns are validated; URL schemes are restricted to
  http/https; userinfo/localhost/private-IP-literal URLs and `..` in
  the output path are refused (override with `--allow-private`).
- **Robots:** default `-s2` = always obey robots.txt; `--robots` 0/1 exist for
  authorized archives of your own sites only.

## Known risks & mitigations

Mirrored content may be copyrighted and subject to site terms — mirror only
what you are authorized to archive, and do not redistribute. Mirrors can
contain scripts, cookies, or tracking pixels — review files before opening.
Aggressive crawls burden servers: defaults (2 sockets, bounded depth,
same-address travel, robots honored) keep that bounded; raise limits only
deliberately.

## Verify it

`bash scripts/selftest.sh` — offline suite using a stub httrack: recipe argv
composition, JSON contracts, exit codes, policy rejections, version sync,
regression pins against the v1.0.2 hallucinated flags. No network, no sudo.
