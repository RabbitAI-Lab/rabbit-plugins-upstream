## Description:

青虎AI 1688 选品与货源技能帮助电商卖家通过以图搜款、关键词搜索和商品详情查询找到货源、比较供应商并估算采购成本。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, sourcing teams, and ecommerce operators use this skill to find 1688 suppliers from product images, keywords, or offer IDs, then compare price tiers, minimum order quantities, sales signals, shop attributes, fulfillment timing, and margin assumptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product links, search terms, and publicly hosted image URLs may be sent to the Qinghu API.

Mitigation: Use the skill only for intended Qinghu/1688 sourcing workflows and avoid proprietary product images unless the user is comfortable making them available through a public URL.

Risk: The skill may read Qinghu tokens from environment variables and make paid API calls.

Mitigation: Follow the documented authorization flow, request consent before paid calls, and report Qinghu point consumption from the response envelope.

Risk: Large result sets may be exported to local spreadsheet files.

Mitigation: Keep exported files scoped to the working environment and share concise previews instead of exposing full datasets in chat.

Risk: 1688 matches may differ in quality or carry supplier, brand, patent, minimum order quantity, and fulfillment risks.

Mitigation: Recommend sample verification, compare multiple suppliers, and call out authorization, order quantity, and delivery assumptions before acting on recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-1688-sourcing)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu workflow auth check endpoint](https://www.iqinghu.com/api/desktop/qh/workflow/page?pageNum=1&pageSize=5)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with JSON request examples and optional spreadsheet exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include supplier comparison tables, concise previews, cost assumptions, risk notes, and exported table files for larger result sets.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
