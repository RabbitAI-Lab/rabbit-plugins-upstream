## Description:

通过极鲸云真实 AliExpress 数据查询商品、店铺、类目和历史趋势，帮助用户完成选品、竞店和品类市场调研。

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, market analysts, and agents use this skill to query GeekBI AliExpress data and produce product, shop, category, pricing, sales, and trend research for marketplace decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GeekBI bearer-token state can be stored locally in multiple locations, including the installed skill directory and current workspace.

Mitigation: Use the skill only where local GeekBI authentication state is acceptable; prefer a dedicated user config or OS credential-store location and clear old .geekbi state after testing.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/geekbi/geekbi-aliexpress-research-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-aliexpress-research-skill)
- [AliExpress 商品研究](references/AliExpress商品研究.md)
- [AliExpress 商品接口](references/AliExpress商品接口.md)
- [AliExpress 店铺研究](references/AliExpress店铺研究.md)
- [AliExpress 店铺接口](references/AliExpress店铺接口.md)
- [AliExpress 类目研究](references/AliExpress类目研究.md)
- [AliExpress 类目接口](references/AliExpress类目接口.md)
- [AliExpress 运营与政策口径](references/AliExpress运营与政策口径.md)
- [接口总览](references/接口总览.md)
- [查询暂停与恢复流程](references/查询暂停与恢复流程.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown research summaries with data scope, evidence, risks, and validation steps.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON snippets or service action links during authentication or recoverable query pauses.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
