## Description: <br>
Claude 4.6 Series Messages API on PoYo / poyo.ai via `https://api.poyo.ai/v1/messages`; use for `claude-sonnet-4-6`, `claude-opus-4-6`, Claude-compatible messages, tools, structured output, prompt cache settings, vision content blocks, streaming, and server-side integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to prepare PoYo Claude 4.6 Messages API payloads, curl commands, streaming setup, tool-use configuration, structured-output settings, and response parsing guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API keys could be exposed through browser code, public repositories, logs, screenshots, chat output, or raw request headers. <br>
Mitigation: Keep `POYO_API_KEY` server-side in environment variables or a backend secret manager, and redact API keys from logs and generated examples. <br>
Risk: Private prompts, image content, or tool inputs could be sent to PoYo without the user's intended data-sharing posture. <br>
Mitigation: Review payloads before sending them and avoid sending private prompts, images, or tool inputs unless that is acceptable for the workflow. <br>
Risk: The helper script can submit a prepared payload to the live PoYo Messages API when invoked with a JSON file and `POYO_API_KEY`. <br>
Mitigation: Use the submit script only from a trusted shell after explicit confirmation that the payload should be sent to PoYo. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/coolhackboy/skills/poyo-claude-4-6-api) <br>
- [PoYo Claude 4.6 API model page](https://poyo.ai/models/claude-4-6-api) <br>
- [PoYo Claude Messages API docs](https://docs.poyo.ai/api-manual/chat-series/claude-messages) <br>
- [PoYo API key page](https://poyo.ai/dashboard/api-key) <br>
- [Local API reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payloads and inline bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include PoYo Messages API payloads, curl examples, streaming notes, tool configuration, structured-output settings, and response parsing guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
