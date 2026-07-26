## Description: <br>
Web search via EvoLink API that returns formatted result titles, URLs, and descriptions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[evolinkai](https://clawhub.ai/user/evolinkai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and agents can use this skill to perform current web searches and gather result URLs and short descriptions through the EvoLink API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms are sent to EvoLink for processing. <br>
Mitigation: Avoid searching for secrets, credentials, or sensitive private data. <br>
Risk: Returned snippets and URLs are untrusted web content. <br>
Mitigation: Treat results as research leads and verify important claims before relying on them. <br>
Risk: The skill requires an EvoLink API key. <br>
Mitigation: Store EVOLINK_API_KEY securely and avoid exposing it in prompts, logs, command history, or shared outputs. <br>


## Reference(s): <br>
- [ClawHub Skill Release](https://clawhub.ai/evolinkai/web-research) <br>
- [EvoLink API Reference](https://docs.evolink.ai/en/api-manual/language-series/claude/claude-messages-api?utm_source=clawhub&utm_medium=skill&utm_campaign=web-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text containing shell command examples and formatted search results with titles, URLs, and descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires bash, curl, jq, network access to api.evolink.ai, and EVOLINK_API_KEY.] <br>

## Skill Version(s): <br>
v3.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
