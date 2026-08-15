# Rule library schema

Each platform file begins with YAML frontmatter followed by individual rule sections. Keep one platform per file.

## File metadata

```yaml
---
platform: example-platform
display_name: Example Platform
jurisdiction: global
official_policy_url: https://example.com/policy
last_checked: 2026-08-10
status: active
---
```

Required fields are `platform`, `display_name`, `jurisdiction`, `official_policy_url`, `last_checked`, and `status`. Use ISO `YYYY-MM-DD` dates. Allowed status values are `active`, `partial`, `stale`, and `archived`. An unknown URL must be written as `unknown`, not invented.

## Rule record

Use this exact heading and field pattern:

```markdown
## RULE-ID: Short title

- Authority: official
- Status: active
- Surfaces: speech, caption, image
- Risk default: high
- Source: https://example.com/policy
- Published or observed: 2026-08-01
- Verified: 2026-08-10
- Summary: Concise statement of the rule.
- Notes: Applicability, exceptions, conflicts, or interpretation limits.
```

Allowed authority values: `law`, `official`, `campaign`, `heuristic`, `unknown`.

Allowed rule status values: `active`, `superseded`, `disputed`, `stale`, `unknown`.

Allowed default risk values: `prohibited`, `high`, `medium`, `low`, `verify`.

Use a stable platform prefix in IDs, such as `DY-001`. Use a domain overlay when useful, such as `DY-MED-001` or `DY-MIN-001`. Do not reuse an ID after a rule is superseded. Link the replacement in `Notes`.

## Evidence rules

- Prefer first-party policy pages and primary legal sources.
- Record a user-supplied experiential rule as `heuristic`; do not convert frequency of anecdotes into official authority.
- Write `unknown` for missing provenance and mark the finding `待核实` during review.
- Use quotations sparingly. Summaries should retain conditions and exceptions.
- Preserve update history through statuses; do not silently rewrite a materially changed rule.
