## Description: <br>
Dataify Google Shopping converts a user's shopping search or price-comparison request into a confirmed Dataify Scraper API call for Google Shopping. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to run Google Shopping product searches, price comparisons, and filter queries through Dataify after reviewing and confirming the request parameters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Confirmed shopping queries, filters, and the Dataify API token are sent to Dataify when an API call is made. <br>
Mitigation: Review the confirmation table before approving each call and use a token scoped to the Dataify service. <br>
Risk: Credentials can be exposed if the API token is pasted into unrelated chats or echoed in responses. <br>
Mitigation: Provide the token only for this service, prefer the DATAIFY_API_TOKEN environment variable, and keep token values masked in previews and final responses. <br>


## Reference(s): <br>
- [Dataify Google Shopping API Reference](references/google_shopping_api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, API Calls, Text] <br>
**Output Format:** [Markdown confirmation table followed by the raw API response body, which may be JSON, JSON+HTML, HTML, or Light JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Dataify API token; token values are masked in previews and the API response is returned without reshaping.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
