## Description:

餐饮竞品网络变化、重点区域与市场行动建议分析。可将百度地图中复制出的地点名称和地址文本作为地点输入；基于店店通已发布门店快照生成可核验结论。本 Skill 非百度地图官方产品，和百度地图不存在合作、授权或数据来源关系。

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

Market, sales, and restaurant brand intelligence users use this skill to analyze published restaurant store snapshots, compare competitor network changes, inspect priority regions, and turn Baidu Maps address text into nearby-store or site-screening queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill sends pasted map addresses and restaurant brand queries to the 店店通/gotoshop-ai.com service.

Mitigation: Confirm that sharing those queries with the service is acceptable before use, and avoid submitting sensitive internal locations or confidential expansion plans.

Risk: The skill requires a user-provided DDT_API_KEY.

Mitigation: Store the key in a local environment variable, do not paste it into chat, and stop troubleshooting if authentication fails rather than exposing the secret.

Risk: Restaurant network conclusions are limited to 店店通 published store snapshots and stated coverage windows.

Mitigation: Report coverage periods and data scope with conclusions, and avoid treating observations as official openings, closures, revenue, profit, AUV, or closure-reason evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/horacetu/skills/ddt-baidu-map-restaurant-competitor)
- [店店通 DDT Claw](https://gotoshop-ai.com/ddtclaw/)
- [店店通 API key setup](https://gotoshop-ai.com/ddtclaw/open)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with concise analysis, key metrics, coverage notes, limited details, and inline bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a user-provided DDT_API_KEY and avoids displaying API keys, internal identifiers, or unsupported full-store exports.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
