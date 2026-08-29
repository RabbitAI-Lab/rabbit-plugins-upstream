## Description:

青虎AI TikTok 单品分析：批量查商品详情，拆解它关联的带货视频、直播与达人，读商品评论，量化单品的全网爆发力与渠道依赖度，为货源采购与推广预算提供数据支撑。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and analysts use this skill to evaluate a known TikTok Shop product's sales strength, channel dependence, review sentiment, stocking risk, and promotion budget allocation. It is intended for product-level analysis after a product ID, product link, or search term is available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Qinghu API token to access product-analysis data.

Mitigation: Use a user-provided token or the documented environment variables, avoid exposing the token in replies or exported files, and stop when authentication or permission checks fail.

Risk: The skill can make paid Qinghu API calls.

Mitigation: Ask for one upfront confirmation before tool calls, report actual Qinghu point consumption from the response envelope, and do not estimate costs from unrelated business data.

Risk: Ambiguous product requests can lead to analyzing the wrong TikTok item.

Mitigation: Confirm the product ID or search result before paid calls when the user provides only a name or ambiguous link.

Risk: Large analysis results may be saved as local files.

Mitigation: Export large tables locally only when useful, keep responses concise, and provide file links with clear context about what was saved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-tiktok-product-analyst)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with JSON and shell command examples; larger result sets may be exported as local table files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill reports concise product conclusions first, then supporting data with site, period, and sample-size context.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
