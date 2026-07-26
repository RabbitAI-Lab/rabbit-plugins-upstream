## Description: <br>
Use Exa Search API to search the web and return structured results including title, URL, snippet, and optional page text through a local Node script. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xinhai-ai](https://clawhub.ai/user/xinhai-ai) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill when they need Exa-backed web search, structured search results, optional page text retrieval, or date-filtered search results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to Exa when the script is invoked. <br>
Mitigation: Do not include secrets, credentials, private business data, or regulated personal information in searches. <br>
Risk: The skill requires an Exa API key in the environment. <br>
Mitigation: Provide EXA_API_KEY through the agent runtime or local environment and avoid exposing it in prompts, command history, or shared logs. <br>
Risk: Optional page text retrieval can return larger third-party web content than snippet-only search. <br>
Mitigation: Use the text option only when full page content is needed and review returned content before relying on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xinhai-ai/skills/exa-search) <br>
- [Exa documentation](https://exa.ai/docs) <br>
- [Exa Search API endpoint](https://api.exa.ai/search) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples; the bundled script returns JSON from the Exa API.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node and EXA_API_KEY; supports count, text, highlights, type, start date, and end date options.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
