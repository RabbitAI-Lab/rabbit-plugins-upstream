## Description: <br>
Gemini 3 Series chat on PoYo / poyo.ai via OpenAI-compatible chat completions and Gemini Native Format. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare PoYo Gemini 3 chat requests, choose between OpenAI-compatible and Gemini Native endpoints, and produce payloads or curl commands for server-side integrations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a PoYo API key for authenticated requests. <br>
Mitigation: Keep POYO_API_KEY in server-side environment variables or a backend secret manager, and avoid exposing it in browser code, logs, screenshots, repositories, or chat output. <br>
Risk: Live API calls can send prompts or payload data to an external service. <br>
Mitigation: Make live calls only when the user explicitly requests them and provides a trusted server-side environment. <br>
Risk: Future versions could request credentials, broad file access, or permission to modify external accounts. <br>
Mitigation: Confirm that any such requests are directly needed for the task before deployment or execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-gemini-3-api) <br>
- [PoYo Gemini 3 API model page](https://poyo.ai/models/gemini-3-api) <br>
- [PoYo chat completions documentation](https://docs.poyo.ai/api-manual/chat-series/chat-completions) <br>
- [PoYo Gemini Native Format documentation](https://docs.poyo.ai/api-manual/chat-series/gemini-native-format) <br>
- [API reference](artifact/references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON payload examples and bash/curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference POYO_API_KEY for server-side authentication; does not require live API calls unless explicitly requested.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
