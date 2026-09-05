# Acceptance Criteria

## CRITICAL Checks

| # | Check | Method |
|---|-------|--------|
| 1 | SKILL.md exists with valid frontmatter | File inspection |
| 2 | `name` in frontmatter matches directory name (`huawei-cloud-vpc-list`) | grep |
| 3 | `description` in frontmatter includes trigger words | grep |
| 4 | No `version` field in frontmatter | grep |
| 5 | Overview section exists | grep for `## Overview` |
| 6 | Prerequisites section exists | grep for `## Prerequisites` |
| 7 | Workflow section exists | grep for `## Workflow` |
| 8 | Core Commands section exists | grep for `## Core Commands` |
| 9 | Parameter Confirmation section exists | grep for `## Parameter Confirmation` |
| 10 | Reference Documents section exists | grep for `## Reference Documents` |
| 11 | `references/iam-policies.md` exists | File existence |
| 12 | No hardcoded credentials | grep for AK/SK patterns |
| 13 | No cross-skill direct calls | grep for other skill names |
| 14 | `scripts/list_vpcs.py` exists with proper pagination | File existence + code review |

## HIGH Checks

| # | Check | Method |
|---|-------|--------|
| 15 | `references/cli-installation-guide.md` exists | File existence |
| 16 | `references/dataflow-diagram.md` exists | File existence |
| 17 | All hcloud/SDK commands include JSON output option | grep |

## Pagination-Fix Specific Checks

| # | Check | Method |
|---|-------|--------|
| 18 | Script aggregates all pages using marker loop | Code review: grep for `while` + `marker` |
| 19 | `total_count` reflects full aggregation, not single page | Code review: check `len(all_vpcs)` |
| 20 | Duplicate detection in pagination loop | Code review: check first-item-duplicate break |
| 21 | Max pages safety limit (prevents infinite loop) | Code review: check `max_pages` limit |
| 22 | VPC count stable across multiple queries | Functional test: run twice, compare counts |

## LOW Checks

| # | Check | Method |
|---|-------|--------|
| 23 | `references/acceptance-criteria.md` exists | File existence |
| 24 | Total skill size < 40 MB | du -sh |
| 25 | Total files < 30 | find count |
| 26 | SKILL.md < 500 lines | wc -l |
| 27 | All file extensions in allowlist | check extensions |