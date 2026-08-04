## Description: <br>
Extracts structured web data from URLs, search results, JavaScript-rendered pages, URL maps, and crawls through the ZooData WebTools API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill when they need structured page data, search-result extraction, JavaScript-rendered page scraping, URL discovery, or site crawling without a separate parsing pass. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Requested URLs, search terms, crawl options, and interactive actions are sent to ZooData for processing. <br>
Mitigation: Use only when sharing those inputs with ZooData is acceptable for the user's environment. <br>
Risk: The skill requires a ZooData API key and can read an optional local credential file. <br>
Mitigation: Prefer environment variables or a secret store, restrict credential-file permissions, and avoid pasting real keys into prompts, docs, logs, or shared files. <br>
Risk: Large crawls, deep-scraped searches, and polling can consume paid credits. <br>
Mitigation: Estimate credit use and confirm before large crawls or deep-scrape jobs. <br>


## Reference(s): <br>
- [ClawHub web-extract skill page](https://clawhub.ai/apiclaw/skills/web-extract) <br>
- [ZooData Skills homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [Web Extract endpoint reference](references/reference.md) <br>
- [ZooData API keys](https://zoodata.ai/en/api-keys) <br>
- [ZooData pricing](https://zoodata.ai/en/pricing) <br>


## Skill Output: <br>
**Output Type(s):** [json, text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and API responses that may include JSON, markdown, or raw HTML.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY; sends requested URLs, search terms, crawl options, and interactive actions to ZooData.] <br>

## Skill Version(s): <br>
0.2.3 (source: server evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
