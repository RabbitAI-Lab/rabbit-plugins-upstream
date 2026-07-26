## Description: <br>
PoYo Claude Fable 5 Messages API integration that helps agents prepare payloads, curl calls, streaming handling, tool-use schemas, structured output settings, and response parsing notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to build or explain PoYo Claude Fable 5 Messages API requests, including server-side payloads, streaming calls, tool definitions, structured output options, and response parsing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API keys or private request content could be exposed if copied into client-side code, logs, screenshots, public repositories, or chat output. <br>
Mitigation: Keep POYO_API_KEY in server-side environment variables or a secret manager, and avoid logging private messages, tool inputs, raw request bodies, or API key headers. <br>
Risk: The helper script sends the provided JSON payload to PoYo, so untrusted payloads could disclose data or trigger unintended requests. <br>
Mitigation: Inspect payloads before running the helper script, use it only from a trusted shell, and make live API calls only when the user explicitly asks. <br>
Risk: Returned tool calls can be unsafe if an application executes them without validation. <br>
Mitigation: Execute tool calls only through an application-controlled allowlist with validated arguments. <br>


## Reference(s): <br>
- [PoYo Claude Fable 5 model page](https://poyo.ai/models/claude-fable-5) <br>
- [PoYo Claude Messages API docs](https://docs.poyo.ai/api-manual/chat-series/claude-messages) <br>
- [PoYo Claude Fable 5 Messages API Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with JSON payloads and bash examples when useful] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model selection, request parameters, streaming notes, tool schemas, structured output settings, and response parsing guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
