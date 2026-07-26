## Description: <br>
Turns Google Hotels search requests into confirmed Dataify Scraper API form POSTs and returns the raw API response body. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to prepare and run Google Hotels searches through Dataify after reviewing a parameter table and confirming a live request. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Hotel search details and the Dataify API token are sent to Dataify during live requests. <br>
Mitigation: Review the confirmation table before approving each live request and set DATAIFY_API_TOKEN only in environments you control. <br>
Risk: Incorrect or incomplete parameters can produce unintended hotel searches. <br>
Mitigation: Use only documented defaults, ask for missing required values, and regenerate the confirmation table after changes. <br>
Risk: The skill returns the raw API response body without filtering or summarizing it. <br>
Mitigation: Review the raw response before relying on prices, availability, or downstream use. <br>


## Reference(s): <br>
- [Dataify Google Hotels API](references/google_hotels_api.md) <br>
- [Dataify Scraper API endpoint](https://scraperapi.dataify.com/request) <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-google-hotels) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Text, Guidance] <br>
**Output Format:** [Markdown parameter table, inline shell commands, and raw API response text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user confirmation before live requests and returns the API response body directly.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
