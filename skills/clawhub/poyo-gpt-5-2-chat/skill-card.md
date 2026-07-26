## Description: <br>
GPT-5.2 chat completions on PoYo via the OpenAI-compatible chat completions API, with guidance for payloads, streaming, server-side API keys, and integration examples. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare PoYo `gpt-5.2` chat completion requests, including message payloads, optional streaming behavior, curl examples, and response parsing notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The helper sends chat message content to PoYo when invoked. <br>
Mitigation: Review payloads before submission and avoid sending private or policy-restricted content unless the deployment is approved for that data. <br>
Risk: The PoYo API key could be exposed if copied into client code, logs, screenshots, repositories, or chat output. <br>
Mitigation: Keep `POYO_API_KEY` in server-side environment variables or a backend secret manager and avoid logging authorization headers or raw secrets. <br>
Risk: The shell helper performs a live chat completion request when run with a payload file. <br>
Mitigation: Run it only from a trusted shell with an intentional payload and a server-side `POYO_API_KEY`. <br>


## Reference(s): <br>
- [PoYo GPT-5.2 model page](https://poyo.ai/models/gpt-5-2) <br>
- [PoYo chat completions API docs](https://docs.poyo.ai/api-manual/chat-series/chat-completions) <br>
- [PoYo API key page](https://poyo.ai/dashboard/api-key) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-gpt-5-2-chat) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payloads and bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model identifiers, chat payloads, streaming notes, system prompt constraints, and response parsing guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
