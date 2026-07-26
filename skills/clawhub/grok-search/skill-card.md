## Description: <br>
Search the web or X/Twitter using xAI Grok server-side tools (web_search, x_search) via the xAI Responses API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[notabhay](https://clawhub.ai/user/notabhay) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to run Grok-backed web and X searches, return structured JSON with citations, chat with Grok, inspect available models, and optionally analyze images through the xAI Responses API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries, prompts, and explicitly provided images are sent to xAI when the scripts are used. <br>
Mitigation: Avoid submitting secrets, private images, or sensitive prompts unless that transmission to xAI is intended. <br>
Risk: The skill requires an xAI API key and can use local ClawHub configuration as a credential source. <br>
Mitigation: Store XAI_API_KEY in the intended environment or ClawHub config location and limit access to that credential. <br>


## Reference(s): <br>
- [xAI Search tools](https://docs.x.ai/docs/guides/tools/search-tools) <br>
- [xAI Tools overview](https://docs.x.ai/docs/guides/tools/overview) <br>
- [xAI API reference](https://docs.x.ai/docs/api-reference) <br>
- [xAI tools quick links](artifact/references/xai-tools-links.md) <br>
- [ClawHub skill page](https://clawhub.ai/notabhay/skills/grok-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON search results with citations, plain text chat output, model lists, and Markdown usage guidance with shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results include query, mode, results, and citations; xAI API calls require Node.js and XAI_API_KEY.] <br>

## Skill Version(s): <br>
0.2.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
