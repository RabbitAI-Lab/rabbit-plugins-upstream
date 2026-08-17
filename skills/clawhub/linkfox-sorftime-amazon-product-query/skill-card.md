## Description:

基于 Sorftime 数据的亚马逊多维度产品搜索与筛选技能，覆盖 14 个站点，支持产品发现、竞品调研、类目/品牌/卖家分析和历史月份快照回看。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and e-commerce researchers use this skill to query Sorftime product data, filter Amazon listings across marketplaces, compare competitors, inspect category or brand product sets, and review historical product snapshots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Amazon product queries, API keys, account information, login by phone verification code, and paid ordering flows.

Mitigation: Install and run it only when the user trusts LinkFox/Sorftime with those queries, credentials, account details, and payment actions.

Risk: The scripts support endpoint override environment variables for LinkFox gateway, login, and agent-user APIs.

Mitigation: Avoid setting endpoint override variables unless the destination is controlled and expected.

Risk: Product query responses, cache files, session metadata, and payment QR images can persist in local linkfox output directories.

Mitigation: Clear local linkfox output and cache directories when saved query results or payment artifacts should not remain on disk.

Risk: The security verdict is suspicious because the skill combines product search with login, API key handling, payment ordering, local storage, and silent feedback reporting.

Mitigation: Review the skill and its network behavior before installation, and monitor usage where credentials or billing actions are involved.

## Reference(s):

- [Sorftime Amazon Product Search API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-sorftime-amazon-product-query)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with JSON API responses and saved JSON data files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The product search script saves full responses under a local linkfox session directory, uses a 24-hour cache by default, and summarizes large responses in stdout unless inline output is requested.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
