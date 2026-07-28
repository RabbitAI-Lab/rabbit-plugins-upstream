## Description: <br>
Extracts structured JSON, Markdown, or raw HTML from web pages, search results, URL maps, and recursive crawls through ZooData WebTools endpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to fetch structured page data, search results with optional deep scraping, URL maps, and crawl outputs for downstream analysis or automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Requested URLs, search queries, and crawl parameters are sent to ZooData for processing. <br>
Mitigation: Use the skill only for data you are comfortable sharing with ZooData and avoid submitting sensitive targets or queries. <br>
Risk: Large crawls and deep-scraped searches can consume API credits. <br>
Mitigation: Estimate costs and confirm large crawls before execution; keep crawl limits and polling intervals conservative. <br>
Risk: The skill requires an API key that may be stored in the environment or local config. <br>
Mitigation: Prefer ZOODATA_API_KEY in a protected environment or a secured config file, and do not expose keys in prompts, logs, or shared files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/web-extract) <br>
- [ZooData Skills homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [Web Extract endpoint reference](references/reference.md) <br>
- [ZooData API keys](https://zoodata.ai/en/api-keys) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON-oriented command examples and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include structured extraction fields, endpoint choices, shell commands, and credential setup guidance.] <br>

## Skill Version(s): <br>
0.2.2 (source: release evidence and frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
