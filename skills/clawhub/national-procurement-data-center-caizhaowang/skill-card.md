## Description:

全国采招大数据中心-采招网，当用户需要跨省份、跨行业的全盘数据检索或综合企业画像分析时调用，需综合运用检索与企业画像接口，提供全景式的数据展现。

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Chinese procurement and award notices, analyze company profiles and relationships, track business opportunities, and summarize procurement market patterns from Zhiliaobiaoxun/Caizhaowang data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: If no API key is configured, the skill may ask to register a trial account using device characteristics and then store the returned API key locally.

Mitigation: Prefer supplying ZLBX_API_KEY through a managed secret or environment variable; allow automatic registration only after explicit user consent and review local credential storage.

Risk: The skill can produce recharge, login, and promotional links as part of its account flow.

Mitigation: Review links critically before use and avoid entering credentials or payment details unless the destination is expected and trusted.

Risk: Company expansion and procurement-contact workflows may return sensitive or masked contact information.

Mitigation: Use contact data only as returned by the service; do not attempt to deanonymize masked phone numbers or perform bulk contact exports.

Risk: Procurement analysis can be misleading when filters, amount units, match modes, or company disambiguation are wrong.

Mitigation: Show applied filters, confirm ambiguous companies, check amount units before querying, and summarize uncertainty in user-facing results.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/pkuycl/skills/national-procurement-data-center-caizhaowang)
- [Bid Search API Reference](references/api-search.md)
- [Company Analysis API Reference](references/api-company.md)
- [Market Analysis API Reference](references/api-market.md)
- [Account API Reference](references/api-account.md)
- [Automatic Registration Flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown summaries with tables and JSON request or response snippets when useful.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on authenticated API responses, account quota, and user-provided or locally stored API credentials.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
