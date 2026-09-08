## Description:

青虎AI Shopee 选品决策技能为重大项目立项串联站点大盘、类目榜单、店铺榜单、商品榜单和热搜词榜，输出“大盘+竞店+爆款+搜词”的全景选品报告和多维度结论。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Shopee sellers, ecommerce analysts, and market researchers use this agent to decide whether to pursue a major Shopee product-selection initiative and to compare market, category, competitor-store, product, and search-demand signals before committing resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use a Qinghu API key and spend Qinghu credits after approval.

Mitigation: Require user approval before paid Qinghu calls and report actual Qinghu credit consumption from the returned pointCost value.

Risk: The skill calls Qinghu's external API and depends on third-party Shopee market data.

Mitigation: Treat Qinghu responses as third-party market intelligence, include source context in reports, and avoid presenting the data as Shopee seller-backend ground truth.

Risk: Larger result sets may be exported to local spreadsheet-style files that could contain sensitive business research.

Mitigation: Review exported file paths and contents before sharing or retaining reports that include sensitive product, market, or competitor analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-shopee-decision)
- [Publisher profile](https://clawhub.ai/user/autoagc)
- [Qinghu data API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown report with JSON and shell command examples, concise findings, and optional spreadsheet-style exported files for larger datasets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The report leads with a recommendation, includes market/category/store/product/search sections, and may link to local exported tables when result arrays contain 10 or more records.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
