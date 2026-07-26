## Description: <br>
This documentation skill guides agents that help developers build Azure AI Foundry agents with cloud search and multi-model capabilities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill for guidance on building Azure AI Foundry agent workflows, including model calls, conversational agents, web search, hosted tools, and structured outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests execution and code-modification authority that is not clearly scoped in the artifact. <br>
Mitigation: Review the skill before installation and use it only in repositories where code edits and command execution are acceptable. <br>
Risk: Azure examples may use local credentials, network access, hosted tools, and billable cloud resources. <br>
Mitigation: Use least-privilege cloud credentials, confirm target subscriptions and regions, and monitor cost before running cloud-backed examples. <br>
Risk: The artifact states that it is not suitable for decisions requiring complete certainty. <br>
Mitigation: Require human review for high-impact decisions and verify generated guidance against official Azure documentation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/agent-framework-azure-ai-py) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Skill homepage](https://skillhub.cn) <br>
- [Microsoft Learn API reference](https://learn.microsoft.com/api/协议) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with code blocks and structured examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include JSON-shaped examples, environment variable guidance, and cloud setup notes.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
