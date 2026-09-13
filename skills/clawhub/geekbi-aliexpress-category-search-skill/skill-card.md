## Description:

Uses GeekBI live AliExpress data to look up category trees, verified category paths, and category IDs, then analyze product samples for sales, revenue, price bands, supply structure, and category opportunities without treating samples as full-platform market data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, analysts, and developers use this skill to find trustworthy AliExpress category IDs and study category-level product samples for selection, pricing, supply concentration, and next-step validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Login handling could expose authentication tokens or direct users to untrusted login links.

Mitigation: Install only when GeekBI is trusted, avoid custom --base-url values, verify login links before opening them, and review any .geekbi/agent-auth.json files created after use.

Risk: Category product samples can be mistaken for complete AliExpress market data.

Mitigation: Keep outputs scoped to the returned sample and state filters, sample size, site, total-hit limit, and update time before drawing category conclusions.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/geekbi/geekbi-aliexpress-category-search-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-aliexpress-category-search-skill)
- [AliExpress 类目接口](references/AliExpress类目接口.md)
- [AliExpress 类目研究](references/AliExpress类目研究.md)
- [查询暂停与恢复流程](references/查询暂停与恢复流程.md)
- [AliExpress 运营与政策口径](references/AliExpress运营与政策口径.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with JSON command outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports category path, sample scope, filters, site, update time, key data, opportunities, risks, and recommended next validation steps.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
