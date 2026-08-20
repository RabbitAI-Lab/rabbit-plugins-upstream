## Description:

This skill helps agents produce TikTok Shop product-selection reports by combining Qinghu product, video, influencer, seller, product-detail, 1688 sourcing, and Xiaofeng ERP listing workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Commerce operators and agents use this skill to evaluate TikTok Shop product opportunities across demand, content traction, influencer supply, competitor stores, sourcing, and listing readiness. It is intended for heavier product-decision reports rather than quick single-item discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can spend Qinghu credits through paid data tools.

Mitigation: Require user consent before paid calls, rely on the tool-reported pointCost for accounting, and report consumption only when paid calls occur.

Risk: The skill may use a Qinghu token supplied by the user or configured in the environment.

Mitigation: Use the token only for Qinghu API access and avoid exposing credentials in reports, logs, or exported artifacts.

Risk: ERP distribution can push selected product links through the Xiaofeng-to-Doudian listing path.

Mitigation: Confirm the exact links and listing template with the user before any distribution action.

Risk: Exported tables may contain commerce research data from product, video, influencer, seller, or sourcing records.

Mitigation: Prefer file exports with concise previews instead of pasting large raw datasets into chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-tiktok-decision)
- [ClawHub publisher profile](https://clawhub.ai/user/autoagc)
- [Qinghu data API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown report with concise recommendations, optional exported tables, and listing status when distribution is performed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include exported tabular evidence files when tool results contain larger record sets; paid Qinghu credit consumption is reported when paid calls occur.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
