## Description: <br>
When the user requests "call Google Local" or "local search/nearby search/place search", or explicitly mentions the local search field, the dataify-google-local skill is triggered. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to convert Google Local or nearby-place search requests into confirmed Dataify Scraper API calls. It helps preview request parameters, collect missing required input, and return the API response body after explicit user confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends Google Local search parameters to Dataify and requires an API token. <br>
Mitigation: Provide the token only through the documented token flow or DATAIFY_API_TOKEN, and review the parameter preview before confirming any call. <br>
Risk: Generic local-search wording may trigger the skill for broad nearby-place requests. <br>
Mitigation: Confirm that Dataify Google Local is the intended provider before approving the API call. <br>


## Reference(s): <br>
- [Dataify Google Local API](artifact/references/google_local_api.md) <br>
- [Dataify Scraper API endpoint](https://scraperapi.dataify.com/request) <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-google-local) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown parameter previews, shell command examples, and raw API response bodies.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit user confirmation and a Dataify API token before sending requests.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
