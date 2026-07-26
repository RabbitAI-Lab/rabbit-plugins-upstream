## Description: <br>
Azure Cloud Architect helps agents use a local Azure CLI session to inventory resources, navigate subscriptions, audit RBAC and security posture, analyze costs, and prepare confirmed Azure changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Cloud engineers, operations teams, and security reviewers use this skill to inspect Azure subscriptions, produce CLI-backed reports, and plan cost or security remediation while keeping write or destructive actions behind explicit confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help operate Azure through the user's local Azure CLI session, so commands may act with the privileges of the signed-in account. <br>
Mitigation: Use least-privilege Azure roles and verify the active account, tenant, and subscription before approving commands. <br>
Risk: Write, destructive, or sensitive Azure operations could change or remove production resources if approved without review. <br>
Mitigation: Review proposed write or destructive commands, prefer dry-run or what-if previews where available, and require explicit confirmation before execution. <br>
Risk: Azure command output or user prompts may expose secrets, tokens, keys, or sensitive infrastructure details. <br>
Mitigation: Avoid pasting secrets into chats or logs, redact sensitive values from command output, and rotate any credential that is accidentally exposed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/azure-cloud-architect) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with Azure CLI command blocks and tabular summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include proposed Azure CLI commands, audit findings, cost-analysis summaries, and confirmation steps for write or destructive actions.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
