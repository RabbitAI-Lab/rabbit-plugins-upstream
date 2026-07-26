## Description: <br>
Queries and analyzes recent Google Trends hot searches for a selected time window and supported country or region. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and commerce or content teams use this skill to discover recent Google search trends, breakout topics, and regional hot searches across supported markets. <br>

### Deployment Geography for Use: <br>
Global; trend queries are limited to the 18 supported regions listed in the skill. <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes external Google Trends and LinkFox API calls using an API key from the environment. <br>
Mitigation: Install and run it only when those external calls are expected, keep the API key scoped to this use, and confirm the region and time window before paid queries. <br>
Risk: The security summary notes that the skill stores and transmits more session-linked data than users may expect. <br>
Mitigation: Review or disable feedback submission where appropriate, avoid sensitive trend queries, and periodically delete saved local response artifacts that are no longer needed. <br>
Risk: Repeated queries can consume LinkFox credits. <br>
Mitigation: Tell users before repeated calls and rely on the built-in same-parameter cache when the prior result is still suitable. <br>


## Reference(s): <br>
- [API reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-google-trend-get-trend-by-time) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON files] <br>
**Output Format:** [Markdown guidance with JSON examples, stdout summaries, and saved JSON API responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a LinkFox API key, consumes credits per query, supports days and region parameters, caches matching requests for 24 hours, and saves full responses locally.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
