## Description:

帮助建筑行业用户查询工程招投标信息、追踪项目进展，并发现潜在供应商和临期项目商机。

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

建筑行业用户可检索中国工程招投标公告、分析企业与市场、追踪项目阶段，并识别潜在参标单位和续约机会。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic trial registration sends a stable hashed MAC-derived device identifier to the service.

Mitigation: Review the privacy implications and obtain consent before registration; configure your own ZLBX_API_KEY to avoid automatic registration.

Risk: Automatically generated API keys are stored locally and account or contact features may expose sensitive information.

Mitigation: Protect ~/.zlbx/config.json and use contact and account-management features only when needed for the intended workflow.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pkuycl/skills/architecture-bid-insight-zhulongbiaoshi)
- [Skill usage documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Bid search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account registration guidance](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include bid details, company information, market summaries and project recommendations.]

## Skill Version(s):

1.0.8 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
