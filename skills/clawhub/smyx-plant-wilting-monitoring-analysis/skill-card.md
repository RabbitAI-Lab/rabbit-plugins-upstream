## Description:

Early monitoring of plant wilting based on hyperspectral imaging and computer vision, captures early wilting signs before visible symptoms, provides early warning for precision irrigation and disease control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to submit plant image, video, or URL inputs for early wilting analysis, wilting-grade assessment, and environment-versus-pathology warning reports. It can also query identity-linked historical plant wilting reports from the cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends plant images, videos, or media URLs to a cloud analysis service.

Mitigation: Use only media appropriate for third-party cloud processing, and confirm the publisher's data retention and handling practices before installing for sensitive environments.

Risk: The skill silently creates or reuses an internal user identity and queries identity-linked report history.

Mitigation: Review whether automatic identity creation and history lookup match the deployment's account, audit, and privacy expectations before use.

Risk: The skill may store service tokens in a local workspace database.

Mitigation: Install only in workspaces where local credential storage is acceptable, and remove local workspace data when the skill is no longer trusted or needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-wilting-monitoring-analysis)
- [API interface documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, files, guidance]

**Output Format:** [Markdown text with structured JSON report content, report links, and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local file paths or public media URLs as inputs, calls a cloud analysis API, and can return identity-linked historical report lists.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
