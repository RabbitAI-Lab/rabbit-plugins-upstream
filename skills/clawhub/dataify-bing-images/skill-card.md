## Description: <br>
Dataify Bing Images turns natural-language Bing image search requests into confirmed Dataify API calls and returns the API response. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to prepare Bing image search parameters, review them before execution, and call Dataify's Bing Images API after confirmation. It is useful when an agent needs image search results with filters such as market, region, size, color, layout, date, or license. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms and selected request parameters are sent to Dataify for live Bing image search calls. <br>
Mitigation: Use the required preview step to inspect the complete parameter table before confirming a live API call. <br>
Risk: A Dataify API token is required for live calls and could be exposed if handled carelessly. <br>
Mitigation: Provide the token only when the Dataify service is trusted, avoid displaying Authorization values, and prefer per-run token use when persistent shell storage is not desired. <br>
Risk: The skill returns Dataify API responses directly, including JSON strings or HTML when requested. <br>
Mitigation: Review returned content before using it in downstream workflows, especially when HTML output is requested. <br>


## Reference(s): <br>
- [Dataify Bing Images API Reference](artifact/references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-bing-images) <br>
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, HTML, shell commands, guidance] <br>
**Output Format:** [Markdown parameter preview and raw Dataify API response, usually JSON and optionally HTML.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Live API calls require user confirmation and a Dataify API token; responses are returned without post-processing.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
