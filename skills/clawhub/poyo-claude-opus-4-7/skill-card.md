## Description: <br>
Claude Opus 4.7 Messages API helper for PoYo that assists with Claude-compatible payloads, curl requests, streaming setup, tool-use payloads, structured output settings, and response parsing notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when they have chosen PoYo for a Claude Opus 4.7 workflow and need request payloads, server-side curl commands, streaming guidance, tool-use configuration, structured output setup, or integration notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send user-provided prompts, images, tool inputs, or other payload content to PoYo when explicitly run. <br>
Mitigation: Review payloads before submission and avoid sending private data unless that data sharing is acceptable. <br>
Risk: The PoYo API key is required for live requests and could be exposed if placed in client-side code, logs, screenshots, repositories, or chat output. <br>
Mitigation: Keep POYO_API_KEY in server-side environment variables or a backend secret manager and do not print raw API key headers. <br>
Risk: Optional request fields such as tools, streaming, structured output, cache settings, and thinking may vary by provider support. <br>
Mitigation: Verify current field support in the PoYo documentation before relying on optional parameters. <br>


## Reference(s): <br>
- [PoYo Claude Opus 4.7 model page](https://poyo.ai/models/claude-opus-4-7) <br>
- [PoYo Claude Messages API documentation](https://docs.poyo.ai/api-manual/chat-series/claude-messages) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-claude-opus-4-7) <br>
- [artifact/references/api.md](artifact/references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payloads and bash curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce PoYo request payloads, response parsing notes, and server-side execution guidance; live submission requires explicit user intent and POYO_API_KEY.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
