## Description:

Detects and analyzes indoor plant light stress from images and optional lux data, identifying low or excessive light symptoms and suggesting adjustments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze indoor plant images, videos, or image URLs for light-stress symptoms and receive structured care guidance. It also supports querying prior cloud-hosted analysis reports for the resolved user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, URLs, and user identifiers may be sent to the lifeemergence cloud service for analysis and report lookup.

Mitigation: Use only with plant media and URLs that are appropriate to upload to that service, and avoid submitting unrelated personal or sensitive content.

Risk: The skill can create or reuse an identity and keep returned tokens in a local SQLite record in the workspace data directory.

Mitigation: Review the workspace data directory before and after use, restrict local file access where possible, and remove stored tokens when they are no longer needed.

Risk: Values placed in data/smyx-api-key.txt are treated as an identity for remote login.

Mitigation: Do not store unrelated secrets in data/smyx-api-key.txt; keep that file limited to the intended identity value.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-indoor-plant-light-stress-detect-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown text with structured JSON content and optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the displayed analysis result to a user-specified output file.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
