## Description:

抖音相似账号推荐工具，输入抖音账号名称或账号ID，通过红狐API接口获取本账号数据、内容数据和相似账号推荐数据，深度分析共通点、差异点和优化建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

External Douyin creators, brand operators, MCN teams, and content teams use this skill to find comparable or top-performing Douyin accounts and review account metrics, content patterns, and optimization suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin account identifiers and the user's RedFox API key to RedFox.

Mitigation: Use the skill only when that data sharing is acceptable, and prefer a temporary environment variable or dedicated secret manager for the API key.

Risk: The skill documentation and behavior may encourage persisting or revealing API keys.

Mitigation: Do not write the API key into shell startup files, logs, prompts, or output; avoid echoing the full key.

Risk: query_wrapper.py ignores the requested account and runs a hard-coded lookup.

Mitigation: Avoid query_wrapper.py and invoke scripts/douyin_similar_account.py with an explicit account_id after reviewing the command.

## Reference(s):

- [Core Workflow](references/core_workflow.md)
- [README.en.md](README.en.md)
- [ClawHub Skill Page](https://clawhub.ai/redfox-data/skills/douyin-similar-account)
- [RedFoxHub](https://redfox.hk)
- [RedFox Similar Accounts API](https://redfox.hk/story/api/dyUser/querySimilarAccounts)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, API Calls, Shell commands, Guidance]

**Output Format:** [Markdown report with account details, recommendation tables, and analysis text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires REDFOX_API_KEY and sends the requested Douyin account identifier to RedFox.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
