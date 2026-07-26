## Description: <br>
Azure Infra provides chat-based Azure infrastructure assistance using Azure CLI and portal context for querying, auditing, monitoring resources, and proposing safe changes with explicit confirmation before write or destructive actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bmdhodl](https://clawhub.ai/user/bmdhodl) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, cloud engineers, and operators use this skill to inspect Azure subscriptions, audit security, cost, and health signals, and prepare Azure CLI changes that require confirmation before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can propose Azure CLI write, delete, IAM, scaling, billing, or deployment actions against an Azure subscription. <br>
Mitigation: Keep actions read-only by default, and before any write or destructive action require confirmation after reviewing the subscription, resource group, exact command, and dry-run output where available. <br>
Risk: The skill uses the current Azure CLI login to inspect cloud infrastructure and may surface resource, access, cost, or monitoring details. <br>
Mitigation: Install only where the agent is allowed to inspect the Azure tenant, and do not reveal or log secrets such as keys, tokens, client secrets, or credentials. <br>
Risk: Multiple Azure subscriptions or tenants can cause queries or changes to target the wrong scope. <br>
Mitigation: Confirm and state the active subscription or tenant before subscription-scoped results or any proposed change. <br>


## Reference(s): <br>
- [Azure CLI Query Patterns](references/azure-cli-queries.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/bmdhodl/skills/azure-infra) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Analysis, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown responses with inline Azure CLI commands and summarized command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Defaults to read-only Azure CLI usage; write or destructive actions require explicit confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
