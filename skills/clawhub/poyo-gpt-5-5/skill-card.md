## Description: <br>
GPT-5.5 chat completions on PoYo / poyo.ai via `https://api.poyo.ai/v1/chat/completions`; use for `gpt-5.5`, OpenAI-compatible chat payloads, coding help, reasoning, system prompts, multi-turn messages, streaming chat, max_tokens, and server-side chat integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to prepare PoYo GPT-5.5 chat completion payloads, curl examples, streaming guidance, and server-side integration notes for OpenAI-compatible chat workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prepared prompts, system messages, and payload files are sent to PoYo's external API when the skill is explicitly used. <br>
Mitigation: Use the skill only for workflows where sending that data to PoYo is intended, and review payload JSON before submitting sensitive content. <br>
Risk: The skill requires a PoYo API key for live requests. <br>
Mitigation: Keep POYO_API_KEY in a server-side environment variable or backend secret manager, and do not place API keys in frontend code, public repositories, logs, screenshots, or chat output. <br>


## Reference(s): <br>
- [PoYo GPT-5.5 model page](https://poyo.ai/models/gpt-5-5) <br>
- [PoYo chat completions API docs](https://docs.poyo.ai/api-manual/chat-series/chat-completions) <br>
- [PoYo API key page](https://poyo.ai/dashboard/api-key) <br>
- [Local API reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-gpt-5-5) <br>
- [Publisher profile](https://clawhub.ai/user/coolhackboy) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payloads and bash curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include synchronous or streaming response handling notes, system prompt constraints, and response parsing guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
