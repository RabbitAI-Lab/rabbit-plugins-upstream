## Description:

Use when a user asks for HotBee all-web hot rankings, 热榜, 热搜, trending topics, or platform hot-search ranking data across confirmed Xiaohongshu, Douyin, Baidu, Weibo, and Bilibili endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shanye1402-hash](https://clawhub.ai/user/shanye1402-hash)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request current hot-ranking data for Xiaohongshu, Douyin, Baidu, Weibo, and Bilibili through confirmed HotBee endpoints while managing paid API usage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live HotBee requests can consume paid points or quota.

Mitigation: Start with dry-runs, explain selected platforms and possible cost, and require approval before live calls unless the user has already approved spend.

Risk: HOTBEE_API_KEY could be exposed if handled carelessly.

Mitigation: Read the API key only from the local environment and never echo, persist, or include it in generated output.

Risk: Requests for unsupported platforms could produce incorrect endpoint guidance.

Mitigation: Use only confirmed HotBee endpoints and ask for the official OpenAPI contract when a requested platform is not confirmed.

## Reference(s):

- [Hot Rankings API](references/api.md)
- [HotBee Skills](https://www.hotbee.cn/skills)
- [ClawHub Skill Page](https://clawhub.ai/shanye1402-hash/skills/hotbee-hot-rankings)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with shell command examples and API response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses HOTBEE_API_KEY from the local environment; live calls may consume HotBee points or quota.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
