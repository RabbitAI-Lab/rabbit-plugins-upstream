## Description: <br>
Helps agents prepare Claude Opus 4.8 Messages API payloads, curl calls, streaming handling, tool definitions, structured output settings, and server-side integration notes for PoYo. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to build Claude-compatible Messages API requests for PoYo, including payload design, server-side curl examples, streaming notes, and response parsing guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected request payload content may be sent to PoYo during user-directed live calls. <br>
Mitigation: Review payloads before submission and avoid sending private or regulated data unless PoYo is approved for that use. <br>
Risk: PoYo API keys could be exposed if included in browser code, repositories, logs, screenshots, or chat output. <br>
Mitigation: Keep POYO_API_KEY server-side in environment variables or a secret manager and avoid logging raw API key headers. <br>
Risk: Live API calls may submit data outside the local environment. <br>
Mitigation: Make live calls only when the user explicitly requests them and provides a trusted server-side environment. <br>


## Reference(s): <br>
- [PoYo Claude Opus 4.8 model page](https://poyo.ai/models/claude-opus-4-8) <br>
- [PoYo Claude Messages API docs](https://docs.poyo.ai/api-manual/chat-series/claude-messages) <br>
- [PoYo API key page](https://poyo.ai/dashboard/api-key) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-claude-opus-4-8) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON payload examples and curl commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model selection, request parameters, system prompt notes, tool definitions, structured output settings, cache settings, streaming handling, and response parsing notes.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
