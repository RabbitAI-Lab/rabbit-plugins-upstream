## Description:

Based on Huawei Cloud COC (Cloud Operations Center) APIs for script management and remote execution. Supports creating custom scripts (Shell, Python, Bat) and batch execution on target host instances via UniAgent. Applicable to cloud operations automation and batch script deployment scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to create, list, inspect, execute, query, and delete Huawei Cloud COC scripts for Flexus L instances. It supports batch operations, automated maintenance, incident response, application deployment, and parallel data-processing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can execute scripts as root on target Huawei Cloud instances.

Mitigation: Use least-privilege, temporary Huawei Cloud credentials; test on non-production instances first; and manually confirm root execution intent outside the skill before running high-impact commands.

Risk: The skill can delete cloud scripts without a separate enforced confirmation safeguard.

Mitigation: Manually verify the script UUID and intended deletion outside the skill, and prefer a dry-run or review step before invoking delete operations.

Risk: Huawei Cloud AK/SK or security-token values can be exposed if passed on the command line or echoed into conversation.

Mitigation: Provide credentials through environment variables, avoid command-line credential arguments, and do not print credential values or full commands containing secrets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-flexus-l-server-scripts-excute)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [IAM Permission Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [huaweicloudsdkcoc package](https://pypi.org/project/huaweicloudsdkcoc/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON-style API result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call packaged Python scripts that create, execute, query, list, inspect, or delete Huawei Cloud COC scripts.]

## Skill Version(s):

1.0.2 (source: server release evidence; artifact pyproject.toml reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
