## Description:

海量标讯智搜助手-标800，当用户提供复杂的搜索条件（多个关键词、排除特定词汇、指定金额区间）时调用，需精确组合查询条件，过滤无效信息，提供高准确率的数据反馈。

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search tender notices, inspect company participation, and analyze procurement markets with precise keyword, exclusion, amount, geography, and time filters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional trial setup sends platform, architecture, and a hashed MAC-derived identifier for device de-duplication.

Mitigation: Configure ZLBX_API_KEY before use or decline the trial prompt if that device-identification flow is not acceptable.

Risk: The trial setup can store a returned API key in ~/.zlbx/config.json.

Mitigation: Review local credential storage expectations before enabling the setup flow, and manage or remove the stored key according to local policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pkuycl/skills/massive-tender-smart-search-biao800)
- [Publisher profile](https://clawhub.ai/user/pkuycl)
- [Free trial account setup guide](references/account-setup.md)
- [Tender search API details](references/api-search.md)
- [Company analysis API details](references/api-company.md)
- [Market analysis API details](references/api-market.md)
- [Account query API details](references/api-account.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API examples and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide API calls that require ZLBX_API_KEY or a consent-gated trial account setup.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
