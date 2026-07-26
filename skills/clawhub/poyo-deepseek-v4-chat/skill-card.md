## Description: <br>
Poyo Deepseek V4 Chat helps agents prepare PoYo DeepSeek V4 chat completion requests with Flash or Pro model IDs, OpenAI-compatible payloads, streaming choices, and server-side API-key handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to prepare PoYo DeepSeek V4 chat payloads, curl requests, and integration guidance for text generation, coding assistance, reasoning, summarization, and long-context assistant workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends prompts and chat payloads to PoYo's chat-completions API. <br>
Mitigation: Use it only for explicit PoYo or DeepSeek requests, and avoid sending sensitive prompts unless sharing them with PoYo is acceptable. <br>
Risk: The skill requires POYO_API_KEY for authenticated requests. <br>
Mitigation: Keep POYO_API_KEY server-side in environment variables or a backend secret manager, and do not expose it in browser code, public repositories, logs, screenshots, or chat output. <br>
Risk: The bundled shell script can submit a prepared payload to the external PoYo endpoint. <br>
Mitigation: Run it only from a trusted shell with a reviewed payload and a safe server-side environment. <br>


## Reference(s): <br>
- [PoYo DeepSeek V4 Flash model page](https://poyo.ai/models/deepseek-v4-flash) <br>
- [PoYo DeepSeek V4 Pro model page](https://poyo.ai/models/deepseek-v4-pro) <br>
- [PoYo chat completions API docs](https://docs.poyo.ai/api-manual/chat-series/chat-completions) <br>
- [PoYo API key page](https://poyo.ai/dashboard/api-key) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-deepseek-v4-chat) <br>
- [Publisher profile](https://clawhub.ai/user/coolhackboy) <br>
- [Local API reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payloads and bash curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model selection, synchronous or streaming handling, system prompt constraints, response parsing notes, and server-side API-key guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
