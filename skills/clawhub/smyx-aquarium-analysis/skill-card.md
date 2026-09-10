## Description:

Analyzes uploaded or URL-based aquarium pet media through a server-side API to produce structured fish health findings, disease risk warnings, care suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External aquarium owners and developers can use this skill to submit aquatic pet video files or URLs for health analysis, potential disease warnings, care suggestions, report export links, and historical report lookup. Results are health-reference guidance and should not replace professional veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded aquarium media, report data, and internal identity values are sent to the publisher's service.

Mitigation: Use only after reviewing the publisher's data handling; avoid private media or account-linked use until identity handling and data retention are disclosed and approved.

Risk: Security evidence reports plaintext development API endpoints despite HTTPS claims.

Mitigation: Verify production HTTPS/TLS endpoint configuration before deployment and do not use builds that route media or identity data to development HTTP services.

Risk: Security evidence reports raw cloud tokens stored in a shared plaintext SQLite database.

Mitigation: Do not deploy until token storage is removed or replaced with scoped secrets and protected storage appropriate for the deployment environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-aquarium-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Markdown text with embedded JSON analysis data and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured health findings, disease warnings, care suggestions, historical report data, and report export URLs.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata; artifact frontmatter reports 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
