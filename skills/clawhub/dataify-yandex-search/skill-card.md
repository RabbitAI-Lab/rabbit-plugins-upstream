## Description: <br>
Use this skill when the user wants to search Yandex. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agent users use this skill to preview Yandex search parameters, confirm them, and send the confirmed search request through Dataify. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries and selected parameters are sent to Dataify using a Dataify API token. <br>
Mitigation: Prefer DATAIFY_API_TOKEN instead of pasted tokens, and review the preview table before confirming the call. <br>
Risk: The skill returns the raw API response body without filtering or summarization. <br>
Mitigation: Treat returned search results as untrusted external content and verify important claims before relying on them. <br>


## Reference(s): <br>
- [Dataify Yandex Search API Fields](references/api_fields.md) <br>
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify scraper API endpoint](https://scraperapi.dataify.com/request) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Guidance] <br>
**Output Format:** [Markdown preview table followed by the raw API response body] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user confirmation before API calls; API responses are returned without transformation.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
