## Description: <br>
Use APIDot for GPT 5.5 API workflows, including OpenAI-compatible chat, long-horizon agentic execution, complex coding, research synthesis, document analysis, streaming planning, usage tracking, API key safety guidance, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to route APIDot GPT 5.5 integration questions to the right docs, model page, request-planning guidance, and API key safety practices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys or private prompts could be exposed if copied into public code, logs, screenshots, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY and sensitive request data in a server-side environment or secret manager, and avoid logging private prompts, documents, customer data, tool inputs, generated responses, usage records, and request IDs. <br>
Risk: APIDot GPT 5.5 request fields, availability, limits, or commercial terms may be misapplied if stale or guessed guidance is used. <br>
Mitigation: Confirm model-specific details against the current APIDot docs and model page before preparing requests or making product claims. <br>
Risk: A live API call could send data to APIDot before the user has confirmed the intended environment and data handling. <br>
Mitigation: Use this skill as documentation guidance by default and make live API calls only after the user explicitly asks and provides a safe server-side environment. <br>


## Reference(s): <br>
- [APIDot GPT 5.5 Reference](references/api.md) <br>
- [APIDot Docs](https://apidot.ai/docs) <br>
- [APIDot GPT 5.5 Model Page](https://apidot.ai/models/gpt-5-5) <br>
- [APIDot GPT 5.5 API Docs](https://apidot.ai/docs/gpt-5-5) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Error Guidance](https://apidot.ai/docs/errors) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>
- [ClawHub Skill Page](https://clawhub.ai/jiehao71727/skills/apidot-gpt-5-5-api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with links, checklists, and routing notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no executable code, automatic network calls, bundled API clients, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
