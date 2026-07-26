## Description: <br>
Prepares Dataify builder requests for Crunchbase scraper tools rooted at crunchbase_company_by-url, including tool selection, saved parameter lookup, and curl generation for scraperapi.dataify.com/builder. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and data operators use this skill to prepare Dataify Crunchbase scraper builder requests, choose the URL or keyword tool, provide parameter values, and receive a curl command that uses DATAIFY_API_TOKEN. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated requests use a Dataify API token, and persistent shell startup configuration can expose credentials if handled carelessly. <br>
Mitigation: Use session-only environment variables or managed secret storage when appropriate, and avoid committing, logging, or sharing DATAIFY_API_TOKEN. <br>
Risk: Builder requests send selected scraper parameters and any supplied business data to Dataify's scraperapi.dataify.com endpoint. <br>
Mitigation: Review parameters before execution and avoid including secrets or unnecessary sensitive business data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-crunchbase-company-by-url) <br>
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Dataify builder endpoint](https://scraperapi.dataify.com/builder) <br>
- [Tool parameters catalog](artifact/references/tool-params.json) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, JSON, Guidance] <br>
**Output Format:** [Markdown with inline bash, PowerShell, and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generates Dataify builder curl requests and can normalize spider_parameters JSON through the bundled helper script.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
