## Description: <br>
Azure Cloud Architect Free helps agents use the local Azure CLI to navigate subscriptions, list Azure resources, and check virtual machine health for basic Azure inventory and health-check workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operators, and IT staff use this skill to answer basic Azure environment questions from an existing Azure CLI login, including listing resources, checking VM power state, and selecting the active subscription. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may change the active Azure CLI subscription for later commands in the same environment. <br>
Mitigation: Verify the active subscription with az account show after using the skill, especially before running any separate write-capable Azure commands. <br>
Risk: Results depend on the user's existing Azure CLI login, tenant, and permissions. <br>
Mitigation: Confirm the expected Azure account, tenant, subscription, and Reader-level access before relying on inventory or health-check results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/azure-cloud-architect-free) <br>
- [Skill homepage](https://skillhub.cn) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with Azure CLI command snippets and tabular command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the local Azure CLI session; outputs may include subscription context and Azure resource tables.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
