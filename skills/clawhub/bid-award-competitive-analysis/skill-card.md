## Description:

中标结果查询与竞争分析服务，查询中标公告与中标单位、企业招中标战绩画像、竞争对手识别与重叠度分析、Top中标单位/中标品牌统计、历史中标价格走势。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commercial teams use this skill to query Chinese bid and award records, identify winners and competitors, review company bidding history, and summarize market, supplier, brand, and price patterns for tender review and competitive planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or use an account and store an API key locally when no key is already configured.

Mitigation: Configure ZLBX_API_KEY manually before use when possible, and protect or review ~/.zlbx/config.json if local credential storage is used.

Risk: Auto-registration can send a hashed device identifier when no API key is configured.

Mitigation: Use auto-registration only after informed user consent, or avoid this path by configuring an API key before running the skill.

Risk: A billing or auto-login recharge link may be generated after free quota is exhausted.

Mitigation: Review the link destination and account context before opening or sharing any recharge link.

Risk: Company and contact query outputs may be incomplete or sensitive in downstream business use.

Mitigation: Review company and contact results before relying on them for decisions or sharing them outside the intended workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/bid-award-competitive-analysis)
- [标讯搜索类工具 API 详情](artifact/references/api-search.md)
- [企业分析类工具 API 详情](artifact/references/api-company.md)
- [市场分析类工具 API 详情](artifact/references/api-market.md)
- [账户查询类工具 API 详情](artifact/references/api-account.md)
- [SKILL 自动注册详细流程](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with JSON API request and response details, plus shell or configuration snippets when account setup is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read ZLBX_API_KEY or ~/.zlbx/config.json, call Zhiliaobiaoxun APIs, and write ~/.zlbx/config.json during user-approved auto-registration.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
