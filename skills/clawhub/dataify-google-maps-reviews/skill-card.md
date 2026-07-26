## Description: <br>
Collect Google Maps review and comment information from Google Maps URLs through the Dataify Scraper API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to create Dataify collection tasks for Google Maps reviews, preview request parameters, and submit confirmed collection jobs by URL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends Google Maps URLs and collection parameters to the external Dataify service. <br>
Mitigation: Install only if this data sharing is acceptable, and review the Markdown confirmation table before approving each API call. <br>
Risk: A Dataify API token is required and may be provided interactively or through DATAIFY_API_TOKEN. <br>
Mitigation: Use a scoped token where possible, never paste tokens into shared logs, and avoid permanent environment-variable storage on shared machines. <br>
Risk: The skill can create external collection tasks through Dataify. <br>
Mitigation: Confirm parameters before submission and review task status in the official Dataify dashboard after creation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-google-maps-reviews) <br>
- [Publisher profile](https://clawhub.ai/user/dataify-server) <br>
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify login](https://dashboard.dataify.com/login?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown confirmation tables, shell commands, and JSON API responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and a Dataify API token; submits Google Maps URLs and collection parameters to Dataify after user confirmation.] <br>

## Skill Version(s): <br>
1.2.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
