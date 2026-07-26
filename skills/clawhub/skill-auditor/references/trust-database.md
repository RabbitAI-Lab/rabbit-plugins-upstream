# Trust Database (offline, community-maintained)

> This file is an offline record of skills with known security posture.
> The audit script reads `## Project-specific trusted domains` if present.

## Known-malicious skills

> Skills confirmed malicious by community review. Audit script may hard-fail on these.

| Slug | Author | Pattern | Reported | Source |
|---|---|---|---|---|
| _(none yet)_ | | | | |

To report a malicious skill, open a PR adding a row. Include:
- slug + author handle
- pattern observed (with file:line)
- date discovered
- link to disclosure / write-up

## Known-benign skills

> Skills that have been manually reviewed and are considered safe. They may still trigger some rules (e.g. legitimate use of `~/.aws/credentials` for an AWS skill) — listed here to suppress false positives.

| Slug | Author | Notes | Reviewed |
|---|---|---|---|
| `skill-vetter` | spclaudehome | Manual checklist, no code execution | 2026-07-04 |
| `self-improving-agent` | pskoett | Logs learnings to local files, no network exfil | 2026-07-04 |
| `ontology` | oswalpalash | Local graph storage, no network | 2026-07-04 |

## Project-specific trusted domains

> Domains the audit script should treat as allowlisted, in addition to the default list in `vet.py DEFAULT_ALLOWLIST`.

```
# Add one domain per line. Lines starting with # are comments.
# Example:
# internal.corp.example.com
# api.internal.tooling.dev
```

## How to contribute

1. **Malicious skill**: open a PR with the table row + a write-up link. Maintainers will review and merge.
2. **Benign skill (false positive suppression)**: open a PR after manually auditing the skill. Include the audit report (run `python3 scripts/vet.py <path> --json`) as evidence.
3. **Trusted domains**: add to the section above, with a comment explaining why the domain is trusted.

## Disclaimer

This database is community-maintained and may be incomplete or outdated. Always run `skill-auditor` and apply human judgment (Step 5 of the protocol) regardless of database entries.
