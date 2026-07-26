## Description: <br>
Turns a user's Bing News request into Dataify Bing News API parameters, previews the request for confirmation, and returns the confirmed API response directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to run confirmed Bing News searches through the Dataify/ScraperAPI endpoint. It is useful when a user wants raw Bing News API results after reviewing request parameters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Dataify API tokens could be exposed if shared in prompts, logs, or copied output. <br>
Mitigation: Prefer the DATAIFY_API_TOKEN environment variable or an explicit token parameter for the current run, and avoid displaying Authorization values. <br>
Risk: News search terms and request parameters are sent to Dataify/ScraperAPI. <br>
Mitigation: Avoid confidential or unrelated secret text in search prompts and confirm the full parameter table before calling the API. <br>
Risk: Raw API output may contain unreviewed JSON or HTML returned by the service. <br>
Mitigation: Review raw API output before sharing it elsewhere or using it in downstream workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-bing-news) <br>
- [Publisher profile](https://clawhub.ai/user/dataify-server) <br>
- [Dataify Bing News API Reference](references/api.md) <br>
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, HTML, Shell commands, Guidance] <br>
**Output Format:** [Markdown parameter preview tables, shell commands, and raw API response text that may contain JSON or HTML] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user confirmation before live API calls; raw API output is returned without summarizing or reformatting.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
