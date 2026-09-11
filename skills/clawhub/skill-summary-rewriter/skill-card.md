## Description:

Turns an approved Storefront Copy Brief into accurate titles, descriptions, and first-screen copy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill publishers use this skill after positioning is settled to turn an approved Storefront Copy Brief into storefront-ready display names, descriptions, hero copy, and optional CTAs with claim checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation may fetch executable Node package code that is not pinned to a reviewed version.

Mitigation: Prefer a version-pinned release or install only in a restricted environment where the npm dependency cannot access sensitive project or account data.

Risk: Generated storefront copy could overstate skill capabilities when the brief lacks audience, claim, or evidence fields.

Mitigation: Use the required brief completeness check and claim check; return to positioning review instead of producing unsupported claims when core evidence is missing.

## Reference(s):

- [Storefront Copy Writing Rules](artifact/references/summary_patterns.md)
- [Skill Storefront Copy Output Template](artifact/templates/summary_rewrite_output.md)
- [Brief-to-Copy Examples](artifact/examples/weak_vs_strong_summaries.md)
- [Skill Changelog](artifact/CHANGELOG.md)
- [ClawHub Skill Page](https://clawhub.ai/bonniegeng-max/skills/skill-summary-rewriter)
- [OpenClaw Publisher Homepage](https://github.com/bonniegeng-max/openclaw-publisher)

## Skill Output:

**Output Type(s):** [Markdown, Text, Guidance]

**Output Format:** [Markdown with structured copy variants and claim-check table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes brief completeness status, message spine, Direct/Distinctive/Compact variants, recommendation, claim check, and rejected wording rationale.]

## Skill Version(s):

2.0.0 (source: frontmatter, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
