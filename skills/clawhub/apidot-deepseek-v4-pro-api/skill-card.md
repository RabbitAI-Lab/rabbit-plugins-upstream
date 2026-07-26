## Description: <br>
Use APIDot for DeepSeek V4 Pro API workflows, including OpenAI-compatible chat, 1M-token long-context reasoning, complex coding, document review, agent planning, streaming planning, usage tracking, API key safety guidance, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to find APIDot DeepSeek V4 Pro documentation and plan safe OpenAI-compatible chat integrations, long-context reasoning workflows, usage tracking, and API key handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys or private prompts may be exposed if copied into browser code, public logs, repositories, screenshots, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY and sensitive request data server-side, preferably in environment variables or a backend secret manager. <br>
Risk: Live APIDot API calls could send private prompts, documents, customer data, or generated responses to an external service. <br>
Mitigation: Only make live API calls when the user explicitly asks and provides a safe backend environment. <br>
Risk: Outdated or guessed model fields could produce incorrect integration guidance. <br>
Mitigation: Use the current APIDot docs and model page for supported request fields, limits, response wrappers, availability, and commercial terms. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jiehao71727/skills/apidot-deepseek-v4-pro-api) <br>
- [APIDot documentation](https://apidot.ai/docs) <br>
- [APIDot DeepSeek V4 Pro model page](https://apidot.ai/models/deepseek-v4-pro) <br>
- [APIDot DeepSeek V4 Pro API docs](https://apidot.ai/docs/deepseek-v4-pro) <br>
- [APIDot examples](https://github.com/APIDotAI/apidot-examples) <br>
- [APIDot DeepSeek V4 Pro Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with links, integration notes, and optional code-oriented planning] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; produces routing and integration guidance without executing API calls.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
