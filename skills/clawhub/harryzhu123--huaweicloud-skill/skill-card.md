## Description: <br>
The huaweicloud-skill helps agents plan, run, and validate Huawei Cloud hcloud/KooCLI resource operations and Huawei Cloud MaaS model tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[harryzhu123](https://clawhub.ai/user/harryzhu123) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and cloud operators use this skill to inspect Huawei Cloud context, construct hcloud/KooCLI commands, plan safe resource changes, validate execution results, and work with Huawei Cloud MaaS APIs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide real Huawei Cloud resource changes and MaaS calls that may affect live infrastructure or incur cost. <br>
Mitigation: Use least-privilege hcloud profiles or environment credentials, prefer plan and dry-run modes first, and review exact submit tokens and commands before live changes. <br>
Risk: Terraform, billing, and account-wide read workflows can expose sensitive production state, spending data, or broad account scope. <br>
Mitigation: Run those workflows only in reviewed directories and accounts, limit scope where possible, and redact sensitive outputs before sharing results. <br>
Risk: Credentials, API keys, private keys, and security-sensitive network settings may be mishandled during cloud operations. <br>
Mitigation: Keep secrets in local profiles or environment variables, avoid echoing them in conversation or logs, and require explicit review for security group, identity, key, and public exposure changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/harryzhu123/skills/huaweicloud-skill) <br>
- [Runtime safety boundaries](references/runtime-safety-boundaries.md) <br>
- [Workflow](references/workflow.md) <br>
- [Authentication and context](references/auth-and-context.md) <br>
- [Command construction](references/command-construction.md) <br>
- [Terraform workflow](references/terraform-workflow.md) <br>
- [MaaS model calls](references/maas-model-calls.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON plans, and Terraform or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs often include dry-run plans, explicit confirmation steps, validation checks, and cautions for cloud credentials, billing scope, and state-changing operations.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
