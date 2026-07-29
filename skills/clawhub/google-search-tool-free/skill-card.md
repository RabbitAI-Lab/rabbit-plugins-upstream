## Description: <br>
谷歌搜索工具 uses Google Custom Search Engine to retrieve live search results and return structured titles, links, and summaries for research and information lookup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, students, researchers, and developers use this skill to run explicit web search and research queries through Google Custom Search and review structured result summaries. It is suited for academic lookup, technical documentation discovery, and time-sensitive information retrieval when the user has configured Google API credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to Google's Custom Search API and may expose sensitive terms to an external service. <br>
Mitigation: Do not include secrets, credentials, or sensitive personal data in search queries. <br>
Risk: The artifact contains imprecise SEO trigger text and create/export wording that can overstate the free skill's supported behavior. <br>
Mitigation: Use the skill only for explicit web search and research tasks, and rely on the documented free-edition limits for batch search, export, custom site search, and search history. <br>
Risk: The skill requires Google API credentials to operate. <br>
Mitigation: Configure credentials through environment variables or a local environment file and avoid placing API keys in prompts, shared logs, or generated output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/google-search-tool-free) <br>
- [Google APIs endpoint](https://www.googleapis.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and structured JSON-style search results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results include status, result data, execution log, and error fields; use requires Google API key and Custom Search Engine ID configuration.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
