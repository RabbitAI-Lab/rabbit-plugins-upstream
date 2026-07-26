## Description: <br>
PoYo GPT-5.6 Responses API integration for selecting GPT-5.6 model variants, preparing request payloads, configuring tools and reasoning, handling streaming, and continuing server-side response workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare and submit PoYo GPT-5.6 Responses API requests, including model selection, request payloads, streaming behavior, tool settings, and response parsing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API keys could be exposed if copied into browser code, logs, screenshots, public repositories, or chat output. <br>
Mitigation: Keep POYO_API_KEY in server-side environment variables or a backend secret manager and avoid logging authorization headers. <br>
Risk: Private prompts, tool arguments, media, or request bodies could be sent to PoYo or retained in application logs. <br>
Mitigation: Review payloads before submission and send sensitive data only when organizational policy allows it. <br>
Risk: Returned tool calls or prepared helper-script payloads could perform unintended actions if executed without review. <br>
Mitigation: Execute tool calls only through an application-controlled allowlist with validated arguments, and use the helper script only from a trusted shell after reviewing the JSON payload. <br>


## Reference(s): <br>
- [PoYo GPT-5.6 model page](https://poyo.ai/models/gpt-5-6) <br>
- [PoYo Responses API documentation](https://docs.poyo.ai/api-manual/chat-series/responses) <br>
- [PoYo API key page](https://poyo.ai/dashboard/api-key) <br>
- [PoYo GPT-5.6 Responses API Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with JSON payloads and bash/curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include exact model IDs, request fields, streaming handling, response parsing notes, and server-side API key guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
