## Description: <br>
GPT-5.4 chat completions on PoYo via an OpenAI-compatible chat completions API, with guidance for payloads, streaming, server-side curl usage, and response handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare and submit PoYo GPT-5.4 chat completion requests, including system prompts, multi-turn messages, streaming options, and server-side integration examples. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prepared prompts, messages, and payloads may be sent to the PoYo service when the submit script is used. <br>
Mitigation: Only submit payloads the user intends to send to PoYo, and avoid enabling the skill for generic tasks unless PoYo involvement is desired. <br>
Risk: The skill requires a PoYo API key for live requests. <br>
Mitigation: Keep POYO_API_KEY in a server-side environment variable or secret manager and do not expose it in browser code, logs, screenshots, public repositories, or chat output. <br>


## Reference(s): <br>
- [PoYo GPT-5.4 model page](https://poyo.ai/models/gpt-5-4) <br>
- [PoYo chat completions API docs](https://docs.poyo.ai/api-manual/chat-series/chat-completions) <br>
- [PoYo API key page](https://poyo.ai/dashboard/api-key) <br>
- [API reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-gpt-5-4) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with JSON payloads and inline bash or curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include synchronous or streaming response handling notes and server-side API key guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
