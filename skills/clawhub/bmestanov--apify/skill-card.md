## Description: <br>
Run Apify Actors through the Apify REST API to scrape websites, crawl pages, extract data, and retrieve results from datasets and key-value stores. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bmestanov](https://clawhub.ai/user/bmestanov) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to choose and run Apify Actors, monitor runs, and retrieve structured scraping or crawling outputs from Apify storage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can let an agent operate an Apify account with broad account and data-management effects. <br>
Mitigation: Use a revocable least-privilege APIFY_TOKEN, keep the token out of logs and prompts, and approve each Actor, target site, budget, and run limit before execution. <br>
Risk: Account-limit changes, webhooks, schedules, or deletes could have persistent or destructive effects. <br>
Mitigation: Do not allow those operations unless the user explicitly requested and reviewed them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/bmestanov/apify) <br>
- [Apify API Documentation](https://docs.apify.com/api/v2) <br>
- [Apify API Markdown Reference](https://docs.apify.com/api/v2.md) <br>
- [Apify Store](https://apify.com/store) <br>
- [OpenAPI Specification](openapi.json) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text, code] <br>
**Output Format:** [Markdown with inline bash commands and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires APIFY_TOKEN and either curl or wget; results are typically returned as JSON, CSV, JSONL, XML, XLSX, RSS, logs, or key-value store records depending on the Apify endpoint.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
