## Description: <br>
Collects Indeed company information by creating Dataify Scraper API tasks from a company list URL, keyword, industry and state, or company URL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to configure and submit Indeed company-information collection jobs through Dataify. It helps confirm parameters, handle Dataify API token setup, and report the created task ID or status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Dataify API token and can optionally save it as DATAIFY_API_TOKEN. <br>
Mitigation: Treat the token as a secret, do not echo it in user-facing output, and save it permanently only after explicit user consent. <br>
Risk: Confirmed parameters are submitted to Dataify to create external collection tasks. <br>
Mitigation: Show the exact Markdown confirmation table before each real API call and submit only after explicit user confirmation. <br>


## Reference(s): <br>
- [Dataify Indeed Companies Info API Reference](references/indeed_companies_info_api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-indeed-companies-info) <br>
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, API calls, Configuration, Guidance] <br>
**Output Format:** [Markdown confirmation tables, shell commands, and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Dataify API token; successful API calls create collection tasks and return task identifiers or status.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
