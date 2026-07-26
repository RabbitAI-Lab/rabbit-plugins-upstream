## Description: <br>
Runs Bing video searches through the Dataify API after confirming the request parameters with the user. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to convert natural-language Bing video search requests into Dataify API parameters, confirm the full request table, and run the search with a user-provided Dataify API token. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Confirmed searches send the user's query and selected filters to Dataify. <br>
Mitigation: Review the full parameter table before confirming a live call and avoid sending sensitive search terms unless that disclosure is acceptable. <br>
Risk: Live calls require a Dataify API token that could be exposed if handled carelessly. <br>
Mitigation: Prefer passing the token for the current run unless intentionally storing DATAIFY_API_TOKEN as an environment variable. <br>


## Reference(s): <br>
- [Dataify Bing Videos API Reference](references/api.md) <br>
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-bing-videos) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Text, Shell commands] <br>
**Output Format:** [Markdown confirmation table followed by the raw Dataify API response, usually JSON or HTML when requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Live API calls require user confirmation and a DATAIFY_API_TOKEN before search parameters are sent to Dataify.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
