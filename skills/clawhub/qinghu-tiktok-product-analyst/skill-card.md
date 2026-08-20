## Description:

Qinghu AI TikTok product analysis uses Qinghu API data to evaluate a TikTok Shop product's sales performance, channel drivers, related videos, live sessions, influencers, reviews, and stocking or promotion implications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, product analysts, and sourcing teams use this skill to evaluate a known TikTok product, understand whether growth is driven by videos, live commerce, or influencer distribution, summarize review sentiment, and decide stocking and promotion budget posture.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill calls external Qinghu API endpoints and uses a Qinghu token supplied by the user or environment.

Mitigation: Use only the documented Qinghu token sources, avoid exposing tokens in output, and stop with a clear explanation when authentication or account permissions fail.

Risk: Some Qinghu tools may consume paid Qinghu points.

Mitigation: Check the returned free flag, request user approval before paid tools, prefer free tools when available, and report actual Qinghu point consumption from the response envelope.

Risk: The workflow can automatically create local spreadsheet exports for large result sets.

Mitigation: Create exports only for relevant large datasets, provide the file link with a short preview, and avoid pasting large raw tables into chat.

Risk: TikTok product data may lag real-time merchant dashboards, and comment analysis can be sample-limited.

Mitigation: Label numerical conclusions with site, period, cycle, and sample size, and disclose timing or sample limits when presenting stocking or budget guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-tiktok-product-analyst)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Files, Guidance]

**Output Format:** [Markdown analysis with optional local spreadsheet exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local spreadsheet exports for larger result sets; responses should summarize key conclusions and link to exported files when produced.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
