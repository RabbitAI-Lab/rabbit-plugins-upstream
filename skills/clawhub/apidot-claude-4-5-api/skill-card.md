## Description: <br>
Routes Claude 4.5 API integration questions to APIDot documentation, model pages, reference notes, and safe implementation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to plan Claude 4.5 integrations on APIDot, including model selection, Messages-style workflows, streaming, tool use, and API-key handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys, prompts, private context, or generated responses could be exposed if copied into frontend code, public logs, screenshots, repositories, or chat output. <br>
Mitigation: Keep APIDot API keys in server-side environment variables or a backend secret manager, and keep sensitive prompts, context, tool inputs, and responses out of public logs. <br>
Risk: Model names, request fields, limits, or commercial terms may change after the skill release. <br>
Mitigation: Verify live APIDot documentation and model pages before preparing production payloads or making current product claims. <br>
Risk: Live API calls could be made from an unsafe environment if users skip credential and backend checks. <br>
Mitigation: Make live APIDot API calls only when the user explicitly asks and provides a safe server-side environment. <br>


## Reference(s): <br>
- [APIDot Docs](https://apidot.ai/docs) <br>
- [APIDot Claude 4.5 Model Page](https://apidot.ai/models/claude-4-5) <br>
- [APIDot Claude 4.5 Docs](https://apidot.ai/docs/claude-4-5) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Error Guidance](https://apidot.ai/docs/errors) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>
- [APIDot Claude 4.5 Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown guidance with links and concise implementation notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no executable files, bundled API clients, automatic network calls, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
