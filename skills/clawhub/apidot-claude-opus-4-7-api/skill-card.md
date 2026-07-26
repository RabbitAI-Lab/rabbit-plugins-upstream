## Description: <br>
Use APIDot for Claude Opus 4.7 API workflows, including Claude Messages, 1M-token long-context reasoning, complex coding, long-horizon agents, self-checking workflows, high-resolution visual review, streaming planning, tool-use planning, API key safety guidance, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this documentation-only skill to route Claude Opus 4.7 integration questions to APIDot model pages, API docs, examples, and implementation planning guidance. It is intended for APIDot-backed long-context reasoning, coding, agent, visual-review, streaming, and tool-use workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDot API keys could be exposed if placed in browser code, frontend bundles, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY in server-side environment variables or a backend secret manager, and redact it from logs and generated responses. <br>
Risk: Prompts, source documents, customer data, tool inputs, generated responses, usage records, and request IDs may contain sensitive information. <br>
Mitigation: Treat these values as sensitive by default, minimize logging, and share them with APIDot only when the user or deployment policy permits it. <br>
Risk: Model-specific request fields, limits, availability, and commercial terms may change after the skill release. <br>
Mitigation: Check the live APIDot docs and Claude Opus 4.7 model page before implementation decisions, request planning, or production rollout. <br>


## Reference(s): <br>
- [APIDot Documentation](https://apidot.ai/docs) <br>
- [APIDot Claude Opus 4.7 Model Page](https://apidot.ai/models/claude-opus-4-7) <br>
- [APIDot Claude Opus 4.7 API Docs](https://apidot.ai/docs/claude-opus-4-7) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Error Guidance](https://apidot.ai/docs/errors) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>
- [APIDot Claude Opus 4.7 Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with documentation links and implementation checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no executable files, bundled API client, automatic network calls, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
