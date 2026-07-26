## Description: <br>
Collect Booking hotel information through Dataify Scraper API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to preview parameters, confirm required Booking URLs, and create Dataify collection tasks for Booking hotel listings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Dataify API token and may save DATAIFY_API_TOKEN in the local environment. <br>
Mitigation: Confirm token handling before each run, never echo the token, and save it persistently only after explicit user consent. <br>
Risk: The skill creates Booking hotel collection tasks through Dataify after parameter confirmation. <br>
Mitigation: Review the Markdown confirmation table and verify all Booking URLs and task parameters before making the API call. <br>


## Reference(s): <br>
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-booking-hotellist) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown confirmation tables with inline shell commands and task status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Booking URL and a Dataify API token; can submit one or more spider parameter sets after confirmation.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
