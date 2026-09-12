## Description:

Qinghu AI TikTok product-selection decisioning correlates product rankings, video rankings, influencer supply, competitor-store products, and product detail data to produce an actionable TikTok selection report with optional 1688 sourcing and Xiaofeng ERP listing support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators and TikTok Shop teams use this skill to decide which products or categories to pursue by combining sales, content, influencer, competitor, sourcing, and margin signals. It can also guide confirmed handoff into 1688 sourcing and Xiaofeng ERP distribution workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can spend Qinghu credits through paid data calls.

Mitigation: List the planned tools and obtain user confirmation before execution, then report actual Qinghu credits from returned pointCost values.

Risk: The workflow requires Qinghu API credentials.

Mitigation: Use only a user-provided key or configured QINGHU_TOKEN/QHKIT_TOKEN value, and avoid exposing the credential in outputs.

Risk: Optional Xiaofeng ERP distribution can initiate a downstream listing flow.

Mitigation: Restate the selected links and template and obtain confirmation before running distribution.

Risk: Selection guidance may be affected by delayed or scoped market data.

Mitigation: Label site, date period, accounting period, and sample size, and present conclusion-level risks before supporting data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-tiktok-decision)
- [Qinghu data API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu login](https://www.iqinghu.com/workbench/login?type=1&urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown report with concise summaries and exported table or data-file links when record sets are large]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes upfront tool and cost confirmation, Qinghu credit reporting after paid calls, and labeled data scope such as site, period, and sample size.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
