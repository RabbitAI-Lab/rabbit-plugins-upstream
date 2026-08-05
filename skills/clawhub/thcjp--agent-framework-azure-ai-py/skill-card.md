## Description: <br>
This documentation-only skill guides developers building Azure AI Foundry agents with cloud search and multi-model capabilities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill for guidance on building Azure AI Foundry agents, including tool configuration, cloud search, multi-model workflows, and structured responses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide active development actions, including file writes and shell commands, despite being described as documentation-only. <br>
Mitigation: Review proposed changes and commands before approval, and run the agent in a constrained workspace. <br>
Risk: Azure cloud-agent usage may require credentials, network access, and billable resources. <br>
Mitigation: Use least-privilege Azure credentials, confirm target subscriptions and regions, and monitor cloud costs before running generated workflows. <br>
Risk: Generated guidance may be unsuitable for critical decisions that require complete determinism. <br>
Mitigation: Keep human review in the loop for high-impact decisions and validate outputs against authoritative project requirements. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/agent-framework-azure-ai-py) <br>
- [Microsoft Learn API reference mentioned by the skill](https://learn.microsoft.com/api/协议) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with JSON, Python, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose file reads, file writes, shell commands, Azure cloud-agent setup, and credential configuration steps.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
