## Description:

Uses GeekBI to query and analyze AliExpress shop details, sales, revenue, ratings, followers, product counts, category structure, and operating trends when a shop ID or representative product ID is available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to research AliExpress shops by shop ID or product ID, compare shop performance, and summarize product-structure evidence. It supports read-only competitive research and excludes seller-center write operations, orders, advertising, returns, commissions, and fulfillment metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GeekBI authentication state may be stored locally.

Mitigation: Use the default GeekBI endpoint, avoid shared or synced workspaces, and clear the local auth state when finished if the token should not remain on disk.

Risk: AliExpress shop metrics can be incomplete, delayed, or sample-limited and should not be treated as official settlement or account-health data.

Mitigation: Disclose missing fields, collection time, invalid placeholder values, and the sample boundary; verify operational decisions in AliExpress front-end or seller-center sources.

## Reference(s):

- [Server-resolved source repository](https://github.com/geekbi/geekbi-aliexpress-shop-search-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-aliexpress-shop-search-skill)
- [AliExpress shop interface reference](references/AliExpress店铺接口.md)
- [AliExpress shop research reference](references/AliExpress店铺研究.md)
- [AliExpress operations and policy framing](references/AliExpress运营与政策口径.md)
- [Query pause and resume flow](references/查询暂停与恢复流程.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown prose with JSON evidence from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only AliExpress shop research summaries should distinguish interface facts, sample calculations, business judgment, missing fields, collection time, and items requiring external verification.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
