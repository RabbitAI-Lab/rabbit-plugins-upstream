## Description: <br>
Use APIDot for Gemini 3.5 Flash API workflows, including stable Gemini Native generateContent, streamGenerateContent, long-context chat, coding iteration, knowledge-base Q&A, streaming planning, usage tracking, API key safety guidance, and APIDot docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to route Gemini 3.5 Flash integration work through APIDot documentation, model pages, request planning guidance, and API-key safety practices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDOT_API_KEY may be exposed if an agent places it in browser code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Keep the key in server-side environment variables or a backend secret manager, and avoid echoing secrets in generated code or operational output. <br>
Risk: Live API calls may be made when the user only intended documentation or planning help. <br>
Mitigation: Only allow live APIDot calls when the user explicitly requests them and provides a safe server-side environment. <br>
Risk: Model-specific request fields or commercial details may become outdated. <br>
Mitigation: Use the current APIDot model page and API documentation as the source of truth before preparing payloads or making product claims. <br>


## Reference(s): <br>
- [APIDot documentation](https://apidot.ai/docs) <br>
- [APIDot Gemini 3.5 Flash model page](https://apidot.ai/models/gemini-3-5-flash) <br>
- [APIDot Gemini 3.5 Flash API docs](https://apidot.ai/docs/gemini-3-5-flash) <br>
- [APIDot quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot error guidance](https://apidot.ai/docs/errors) <br>
- [APIDot examples](https://github.com/APIDotAI/apidot-examples) <br>
- [APIDot Gemini 3.5 Flash Reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/jiehao71727/skills/apidot-gemini-3-5-flash-api) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, configuration] <br>
**Output Format:** [Markdown guidance with links, integration notes, configuration advice, and code-oriented recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no bundled executable code, hidden automation, network calls, or stored credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
