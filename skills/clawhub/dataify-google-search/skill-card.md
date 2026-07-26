## Description: <br>
Dataify Google Search turns a user's Google search request into a confirmed Dataify Scraper API call and returns the raw response body. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to map natural-language Google search requests into Dataify Scraper API parameters, confirm the request, and retrieve Google SERP results through Dataify. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends confirmed search parameters to Dataify using a DATAIFY_API_TOKEN. <br>
Mitigation: Review the confirmation table before approving a call, store the token as a secret, and avoid pasting it into shared logs or transcripts. <br>
Risk: Incorrect inferred search parameters could produce unintended Google search requests. <br>
Mitigation: Use the required pre-call confirmation step and regenerate the parameter table after any user changes. <br>


## Reference(s): <br>
- [Dataify Google Search API Reference](references/google_search_api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-google-search) <br>
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance] <br>
**Output Format:** [Markdown confirmation table, shell command guidance, and raw API response body] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user confirmation before API calls and returns the Dataify response without summarizing or reshaping it.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
