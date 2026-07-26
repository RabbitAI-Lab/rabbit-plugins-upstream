## Description: <br>
Use APIDot for Claude 4.6 API workflows, including Claude Sonnet 4.6, Claude Opus 4.6, Messages API, chat completions, streaming, tool use planning, production chat, coding agents, API key safety guidance, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this documentation-only skill to route Claude 4.6 APIDot integration questions to the right model pages, API docs, request-planning guidance, and API key safety practices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys or private prompts could be exposed if copied into browser code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY and sensitive request data server-side in environment variables or a backend secret manager, and avoid logging secrets or private context. <br>
Risk: Outdated or guessed Claude 4.6 request fields could lead to incorrect integration guidance. <br>
Mitigation: Use current APIDot docs and model pages for model-specific request fields, availability, limits, and commercial terms. <br>
Risk: Live API calls could send data or incur usage unexpectedly. <br>
Mitigation: Do not make live API calls unless the user explicitly asks and provides a safe server-side environment. <br>


## Reference(s): <br>
- [APIDot Claude 4.6 Reference](references/api.md) <br>
- [APIDot Docs](https://apidot.ai/docs) <br>
- [APIDot Claude 4.6 Model Page](https://apidot.ai/models/claude-4-6) <br>
- [APIDot Claude 4.6 API Docs](https://apidot.ai/docs/claude-4-6) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Error Guidance](https://apidot.ai/docs/errors) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Configuration] <br>
**Output Format:** [Markdown guidance with reference links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no executable files, automatic network calls, bundled API clients, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
