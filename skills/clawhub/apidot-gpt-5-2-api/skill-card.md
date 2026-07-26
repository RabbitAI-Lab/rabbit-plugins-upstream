## Description: <br>
Use APIDot for GPT 5.2 API workflows, including OpenAI-compatible chat, legacy professional-work compatibility, 400K-token long-context synthesis, agentic coding handoffs, chart reasoning, streaming planning, usage tracking, API key safety guidance, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical agents use this skill to route GPT 5.2 integration questions to APIDot documentation, model pages, examples, and safety guidance. It supports planning chat request handling, streaming behavior, usage tracking, long-context synthesis, chart reasoning, and coding handoff workflows without making live API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDot API keys, prompts, customer data, usage records, or request IDs could be exposed during implementation work. <br>
Mitigation: Keep APIDOT_API_KEY server-side, avoid public logs and frontend bundles, and treat prompts, private documents, generated responses, and usage metadata as sensitive. <br>
Risk: Model-specific request fields, availability, limits, or commercial terms may be outdated if copied from the local skill notes. <br>
Mitigation: Verify current API details in APIDot's live docs and model pages before implementing real calls. <br>
Risk: Live API calls could send sensitive data or use an unsafe credential environment. <br>
Mitigation: Make live calls only when explicitly requested and only from a safe server-side environment. <br>


## Reference(s): <br>
- [APIDot GPT 5.2 Reference](references/api.md) <br>
- [APIDot Docs](https://apidot.ai/docs) <br>
- [APIDot GPT 5.2 Model Page](https://apidot.ai/models/gpt-5-2) <br>
- [APIDot GPT 5.2 Docs](https://apidot.ai/docs/gpt-5-2) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Error Guidance](https://apidot.ai/docs/errors) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown guidance with reference links and integration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only output; no executable code, stored credentials, or automatic network calls.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
