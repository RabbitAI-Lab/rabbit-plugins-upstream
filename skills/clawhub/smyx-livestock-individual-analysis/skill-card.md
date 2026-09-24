## Description:

Identifies individual livestock (pigs, cattle, sheep) by facial or body-pattern features and outputs a stable individual ID with confidence for precision farm management and tracking. | 通过面部/体纹识别畜禽个体，实现精准管理追踪。

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and farm operations teams use this skill to identify pigs, cattle, and sheep from livestock face or body-pattern images and videos. It returns individual IDs, confidence values, matched visual regions, and report links to support identity association for precision feeding, health tracking, production records, and breeding management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded livestock media and report history may be sent to a remote service and associated with account identity.

Mitigation: Treat uploaded media and reports as account-linked data; deploy only after the publisher documents remote service behavior and data handling.

Risk: Security evidence reports hidden identity handling, persistent local tokens, and active plaintext HTTP development endpoints for sensitive media and authentication data.

Mitigation: Install only after development HTTP endpoints are replaced with verified HTTPS production hosts and credential storage behavior is fixed or accepted by the deployment owner.

Risk: Automatic history-query triggers can retrieve account-linked report history.

Mitigation: Narrow history-query triggers and require clear user intent before retrieving historical reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-individual-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Common analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON structured analysis reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include individual livestock IDs, confidence values, matched feature regions, historical report rows, and report export links.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
