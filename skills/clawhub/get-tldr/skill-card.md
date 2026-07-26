## Description: <br>
Provide the summary returned by the get-tldr.com summarize API without further summarization; the skill should format the API output for readability but must not change its content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itobey](https://clawhub.ai/user/itobey) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to send a URL to the get-tldr.com summarize API and return the API-provided summary in readable Markdown without changing its content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends user-provided target URLs to get-tldr.com for summarization. <br>
Mitigation: Use it only for links that are appropriate to share with the external summarize API, especially when URLs contain private paths or query strings. <br>
Risk: The bundled script can store submitted URLs and returned summaries in a local logfile. <br>
Mitigation: Configure the logfile intentionally and clear or protect it when processed links or summaries may contain sensitive information. <br>
Risk: The skill requires a get-tldr API key stored in config, an environment variable, or a local .env file. <br>
Mitigation: Use a dedicated API key and keep config files, .env files, logs, and screenshots private. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/itobey/skills/get-tldr) <br>
- [Publisher profile](https://clawhub.ai/user/itobey) <br>
- [get-tldr summarize API endpoint](https://www.get-tldr.com/api/v1/summarize) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown-formatted API summary for the agent; the bundled script prints JSON responses or JSON error objects to stdout.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a get-tldr API key from config, environment, or a local .env file; submitted URLs and API responses may be written to a local logfile.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
