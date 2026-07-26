## Description: <br>
Dataify Google Finance turns a user's Google Finance request into a confirmed Dataify Scraper API form POST. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to prepare and confirm Google Finance lookup parameters before querying Dataify's scraper API for stocks, indices, funds, currencies, or futures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Google Finance query parameters and the Dataify API token are sent to scraperapi.dataify.com after confirmation. <br>
Mitigation: Review the preview table before confirming, use the skill only in trusted environments, and avoid pasting tokens unless necessary. <br>
Risk: Incorrect or unintended financial query parameters can produce irrelevant API results. <br>
Mitigation: Confirm or modify q, json, hl, window, and no_cache values in the preview table before any API call. <br>


## Reference(s): <br>
- [Dataify Google Finance API reference](references/google_finance_api.md) <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-google-finance) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, API response body, guidance] <br>
**Output Format:** [Markdown confirmation tables, shell commands, and raw Dataify API response bodies.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user confirmation before API calls and returns the response body without summarizing or reshaping it.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
