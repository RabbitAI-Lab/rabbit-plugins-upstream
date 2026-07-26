## Description: <br>
Generates a daily AI news briefing from multiple sources, deduplicates and formats the items, and sends the result as a Feishu card message. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haohuawu](https://clawhub.ai/user/haohuawu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, technical operators, and AI teams use this skill to collect daily AI updates, filter low-value items, deduplicate recurring news, and deliver a concise briefing to a Feishu chat. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can post messages to an external Feishu chat. <br>
Mitigation: Use the dry-run path first, confirm the target Feishu chat ID, and review the generated card before enabling delivery. <br>
Risk: The skill relies on Feishu and Product Hunt credentials. <br>
Mitigation: Use low-scope credentials where possible and keep secrets out of prompts, generated files, and logs. <br>
Risk: GUI/opencli/X collection can use an authenticated browser session. <br>
Mitigation: Enable GUI collection only with an isolated browser profile and disable it when API or RSS sources are sufficient. <br>
Risk: The setup script may attempt host-level package or global npm installation. <br>
Mitigation: Review setup actions first and avoid elevated privileges unless system package changes are intended. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/haohuawu/skills/ai-daily-briefing) <br>
- [Hacker News API](https://hacker-news.firebaseio.com/v0/topstories.json) <br>
- [Product Hunt GraphQL API](https://api.producthunt.com/v2/api/graphql) <br>
- [OpenAI blog RSS](https://openai.com/blog/rss.xml) <br>
- [Google DeepMind blog RSS](https://deepmind.google/blog/rss.xml) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration] <br>
**Output Format:** [Text briefing delivered as a Feishu card, with intermediate JSON files and shell commands for setup, collection, verification, and dry runs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Feishu and Product Hunt credentials; optional Firecrawl and proxy settings expand source coverage.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
