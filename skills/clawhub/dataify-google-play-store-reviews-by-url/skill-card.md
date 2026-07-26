## Description: <br>
Prepares Dataify builder requests for the play.google.com scraper family rooted at google-play-store_reviews_by-url, including tool selection, saved parameter lookup, and generation of a DATAIFY_API_TOKEN-authenticated builder curl request. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to prepare Dataify scraper API builder requests for Google Play Store review or information URL tools without hand-building form-urlencoded payloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated commands use DATAIFY_API_TOKEN for outbound requests to Dataify's scraper API. <br>
Mitigation: Treat DATAIFY_API_TOKEN as a secret, avoid storing it in synced dotfiles or shared-machine profiles, and review generated curl commands before running them. <br>
Risk: Scraper parameters may contain sensitive URLs or identifiers. <br>
Mitigation: Avoid sending sensitive URLs or identifiers as scraper parameters unless they are necessary for the intended Dataify request. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-google-play-store-reviews-by-url) <br>
- [Tool parameter catalog](references/tool-params.json) <br>
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify builder endpoint](https://scraperapi.dataify.com/builder) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with curl command blocks and environment-variable setup instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Builds form-urlencoded Dataify builder requests using user-selected tool signs and JSON spider_parameters.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
