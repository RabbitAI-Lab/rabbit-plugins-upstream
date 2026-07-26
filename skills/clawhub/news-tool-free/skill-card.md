## Description: <br>
个性化新闻助手免费版 helps an agent learn a single user's news interests, output preferences, and timing habits to produce personalized news briefings with local memory and multi-source coverage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individual users, students, and independent developers use this skill to set local news preferences and request concise personalized briefings on chosen topics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The local ~/news profile can contain personal interests, preferences, and briefing history. <br>
Mitigation: Keep the ~/news directory private, review it before sharing logs or backups, and avoid storing sensitive interests in the profile. <br>
Risk: Searches for chosen topics may reveal those topics to the agent's search provider. <br>
Mitigation: Use trusted search providers, avoid highly sensitive queries, and disclose this exposure when using the skill with personal or confidential topics. <br>
Risk: Briefings depend on external search availability and may miss paywalled, stale, or unverified reporting. <br>
Mitigation: Cross-check important items with multiple sources and keep source names and timestamps in the generated briefing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/news-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown briefings with sourced bullets, setup snippets, and local profile/history files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses agent-provided web search and local files under ~/news; no separate API key is required by the skill.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence release.version; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
