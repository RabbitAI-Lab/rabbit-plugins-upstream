## Description:

Helps agents search public community, social media, news, encyclopedia trend, developer ecosystem, and technical discussion signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to gather public trend and discussion signals from free, public web and API sources for news, social media, technical communities, open source activity, and encyclopedia attention. It is not intended for cryptocurrency, blockchain, Web3, NFT, DeFi, exchange, wallet, or related market trend requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outbound requests to public web services can disclose query topics to those services.

Mitigation: Use the skill only for public trend and search tasks, and avoid providing secrets, cookies, tokens, or private internal topics.

Risk: Installing httpx into the active Python environment can change dependency state.

Mitigation: Install dependencies in an isolated environment and pin or review the requirement before deployment.

Risk: Single-source trend signals can be incomplete or misleading.

Mitigation: Compare multiple public sources and report conflicting platform signals instead of presenting one platform as an overall trend.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-search-social-media)
- [ClawHub publisher profile](https://clawhub.ai/user/sensenova-skills)
- [Wikimedia Pageviews API documentation](https://doc.wikimedia.org/generated-data-platform/aqs/analytics-api/)
- [GitHub public search](https://github.com/search)
- [Stack Exchange search](https://stackexchange.com/search)
- [Hacker News](https://news.ycombinator.com/)
- [Baidu Index](https://index.baidu.com/)
- [Weibo hot search](https://s.weibo.com/top/summary)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON script outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Script outputs use a standard JSON object with success, query, provider, items, and error fields.]

## Skill Version(s):

2026.8.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
