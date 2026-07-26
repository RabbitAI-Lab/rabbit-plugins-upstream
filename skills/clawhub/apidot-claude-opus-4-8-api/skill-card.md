## Description: <br>
Use APIDot for Claude Opus 4.8 API workflows, including Claude Messages, long-context reasoning, complex coding, long-horizon agents, adaptive thinking, streaming planning, tool-use planning, API key safety guidance, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this documentation-only skill to route Claude Opus 4.8 integration questions to APIDot docs, model pages, examples, and safe API key handling guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDOT_API_KEY could be exposed if copied into browser code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Keep APIDot API keys in server-side environment variables or a backend secret manager, and avoid displaying or logging them. <br>
Risk: APIDot model availability, request fields, limits, and commercial terms can change after the skill is released. <br>
Mitigation: Verify APIDot's current docs and model pages before making live API calls or committing integration details. <br>
Risk: Prompts, source documents, customer data, tool inputs, generated responses, usage records, and request IDs may contain sensitive information. <br>
Mitigation: Treat those values as sensitive unless the user explicitly says they can be shared, and keep private workflow data out of public logs. <br>


## Reference(s): <br>
- [APIDot Claude Opus 4.8 Reference](references/api.md) <br>
- [APIDot Docs](https://apidot.ai/docs) <br>
- [Claude Opus 4.8 Model Page](https://apidot.ai/models/claude-opus-4-8) <br>
- [Claude Opus 4.8 API Docs](https://apidot.ai/docs/claude-opus-4-8) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Error Guidance](https://apidot.ai/docs/errors) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration instructions, Markdown] <br>
**Output Format:** [Markdown text with links and structured integration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no executable files, automatic network calls, bundled API clients, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
