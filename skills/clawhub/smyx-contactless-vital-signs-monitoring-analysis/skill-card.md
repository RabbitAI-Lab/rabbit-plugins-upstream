## Description:

Non-contact detection of heart rate, respiration, blood oxygen, and heart rate variability from camera footage, without requiring wearable devices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze uploaded or URL-based face videos for contactless vital-sign estimates and to retrieve prior cloud-hosted analysis reports. Results are intended for health reference and are not a substitute for professional medical measurement or diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive face videos and health-related biometric data may be uploaded to cloud services, and the release includes plaintext development endpoints.

Mitigation: Use only documented HTTPS production endpoints and do not process real face videos or health data until upload, storage, retention, and access controls are documented and reviewed.

Risk: The skill silently creates or reuses an identity and can retrieve cloud-hosted report history.

Mitigation: Require clear user consent for identity creation and history retrieval, and verify that report access is scoped to the intended user before deployment.

Risk: Reusable access tokens may be stored locally.

Mitigation: Store credentials in an appropriate secret store, limit workspace sharing, and rotate or revoke test credentials after evaluation.

## Reference(s):

- [API 接口文档](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-contactless-vital-signs-monitoring-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON text returned from skill command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured vital-sign analysis, risk or recommendation text, report export links, and cloud history lists.]

## Skill Version(s):

1.0.16 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
