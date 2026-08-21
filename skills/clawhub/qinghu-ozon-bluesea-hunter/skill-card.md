## Description:

This skill helps agents evaluate Ozon Russia market categories by comparing category growth, market trend snapshots, hot-category rankings, and brand concentration to identify less-saturated segments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and agents use this skill to evaluate Ozon Russia category opportunities for new stores, new product categories, and blue-ocean segment selection. It produces a short list of recommended category paths, growth comparisons against the market baseline, saturation warnings, and entry suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Qinghu API tokens may be available to the agent environment and used for data calls.

Mitigation: Install only in environments where Qinghu Ozon data access is intended, and avoid exposing QINGHU_TOKEN or QHKIT_TOKEN where those credentials should not be used.

Risk: Approved Qinghu data calls may consume Qinghu points.

Mitigation: Confirm the planned tools before the first call, rely on returned pointCost for accounting, and report total Qinghu point consumption after paid calls.

Risk: Market recommendations can be misleading if category IDs, periods, or nested API responses are misread.

Mitigation: Use tool schemas before calling, derive IDs from category lookup tools, parse nested JSON responses, compare like periods, and label site, period, cycle, and sample size in outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-ozon-bluesea-hunter)
- [Qinghu MCP data endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu workflow permission check endpoint](https://www.iqinghu.com/api/desktop/qh/workflow/page?pageNum=1&pageSize=5)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance, API calls]

**Output Format:** [Markdown recommendations with concise previews; larger record sets may be exported as table files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation before Qinghu data calls; paid calls should report Qinghu point consumption.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
