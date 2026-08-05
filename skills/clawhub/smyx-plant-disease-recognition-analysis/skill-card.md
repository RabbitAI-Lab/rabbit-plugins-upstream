## Description:

Identifies plant diseases from image or video input and returns structured diagnostic reports with disease type, cause, severity, prevention suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to analyze plant photos or videos for disease diagnosis, prevention guidance, and cloud report retrieval. It is intended for agricultural production, horticulture, garden maintenance, and plant protection workflows where visual symptoms need structured triage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images or videos may be uploaded to the publisher's cloud service for analysis.

Mitigation: Avoid sensitive media unless cloud processing by this publisher is acceptable, and review organizational data-handling requirements before use.

Risk: The skill may automatically create or reuse an account identity, query cloud report history, read a workspace API-key file, and persist session tokens locally.

Mitigation: Use isolated workspaces for evaluation, review local credential and token storage before installation, and confirm account-linked history behavior is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-disease-recognition-analysis)
- [API interface documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown and structured JSON text with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local image/video files, public media URLs, history-list queries, and optional file output.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter states 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
