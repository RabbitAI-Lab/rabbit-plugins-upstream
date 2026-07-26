## Description: <br>
用于快手数据分析、快手作品研究、关键词观察、内容调研、竞品分析和趋势研究。覆盖 Kuaishou / Kwai work research，来自 SocialDataX 社媒数据助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to search Kuaishou works and short videos for keyword research, content research, competitor analysis, and trend scanning through SocialDataX. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a user-provided SOCIALDATAX_API_KEY for the SocialDataX CLI/API workflow. <br>
Mitigation: Use only the documented SocialDataX access page for API key management, keep the key in the environment, and install only when SocialDataX access is intended. <br>
Risk: Kuaishou search results can be incomplete or paginated, so a single page may not represent full platform coverage. <br>
Mitigation: Use the returned next_page_token unchanged for continued searches and present visible evidence separately from interpretation. <br>
Risk: This is a third-party read-only integration, so users should understand what service receives the API key and query parameters. <br>
Mitigation: Review the server-provided security guidance and the skill's safety boundary before deployment; the artifact does not request local browser data, login, posting, liking, commenting, or account changes. <br>


## Reference(s): <br>
- [SocialDataX AI access page](https://socialdatax.com/ai?from=clawhub) <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-search) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY and node/npm; Kuaishou search results may include content IDs, URLs, titles or descriptions, author facts, counts, publish times, pagination markers, and visible-evidence summaries.] <br>

## Skill Version(s): <br>
0.1.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
