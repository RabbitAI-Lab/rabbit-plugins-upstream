## Description: <br>
Use APIDot for DeepSeek V4 Flash API workflows, including OpenAI-compatible chat, 1M-token long-context reasoning, fast non-thinking responses, prompt-guided reasoning, code review, agent planning, streaming planning, usage tracking, API key safety guidance, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agents use this skill to find APIDot DeepSeek V4 Flash documentation and plan safe OpenAI-compatible chat integrations, including request planning, streaming behavior, usage tracking, model routing, and API key handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDot API keys or private prompts could be exposed if copied into browser code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY in a server-side secret store and avoid logging API keys, private prompts, customer data, documents, tool inputs, generated responses, usage records, and request IDs unless explicitly intended. <br>
Risk: Model availability, request fields, limits, pricing, and commercial terms may change after the skill is installed. <br>
Mitigation: Verify the current APIDot model page, documentation, and pricing before implementation decisions, planning requests, or production rollout. <br>
Risk: Users could treat the documentation router as an executable integration or assume it performs live API validation. <br>
Mitigation: Use it as non-executable guidance only; validate request shapes against current APIDot docs and make live API calls only from a safe server-side environment when explicitly requested. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jiehao71727/skills/apidot-deepseek-v4-flash-api) <br>
- [APIDot documentation](https://apidot.ai/docs) <br>
- [APIDot DeepSeek V4 Flash model page](https://apidot.ai/models/deepseek-v4-flash) <br>
- [APIDot DeepSeek V4 Flash API docs](https://apidot.ai/docs/deepseek-v4-flash) <br>
- [APIDot quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with links, planning notes, and API-key handling guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no executable code, network calls, bundled clients, or credential storage.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
