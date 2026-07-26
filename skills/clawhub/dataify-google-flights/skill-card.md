## Description: <br>
When the user requests "calling Google Flights" or "searching for flight prices/itineraries", or explicitly mentions the flight query field, the dataify-google-flights skill is triggered. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to turn Google Flights search requests into confirmed Dataify Scraper API calls for flight prices and itineraries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Confirmed flight-search details are sent to Dataify. <br>
Mitigation: Review the confirmation table carefully before approving an API call. <br>
Risk: The skill requires a Dataify API token. <br>
Mitigation: Store the token in a secure environment or secret manager instead of pasting it into commands. <br>


## Reference(s): <br>
- [Dataify Google Flights API Reference](references/google_flights_api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-google-flights) <br>
- [Dataify Scraper API Endpoint](https://scraperapi.dataify.com/request) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, API calls, Guidance] <br>
**Output Format:** [Markdown confirmation table, inline shell commands, and raw API response body] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit user confirmation before API calls and returns the API response without reshaping it.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
