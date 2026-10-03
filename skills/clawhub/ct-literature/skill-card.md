## Description:

Searches published medical literature across public sources, merges and deduplicates results, and prepares evidence reports with an optional qualitative safety-literature subset.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

Clinical researchers and evidence-review teams use this skill to find and organize published studies for trial planning, systematic literature reviews, and qualitative published-safety checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online searches may disclose search topics, filters, locale/version, and a stable machine-derived identifier to the author's service, with possible downstream audit logging.

Mitigation: Use local/offline mode where available for sensitive medical, competitive, or unpublished topics; avoid the default online path unless that disclosure is acceptable.

Risk: API keys stored in published skill folders or cosmetically obfuscated .env files may be exposed.

Mitigation: Keep API keys out of published skill folders; do not treat .env obfuscation as security.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/medstatstar/skills/ct-literature)
- [Project homepage (listed in skill metadata; import provenance unavailable)](https://github.com/medstatstar/ct-literature)
- [Capabilities and output guide](references/capabilities.md)
- [Multi-database search guide](references/multi-db-search.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown guidance and HTML and XLSX evidence reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional citation exports, open-access PDF downloads, and a qualitative safety-literature subset.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; bundled skill frontmatter says 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
