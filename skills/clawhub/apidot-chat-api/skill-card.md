## Description: <br>
Use APIDot for chat API workflows, including OpenAI-compatible chat completions, coding assistants, reasoning models, multimodal assistant routing, streaming planning, server-side API key safety, and APIDot chat model docs routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiehao71727](https://clawhub.ai/user/jiehao71727) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to route APIDot chat API questions to current APIDot docs, model pages, examples, and safe integration guidance. It supports planning chat completions, coding assistant, reasoning, multimodal, streaming, and API-key handling workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APIDot API keys or private prompts could be exposed if copied into browser code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Keep APIDOT_API_KEY, system prompts, private messages, transcripts, and logs in server-side environment variables, backend secret managers, or approved secure storage. <br>
Risk: Model availability, request fields, or APIDot product details may change over time. <br>
Mitigation: Verify the current APIDot docs and live model pages before relying on model-specific behavior or routing. <br>
Risk: Live API calls could use unsafe credentials or unapproved environments. <br>
Mitigation: Make live APIDot API calls only when the user explicitly requests them and provides a safe server-side environment. <br>


## Reference(s): <br>
- [APIDot API Docs](https://apidot.ai/docs) <br>
- [APIDot Chat Models](https://apidot.ai/models/chat) <br>
- [APIDot Quickstart](https://apidot.ai/docs/quickstart) <br>
- [APIDot Examples](https://github.com/APIDotAI/apidot-examples) <br>
- [APIDot GitHub Organization](https://github.com/APIDotAI) <br>
- [ClawHub Skill Page](https://clawhub.ai/jiehao71727/skills/apidot-chat-api) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, configuration] <br>
**Output Format:** [Markdown guidance with links and inline configuration or code snippets when needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no executable files, automatic network calls, or credential storage.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
