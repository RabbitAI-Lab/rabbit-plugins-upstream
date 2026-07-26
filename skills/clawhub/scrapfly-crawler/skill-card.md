## Description: <br>
Crawl entire websites using the Scrapfly Crawler API with the Python SDK. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scrapfly](https://clawhub.ai/user/scrapfly) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and data teams use this skill to configure Scrapfly Crawler jobs for site-wide crawling, URL discovery, bulk content retrieval, structured extraction, and WARC/HAR archive handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unbounded or broad crawls can consume credits, crawl unintended pages, or collect irrelevant content. <br>
Mitigation: Use tight page, depth, duration, path, and credit limits; keep external link following disabled unless it is explicitly needed. <br>
Risk: Crawler features such as anti-bot bypass, proxies, robots.txt overrides, or nofollow overrides can be misused on sites where crawling is not authorized. <br>
Mitigation: Crawl only authorized targets, enable robots.txt compliance where appropriate, and use anti-bot or proxy options only with permission. <br>
Risk: API keys, webhook payloads, and saved crawl archives may expose sensitive credentials or collected content. <br>
Mitigation: Protect SCRAPFLY_API_KEY, verify webhook signatures in production, and review WARC/HAR or content archives before storage or sharing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/scrapfly/skills/scrapfly-crawler) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with Python and bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; examples require a Scrapfly API key and user-selected crawl limits.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
