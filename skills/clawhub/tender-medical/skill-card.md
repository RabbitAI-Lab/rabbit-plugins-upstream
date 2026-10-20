## Description:

帮助用户查询和分析招投标、企业及市场数据，默认聚焦医疗卫生行业，并尊重用户指定的行业和地区范围。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

采购、投标和市场分析人员使用该技能检索医疗卫生领域的招中标公告、项目进展、供应商、企业信息与历史价格；用户可以指定其他行业或地区。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic trial registration can send a hashed device identifier to the provider.

Mitigation: Provide your own ZLBX_API_KEY to avoid automatic registration; otherwise obtain consent before registration.

Risk: The skill can store a provider API key locally under ~/.zlbx/config.json.

Mitigation: Review local credential storage and access before enabling the skill; use an existing environment-provided key if preferred.

Risk: Hidden comment-based instructions may affect requests.

Mitigation: Review the skill source and generated requests before allowing access to provider services.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bailianai/skills/tender-medical)
- [Provider skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Search API reference](artifact/references/api-search.md)
- [Company API reference](artifact/references/api-company.md)
- [Registry data reference](artifact/references/api-registry.md)
- [Market API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Account registration reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Markdown with procurement results and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on provider data and available account credits.]

## Skill Version(s):

1.0.5 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
