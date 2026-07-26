## Description: <br>
Provides guidance and examples for building Claude 4.5 Series Messages API requests on PoYo, including payloads, curl commands, streaming, tools, structured output, and response parsing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and integration engineers use this skill to prepare Claude-compatible Messages API payloads for PoYo and to handle server-side integration details such as API keys, streaming, tools, structured outputs, and response parsing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prepared payloads can be sent to PoYo with the configured POYO_API_KEY. <br>
Mitigation: Review payloads for private data and run the submission script only when the user intentionally wants to call the PoYo API. <br>
Risk: Exposing POYO_API_KEY could allow unauthorized API use. <br>
Mitigation: Keep the key in a server-side environment variable or secret manager, and do not put it in browser code, logs, public repositories, screenshots, or chat output. <br>
Risk: Tool-use or structured-output payloads may affect downstream application behavior. <br>
Mitigation: Use tools only when the application can safely execute them, validate tool inputs, and avoid logging private prompts, messages, image content, tool inputs, or API key headers. <br>


## Reference(s): <br>
- [PoYo Claude 4.5 Series model page](https://poyo.ai/models/claude-4-5-api) <br>
- [PoYo Claude Messages API docs](https://docs.poyo.ai/api-manual/chat-series/claude-messages) <br>
- [Local PoYo API reference](artifact/references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-claude-4-5-api) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with JSON and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include API payloads, curl examples, response parsing notes, and guidance for safe server-side use.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
