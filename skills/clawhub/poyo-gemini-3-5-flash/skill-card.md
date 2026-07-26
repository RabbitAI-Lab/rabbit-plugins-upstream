## Description: <br>
Gemini 3.5 Flash chat on PoYo / poyo.ai via `https://api.poyo.ai/v1/chat/completions` and Gemini Native Format; use for `gemini-3.5-flash`, chat completions, native generateContent, streaming, system prompts, multimodal prompt structure, generation config, and server-side integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and integration engineers use this skill to prepare Gemini 3.5 Flash requests on PoYo, including OpenAI-compatible chat payloads, Gemini Native Format payloads, streaming calls, and server-side curl examples. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API keys or raw authorization headers could be exposed through client code, logs, screenshots, repositories, or chat output. <br>
Mitigation: Keep POYO_API_KEY in a server-side environment variable or secret manager, and avoid logging secrets or authorization headers. <br>
Risk: Prompts, media, system messages, or other private data may be sent to the external PoYo API endpoint. <br>
Mitigation: Send only data that is approved to leave the environment, and avoid logging private prompt content or inline media data. <br>
Risk: The helper script can make a live API request with the supplied payload file. <br>
Mitigation: Run the helper only from a trusted shell when a live call is explicitly requested, and review the payload file before execution. <br>


## Reference(s): <br>
- [PoYo Gemini 3.5 Flash model page](https://poyo.ai/models/gemini-3-5-flash) <br>
- [PoYo Gemini Native Format API docs](https://docs.poyo.ai/api-manual/chat-series/gemini-native-format) <br>
- [PoYo Chat Completions API docs](https://docs.poyo.ai/api-manual/chat-series/chat-completions) <br>
- [PoYo Gemini 3.5 Flash API Reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-gemini-3-5-flash) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payloads, curl examples, and concise integration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and POYO_API_KEY for the helper script; supports synchronous and streaming request guidance when explicitly requested.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
