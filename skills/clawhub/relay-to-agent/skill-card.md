## Description: <br>
Relay messages to AI agents on any OpenAI-compatible API with multi-turn session management, agent listing, message sending, and session reset support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ericsantos](https://clawhub.ai/user/ericsantos) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to route prompts to configured OpenAI-compatible agents, inspect available agents, and continue or reset local conversation sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, prior session context, and the endpoint API credential are sent to the configured API provider. <br>
Mitigation: Use only trusted endpoints and avoid sending secrets or regulated data unless the endpoint and local machine are approved for that data. <br>
Risk: Conversation history is persisted in plaintext local session files. <br>
Mitigation: Use --reset or delete the session cache when retained history is not desired. <br>


## Reference(s): <br>
- [Relay To Agent ClawHub skill page](https://clawhub.ai/ericsantos/skills/relay-to-agent) <br>
- [OpenAI Chat API reference](https://platform.openai.com/docs/api-reference/chat) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text or JSON responses from the selected agent, with Markdown usage guidance and shell command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and RELAY_API_KEY; uses agents.json or RELAY_CONFIG for endpoint and agent configuration.] <br>

## Skill Version(s): <br>
0.0.2 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
