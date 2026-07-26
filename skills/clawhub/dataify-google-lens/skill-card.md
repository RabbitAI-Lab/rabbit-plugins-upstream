## Description: <br>
Turns a user's Google Lens or reverse-image-search request into a confirmed Dataify Scraper API form submission. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to convert Google Lens or reverse-image-search requests into confirmed Dataify API calls and receive the raw response body. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Image URLs and selected search parameters are sent to Dataify for reverse image search. <br>
Mitigation: Review the pre-call parameter table and approve only intended values before the API call. <br>
Risk: DATAIFY_API_TOKEN authorizes the Dataify request. <br>
Mitigation: Do not include Authorization in previews or final user-facing output; stop and ask the user to obtain a token if it is missing. <br>


## Reference(s): <br>
- [Dataify Google Lens API Reference](references/google_lens_api.md) <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-google-lens) <br>
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify Scraper API endpoint](https://scraperapi.dataify.com/request) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, API calls, Text] <br>
**Output Format:** [Markdown confirmation table followed by raw API response text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user confirmation before API calls and DATAIFY_API_TOKEN for authorization.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
