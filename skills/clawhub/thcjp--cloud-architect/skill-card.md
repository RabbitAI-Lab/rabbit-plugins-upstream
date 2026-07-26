## Description: <br>
Provides cloud architecture guidance for AWS, Azure, and GCP, including multi-cloud design, 6Rs migration planning, FinOps cost optimization, high availability and disaster recovery, security and compliance, infrastructure as code, and landing zone governance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, platform engineers, and cloud architecture teams use this skill to plan cloud migrations, compare AWS/Azure/GCP service choices, design resilient and compliant architectures, estimate costs, and draft IaC-oriented implementation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may suggest or use local command execution while presenting primarily advisory cloud architecture guidance. <br>
Mitigation: Use it only in trusted workspaces, review each command before execution, and keep production credentials unavailable unless access is intentionally authorized. <br>
Risk: Cloud architecture, migration, cost, security, or IaC recommendations can affect production availability, spend, or compliance if applied without review. <br>
Mitigation: Treat outputs as drafts for human architecture review, test changes in non-production environments, and validate cost and compliance assumptions against the target cloud accounts. <br>
Risk: Optional callback URLs may receive task results or metadata. <br>
Mitigation: Provide callback URLs only for trusted destinations and avoid sending sensitive architecture, credential, account, or workload details to untrusted endpoints. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/cloud-architect) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with architecture recommendations, checklists, and cloud configuration or IaC examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include service comparisons, migration plans, cost estimates, security controls, disaster recovery plans, and Terraform, CloudFormation, or ARM examples.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
