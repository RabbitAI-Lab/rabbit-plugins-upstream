## Description: <br>
Dataify Google Images turns a user's Google Images request into a Dataify Scraper API form submission after parameter confirmation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to prepare, confirm, and execute Google Images searches through Dataify's Scraper API while preserving the raw API response. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search parameters and request details are sent to Dataify when the API call is confirmed. <br>
Mitigation: Confirm the user is comfortable sending the selected parameters to Dataify before making the request. <br>
Risk: The skill requires a DATAIFY_API_TOKEN for authenticated API access. <br>
Mitigation: Keep the token out of displayed parameter tables and avoid echoing token values in responses. <br>
Risk: Raw upstream API responses or errors may include query and request details. <br>
Mitigation: Review raw API responses before sharing them further. <br>


## Reference(s): <br>
- [Dataify Google Images API Reference](references/google_images_api.md) <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-google-images) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown confirmation table followed by the raw API response body after explicit user confirmation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Dataify API token and sends confirmed search parameters to Dataify.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
