## Description:

青虎AI 亚马逊细分市场评估：进入某个品类前先看大盘，评估市场容量、销售额、头部 Listing 与品牌垄断程度、价格带空间、卖家所属地结构、新品活跃度、需求趋势与退货率，并给出市场准入可行性结论。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and market analysts use this skill to decide whether an Amazon category is worth entering. It converts a category query into Qinghu API calls and returns a conclusion-first market assessment with supporting metrics, entry suggestions, and risks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires a Qinghu API key and sends Amazon category queries to Qinghu's API.

Mitigation: Use a Qinghu key intended for this workflow, confirm authorization before calls, and avoid submitting confidential category strategy unless sharing it with Qinghu is acceptable.

Risk: Larger result sets may be written to local export files.

Mitigation: Review generated file locations before sharing outputs and remove exports that contain sensitive market research.

Risk: Market metrics are third-party estimates and may not reflect exact Amazon sales, profitability, compliance, certification, or patent exposure.

Mitigation: Treat the skill output as decision support, validate high-stakes conclusions with independent data, and perform separate compliance, certification, and patent checks before launch.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/qinghu-amazon-market-assessor)
- [Qinghu API Endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API Key Dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown with concise recommendations, metric summaries, risk lists, and links to exported table files when large result sets are returned.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local export files for result arrays with 10 or more records; reports Qinghu point consumption when paid API calls occur.]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
