## Description:

Alibaba Cloud RDS Copilot is an intelligent operations assistant skill for RDS-related Q&A, SQL optimization, instance operations, and troubleshooting through RdsAi OpenAPI calls made with Alibaba Cloud CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, database operators, and support engineers use this skill to ask RDS Copilot for database troubleshooting, SQL optimization, instance-operation guidance, and follow-up diagnosis. It helps prepare Alibaba Cloud CLI calls, validate required inputs, and interpret RDS Copilot responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can ask the agent to install or upgrade Alibaba Cloud CLI and the rdsai plugin before use.

Mitigation: Review install, upgrade, network, and sudo commands before approval, and run them only in an environment where Alibaba Cloud CLI changes are acceptable.

Risk: The skill helps configure cloud credentials for Alibaba Cloud CLI.

Mitigation: Use a dedicated least-privilege RAM user or role, prefer interactive CLI credential setup, and avoid pasting secrets or sensitive production data into prompts.

Risk: The skill defaults to cn-hangzhou, zh-CN, and Asia/Shanghai when the user does not override region, language, or timezone.

Mitigation: Confirm or override region, language, and timezone before executing RDS Copilot calls in another environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-rds-copilot)
- [Related APIs](references/related-apis.md)
- [RAM Policies](references/ram-policies.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Alibaba Cloud CLI documentation](https://help.aliyun.com/zh/cli/)
- [RDS AI Assistant Professional Edition guide](https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/manage-rds-colipot-professional-edition)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API Calls, Markdown]

**Output Format:** [Markdown with inline bash commands and JSON response interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Alibaba Cloud CLI preflight steps, RdsAi command construction, credential-setup guidance, and troubleshooting recommendations.]

## Skill Version(s):

0.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
