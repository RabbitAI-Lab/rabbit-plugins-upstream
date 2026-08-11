## Description:

CCPA Audit runs a bilingual CCPA/CPRA compliance check covering 20 core items, with optional cloud scoring through compliancehub.cn.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

Compliance teams, developers, and external users can use this skill to preview CCPA/CPRA audit checks and generate a scored compliance report after explicitly opting into cloud scoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scored reports send audit answers and the ComplianceHub API key to compliancehub.cn.

Mitigation: Run scored reports only after explicit user opt-in and only when the user is comfortable sharing audit answers with that service.

Risk: Interrupted interactive audits may leave a local draft under ~/.config/compliancehub.

Mitigation: Remove the draft after interruption if the user does not want local audit state retained.

Risk: A saved API key file can expose account access if file permissions are loose.

Mitigation: Prefer COMPLIANCEHUB_API_KEY for temporary use or keep the key file restricted to chmod 600.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwumit/skills/ccpa-audit)
- [Publisher profile](https://clawhub.ai/user/wwumit)
- [ComplianceHub account center](https://compliancehub.cn/account.html?skill=ccpa-audit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Text, JSON, or HTML audit preview and report output with setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scored reports require an explicitly supplied ComplianceHub API key.]

## Skill Version(s):

2.0.0 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
