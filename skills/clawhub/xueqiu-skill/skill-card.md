## Description: <br>
雪球数据API接口调用工具。当用户需要查询雪球组合、用户、行情、调仓历史等投资数据时调用此技能。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiongweixp](https://clawhub.ai/user/xiongweixp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to query Xueqiu investment data from conversation, including users, portfolios, posts, quotes, net value history, holdings, and rebalancing history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks users to provide live paid API credentials to the agent environment. <br>
Mitigation: Use revocable or low-balance credentials, avoid pasting sensitive keys into chat, and rotate any key exposed during use. <br>
Risk: Queries and credentials are sent to a third-party service for Xueqiu data access. <br>
Mitigation: Use the skill only when you trust the service operator and avoid submitting sensitive investment research queries. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/xiongweixp/skills/xueqiu-skill) <br>
- [Xueqiu API service](https://wxpub.aibana.art) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Text, Guidance] <br>
**Output Format:** [Markdown guidance with JSON request examples and API response summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses credentialed POST requests with app_id and secure_key; successful calls are billed and subject to shared rate limits.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
