## Description:

Guides agents through a Qinghu-powered TikTok product research workflow that finds rising blue-ocean products, checks item details, locates 1688 supply matches, and estimates gross margin.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, sourcing teams, and agents use this skill to identify rising TikTok Shop products, review product and content signals, find matching 1688 suppliers, and prepare concise product recommendations with margin assumptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires a Qinghu API token and may expose that token to the Qinghu endpoint.

Mitigation: Request the token only from the user or approved environment variables, use the documented bearer header, and avoid including secrets in outputs or exports.

Risk: Some Qinghu data tools can consume paid credits after authorization.

Mitigation: Review paid-tool prompts before approval, follow the skill's authorization rules, and report actual Qinghu credit usage from the response envelope.

Risk: Large product-research result sets may be exported locally.

Mitigation: Keep exports limited to the requested research data, provide concise previews, and share only intended local export links.

Risk: Margin estimates and 1688 product matches may not reflect final costs or product quality.

Mitigation: Label logistics and commission assumptions, recommend sample validation, and avoid treating 1688 matches as proof of equivalent quality.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/qinghu-tiktok-bluesea-collector)
- [Qinghu MCP API Endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API Key Dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu Workflow Permission Check Endpoint](https://www.iqinghu.com/api/desktop/qh/workflow/page?pageNum=1&pageSize=5)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown summaries with optional exported table files for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs prioritize recommendations, key previews, source links, margin assumptions, and Qinghu credit usage when paid tools are called.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
