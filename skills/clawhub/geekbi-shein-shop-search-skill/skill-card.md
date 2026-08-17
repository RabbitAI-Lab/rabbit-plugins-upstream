## Description:

通过极鲸云实时搜索和分析 SHEIN 店铺，帮助跨境卖家按店铺、站点、托管模式、销量、销售额、评分、评论、商品、粉丝、价格、开店时间和增长指标筛选竞品并形成中文业务结论。

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and analysts use this skill to research SHEIN shops, identify comparable competitors, build shop shortlists, and assess shop-level scale, growth, product supply, followers, reputation, and hosting mode from GeekBI data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs local Python scripts and contacts GeekBI's API using local GeekBI login state.

Mitigation: Install only when that local execution, network access, and account-state reuse are acceptable for the environment.

Risk: The security evidence flags reused or stored GeekBI login state in a mismatched TEMU-named auth directory.

Mitigation: Review the local GeekBI auth storage before installation and confirm it will not unintentionally share or affect login state used by other GeekBI skills.

Risk: Shop conclusions may be misleading if based on partial pagination or unavailable returned fields.

Mitigation: Disclose sample size, total result count, pagination limits, update time, and avoid claims not supported by returned GeekBI data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-shein-shop-search-skill)
- [Source repository](https://github.com/geekbi/geekbi-shein-shop-search-skill)
- [README](artifact/README.md)
- [SHEIN shop search method](artifact/references/SHEIN店铺搜索.md)
- [SHEIN shop search API](artifact/references/SHEIN店铺搜索接口.md)
- [SHEIN shop ranking presets](artifact/references/SHEIN店铺榜单预设.md)
- [Query pause and resume flow](artifact/references/查询暂停与恢复流程.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown business analysis with links to returned SHEIN shops and, when needed, local shell commands for GeekBI queries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language conclusions are limited to shop-level data returned by GeekBI; incomplete pagination should be disclosed as a sample.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
