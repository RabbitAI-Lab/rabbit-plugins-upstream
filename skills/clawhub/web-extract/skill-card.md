## Description: <br>
Extracts structured JSON from web pages, search results, JavaScript-rendered pages, URL maps, and site crawls through the ZooData WebTools API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use Web Extract when they need structured page data, search-result extraction, JavaScript-rendered scraping, URL discovery, or recursive site crawling without a second parsing pass over raw HTML or prose. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Target URLs, search queries, interaction steps, and scraped page content are sent to ZooData. <br>
Mitigation: Use the skill only for content appropriate to share with ZooData, and avoid secrets, confidential data, and internal-only URLs. <br>
Risk: The ZooData API key is required for operation. <br>
Mitigation: Store the key in ZOODATA_API_KEY or a protected config file, and avoid pasting credentials into prompts or generated output. <br>
Risk: The credential check command consumes one credit. <br>
Mitigation: Run the check command intentionally and account for credit usage before repeated verification. <br>


## Reference(s): <br>
- [Web Extract endpoint reference](references/reference.md) <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/web-extract) <br>
- [Publisher homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData API keys](https://zoodata.ai/en/api-keys) <br>


## Skill Output: <br>
**Output Type(s):** [json, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON by default, with optional Markdown or raw HTML and Markdown guidance containing shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY; requests may send target URLs, search queries, interaction steps, and scraped page content to ZooData.] <br>

## Skill Version(s): <br>
0.2.1 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
