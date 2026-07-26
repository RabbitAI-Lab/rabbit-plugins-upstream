## Description: <br>
Create, manage, and deploy ElevenLabs conversational AI agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pennyroyaltea](https://clawhub.ai/user/pennyroyaltea) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to let an agent manage ElevenLabs conversational AI agents, including listing agents, creating local configurations, syncing with ElevenLabs, deploying changes, adding webhook tools, and retrieving widget embed code. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify local agent files and remote ElevenLabs agents while instructing the agent to hide CLI details or silently initialize project files. <br>
Mitigation: Require the agent to disclose file creation, local or remote sync actions, and deployment effects before changes are made. <br>
Risk: Sync, push, update, and webhook-tool operations may overwrite local configuration or change a user's ElevenLabs account. <br>
Mitigation: Require explicit approval before overwrite, push, deployment, or webhook changes, and use dry-run previews before remote deployment. <br>
Risk: Authentication flow and API key handling may expose credentials if handled carelessly. <br>
Mitigation: Use the ElevenLabs CLI authentication flow, do not display or store API keys unnecessarily, and ask the agent to disclose credential handling before authentication. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pennyroyaltea/skills/elevenlabs-agents) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text summaries with CLI-backed agent management actions and configuration changes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local agent configuration files, webhook tool configuration, deployment status summaries, and HTML widget snippets.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
