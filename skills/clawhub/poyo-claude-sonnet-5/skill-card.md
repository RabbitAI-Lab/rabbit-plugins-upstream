## Description: <br>
Helps agents prepare Claude Sonnet 5 Messages API payloads, curl examples, streaming calls, tool-use settings, structured output settings, and integration guidance for PoYo. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to create Claude-compatible Messages API requests for PoYo, including server-side curl calls, payload examples, and integration notes for coding, analysis, chat, vision, and structured-output workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, payloads, tool inputs, images, and system prompts may be sent to PoYo when the API is called. <br>
Mitigation: Confirm the user intends to share the selected content with PoYo, avoid private data unless required, and review payload files before submission. <br>
Risk: The helper script requires a PoYo API key and submits the provided payload file over the network. <br>
Mitigation: Keep POYO_API_KEY in server-side environment variables or a secret manager, never expose it in frontend code or logs, and run the script only from a trusted shell. <br>


## Reference(s): <br>
- [PoYo Claude Sonnet 5 model page](https://poyo.ai/models/claude-sonnet-5) <br>
- [PoYo Claude Messages API docs](https://docs.poyo.ai/api-manual/chat-series/claude-messages) <br>
- [API reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-claude-sonnet-5) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payloads and bash snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model IDs, Claude Messages payloads, curl commands, streaming notes, tool-use settings, structured-output settings, and response parsing guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
