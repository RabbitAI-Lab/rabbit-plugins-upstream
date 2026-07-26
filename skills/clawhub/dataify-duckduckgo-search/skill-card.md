## Description: <br>
Searches DuckDuckGo through Dataify with parameter preview and user confirmation before API calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to run DuckDuckGo searches through the Dataify API after previewing request parameters and obtaining user confirmation. It is useful when a task needs DuckDuckGo results with explicit control over region, safe-search, date filtering, result count, cache use, and response format. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries and Dataify API tokens are third-party data when the confirmed API call runs. <br>
Mitigation: Review the preview before confirming the call, keep DATAIFY_API_TOKEN in the environment, and avoid pasting tokens into chat or command arguments. <br>
Risk: The skill returns API stdout directly to the user. <br>
Mitigation: Review returned content before relying on it or passing it into downstream workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-duckduckgo-search) <br>
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Text] <br>
**Output Format:** [Markdown parameter preview table and raw API response stdout] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a DuckDuckGo query and a Dataify API token for confirmed network calls; explicit command flags can override parsed request fields.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
