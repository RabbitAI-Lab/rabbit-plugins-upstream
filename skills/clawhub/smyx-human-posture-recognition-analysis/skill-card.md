## Description:

Recognizes various poses such as standing, sitting, lying down, bending, raising hands, running, and falling, and supports abnormal pose recognition and fall warnings for security monitoring and elderly care.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to analyze local or URL-based video for human posture classification, fall detection, abnormal posture monitoring, and historical posture-analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive local videos, image or video URLs, and identity or tenant metadata may be sent to configured remote services.

Mitigation: Use the skill only with appropriate consent, review the remote service configuration before installation, and avoid submitting sensitive or regulated footage unless the service is approved.

Risk: Packaged configuration and local token handling may expose deployments to unintended endpoints or weak credential control.

Mitigation: Replace packaged defaults with approved production endpoints and credential storage before deployment, and avoid passing secrets on the command line.

Risk: Historical report queries may return records associated with generated or existing user identifiers.

Mitigation: Limit report-history access to authorized users and verify tenant and user scoping before enabling history queries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-human-posture-recognition-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [API documentation](references/api_doc.md)
- [smyx analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown reports, JSON details, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include posture-analysis results, fall-warning status, report links, and history tables.]

## Skill Version(s):

1.0.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
