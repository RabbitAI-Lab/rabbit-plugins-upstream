## Description: <br>
Analyzes Amazon keyword traffic for competing ASINs by organic search, Sponsored Products, brand ads, video ads, recommendation placements, and AC/ER/TR exposure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers, marketplace analysts, and agent users use this skill to query LinkFox SIF keyword traffic data and compare how competing ASINs receive keyword exposure across organic, paid, and recommendation channels. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends keyword, marketplace, session, and related request data to external LinkFox services. <br>
Mitigation: Verify the configured LinkFox gateway URL and API key handling before use, and avoid submitting sensitive keywords or ASIN sets unless external processing is acceptable. <br>
Risk: The helper script writes complete API responses and cache files locally, which may preserve marketplace research data beyond the conversation. <br>
Mitigation: Run it from an approved workspace, review the linkfox output directory, and remove cached or saved responses when retention is not desired. <br>
Risk: The artifact includes automatic feedback reporting guidance that can send session or feedback-related data to a LinkFox feedback API. <br>
Mitigation: Review or disable feedback behavior where the runtime permits, especially for private workflows or regulated data. <br>
Risk: API calls consume LinkFox credits, and repeated pagination or changed parameters can increase cost. <br>
Mitigation: Confirm user intent before additional calls, use the built-in 24-hour cache when appropriate, and avoid exploratory retries after failures or empty results. <br>


## Reference(s): <br>
- [SIF keyword traffic API reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-sif-keyword-summary) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, API Calls, JSON, Markdown, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown summaries and tables, JSON API responses, shell commands, and saved JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes full API responses to a local linkfox session data directory; large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
