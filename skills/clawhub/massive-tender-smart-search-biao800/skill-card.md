## Description:

海量标讯智搜助手-标800 helps agents search, filter, and analyze tender, company, market, and account data from Biao800-style procurement APIs using complex criteria such as keyword groups, exclusions, regions, amounts, and time windows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business-development agents use this skill to search Chinese tender opportunities, inspect project timelines, analyze companies and competitors, check market trends, and review account usage. It is suited for procurement intelligence workflows that need concise result summaries, tables, and follow-up guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Opt-in auto-registration sends platform, architecture, and hashed MAC information to the provider and stores an API key under ~/.zlbx/config.json.

Mitigation: Prefer preconfiguring ZLBX_API_KEY before first use; approve auto-registration only after reviewing the disclosed device features and local credential storage behavior.

Risk: Company contact lookups can expose account-dependent contact information, including masked or full phone numbers.

Mitigation: Display contact data exactly as returned, respect masking, and avoid attempts to reconstruct or bulk export contact details.

Risk: Tender and market analyses can be misleading if amount units, date fields, or match modes are applied incorrectly.

Mitigation: State the active filters in the answer, normalize displayed amounts with units, and use the documented parameter-specific amount units.

## Reference(s):

- [标讯搜索类工具 API 详情](references/api-search.md)
- [企业分析类工具 API 详情](references/api-company.md)
- [市场分析类工具 API 详情](references/api-market.md)
- [账户查询类工具 API 详情](references/api-account.md)
- [SKILL 自动注册详细流程](references/auto-register.md)
- [ClawHub skill page](https://clawhub.ai/pkuycl/skills/massive-tender-smart-search-biao800)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with concise summaries, result tables, JSON request examples, and occasional shell commands for setup.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or opt-in auto-registration; contact details may be masked by account level.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
