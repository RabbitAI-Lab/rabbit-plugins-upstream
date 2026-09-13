## Description:

Fetches public Kuaishou data by keyword search, creator post listing, and video comment retrieval, returning structured JSON for analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, content operators, and developers use this skill to collect public Kuaishou search results, creator posts, and video comments for content planning, competitor monitoring, trend analysis, KOL screening, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou search terms, video or profile URLs, and GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Install and run the skill only when this data sharing is acceptable, and manage GUAIKEI_API_TOKEN as a secret.

Risk: Saved task logs can retain fetched public data, including comments that may contain personal information.

Mitigation: Delete, redact, or restrict access to saved logs when retained copies are not needed.

Risk: Empty or failed API responses can be mistaken for valid analysis inputs.

Mitigation: Check status and error_code before using results, and do not treat empty or error outputs as successful data collection.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-kuaishou-data-extractor)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Structured JSON with status, error_code, request, skill_metadata, and results; successful runs also save JSON task logs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN, sends Kuaishou query inputs to guaikei.com, and supports task limits up to 10,000 records.]

## Skill Version(s):

1.0.0 (source: release metadata, package.json, changelog released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
