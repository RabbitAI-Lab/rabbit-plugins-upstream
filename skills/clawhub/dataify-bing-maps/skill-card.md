## Description: <br>
Dataify Bing Maps converts natural-language Bing Maps search requests into Dataify API calls and returns the API response directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to search Bing Maps for locations or map results through Dataify, with parameter review before live API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bing Maps search terms and optional location parameters are sent to Dataify with a Dataify API token. <br>
Mitigation: Review the generated confirmation table before approving a live call, especially when a request contains precise addresses or coordinates. <br>
Risk: A live external API call could run with unintended parameters. <br>
Mitigation: Use dry-run or parameter-table mode to inspect parsed fields, and run live calls only after explicit confirmation. <br>


## Reference(s): <br>
- [Dataify Bing Maps API Reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-bing-maps) <br>
- [Dataify Bing Maps API endpoint](https://scraperapi.dataify.com/request) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands] <br>
**Output Format:** [Markdown confirmation tables, shell command invocations, and direct Dataify API response text, JSON, or HTML] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Live calls require a Dataify API token and explicit user confirmation; API responses are returned without summarizing or post-processing.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
