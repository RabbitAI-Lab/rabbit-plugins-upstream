## Description: <br>
Uses local Azure CLI commands to help agents query, diagnose, audit, and manage Azure cloud resources, with read-only operations by default and confirmation required for changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, DevOps engineers, and cloud operators use this skill to inspect Azure subscriptions, diagnose resource health, review security posture, analyze costs, and prepare Azure CLI commands for approved changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can lead an agent to run Azure CLI commands under the user's current Azure login, including potentially impactful cloud-management operations. <br>
Mitigation: Keep actions read-only by default; require review of the full command, target subscription or resource, and expected impact before any write or destructive operation. <br>
Risk: The security review says the artifact describes broad file, API, callback, and API-key capabilities that are not clearly scoped to Azure work. <br>
Mitigation: Limit use to Azure resource queries unless the publisher narrows those capabilities, and do not retrieve or display secret values. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/azure-infra) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline Azure CLI command blocks, tables, and concise status summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results should identify the active Azure subscription context and avoid displaying secret values.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
