## Description: <br>
When the user requests "Call Google Videos" or "Video Search", or explicitly mentions the video field, the dataify-google-videos skill is triggered. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to prepare, preview, confirm, and submit Google Videos search requests to Dataify's Scraper API with documented parameters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries and selected parameters are sent to Dataify's Scraper API. <br>
Mitigation: Review the confirmation table before approving calls and avoid submitting sensitive search terms. <br>
Risk: The skill uses a Dataify API token for authenticated requests. <br>
Mitigation: Keep the token private, use the DATAIFY_API_TOKEN environment variable when possible, and do not echo token values in responses. <br>
Risk: Broad video-search phrasing may activate the skill. <br>
Mitigation: Confirm that the user intends a Google Videos API request before making any real API call. <br>


## Reference(s): <br>
- [Google Videos API Reference](references/google_videos_api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown confirmation table followed by the raw Dataify API response body after confirmation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit user confirmation before API calls and a Dataify API token.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
