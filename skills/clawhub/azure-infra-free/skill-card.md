## Description: <br>
Azure Infra Free helps agents use the local Azure CLI for read-only Azure resource inventory and basic health checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operators, and support engineers use this skill to inspect Azure subscriptions, list common resources, check VM status, and review recent failed activity without performing write actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs local Azure CLI commands against whichever Azure account and subscription are active. <br>
Mitigation: Confirm the logged-in account and active subscription before running queries, and include the subscription context in results. <br>
Risk: Callback URLs could send results to an external endpoint if supplied. <br>
Mitigation: Avoid callback URLs unless the user explicitly requests an external notification flow and confirms the destination. <br>
Risk: Users may ask for write actions or secret retrieval beyond the free skill's intended scope. <br>
Mitigation: Block write actions, avoid displaying secrets, and keep generated Azure CLI commands limited to read-only list, show, get, and monitor queries. <br>


## Reference(s): <br>
- [Azure Infra Free on ClawHub](https://clawhub.ai/thcjp/skills/azure-infra-free) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline Azure CLI commands and structured command output summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should identify the active Azure subscription, avoid secrets, and keep commands read-only.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release evidence; artifact frontmatter reports 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
