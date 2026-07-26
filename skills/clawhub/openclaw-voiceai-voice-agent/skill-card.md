## Description: <br>
Create, manage, and deploy Voice.ai conversational AI agents for agent management, configuration, deployment, knowledge bases, phone numbers, and analytics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gizmogremlin](https://clawhub.ai/user/gizmogremlin) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to manage Voice.ai voice agents from an agent workflow, including creating agents, updating prompts and greetings, deploying or pausing agents, and reviewing agent details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can affect live Voice.ai agents, phone resources, analytics, and deletion workflows. <br>
Mitigation: Require explicit user confirmation before deployment, deletion, phone-number changes, or access to call history and analytics. <br>
Risk: The skill requires bearer-token authentication for the Voice.ai API. <br>
Mitigation: Keep API keys in environment variables or approved secret storage, and do not print, hardcode, or commit bearer tokens. <br>
Risk: Changing prompts, greetings, model settings, or MCP connections can alter the behavior of public-facing voice agents. <br>
Mitigation: Review configuration changes before applying them and test agent behavior before production use. <br>


## Reference(s): <br>
- [Voice.ai Developer Dashboard](https://voice.ai/app/dashboard/developers) <br>
- [Voice Agents Guide](https://voice.ai/docs/guides/voice-agents/quickstart) <br>
- [Agent API Reference](https://voice.ai/docs/api-reference/agent-management/create-agent) <br>
- [Voice.ai Status Page](https://status.voice.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON configuration examples, and CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call Voice.ai APIs when run with a valid VOICE_AI_API_KEY; commands can create, update, deploy, pause, delete, and inspect live voice-agent resources.] <br>

## Skill Version(s): <br>
0.1.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
