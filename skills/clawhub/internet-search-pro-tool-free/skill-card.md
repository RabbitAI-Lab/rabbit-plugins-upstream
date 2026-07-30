## Description: <br>
联网搜索助手 helps users turn natural-language questions into web searches, filter results, and return concise structured summaries with source links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External personal users use this skill to retrieve current news, weather, product information, and other web-search-backed facts, then receive a short summary with sourced results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad command and local-file capabilities that are not tightly scoped to web search. <br>
Mitigation: Review before installing, use it only for non-sensitive searches, and prefer a version with removed or tightly scoped exec and local-file access unless command-line search integration is explicitly required. <br>
Risk: Search queries or optional callback and API configuration can expose private personal or business data. <br>
Mitigation: Do not enter sensitive information, secrets, or private business data into searches or optional configuration values. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/internet-search-pro-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown-style structured search summaries with source links and occasional bash snippets for optional configuration.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns 3-5 search results for a single query; the free edition does not support multi-turn search, batch queries, result export, or search history.] <br>

## Skill Version(s): <br>
1.0.2 (source: evidence.json release.version; artifact/SKILL.md frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
