## Description:

青虎AI Shopee 选品决策为 Shopee 重大选品立项串联站点大盘、类目、竞店、爆款和热搜词数据，生成全景选品报告与多维决策结论。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Shopee sellers, ecommerce analysts, and marketplace operators use this skill for major product-selection decisions that need a structured market, category, competitor, product, search-demand, and risk report before launch.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may require a Qinghu API token and paid Qinghu credits.

Mitigation: Request consent before calls, source the token only from the user or documented environment variables, and disclose actual Qinghu point consumption when calls occur.

Risk: Generated spreadsheet files can contain market-analysis data from the user's investigation.

Mitigation: Share exported files only with intended recipients and avoid pasting large raw datasets into chat.

Risk: The report relies on third-party Shopee market data and does not fully cover local compliance, tax, logistics, or certification requirements.

Mitigation: Validate conclusions against Shopee seller backend data and local operating requirements before committing to a product launch.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-shopee-decision)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown report with local spreadsheet attachments when returned datasets are large]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require a Qinghu API token, approval before paid calls, and point-cost disclosure when calls occur.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
