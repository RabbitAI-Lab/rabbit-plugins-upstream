## Description:

Analyzes a specific tender using historical procurement and award data to suggest bidding, pricing, and competitive strategies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Bidders and procurement teams use this skill to assess whether to pursue a tender, estimate a price range, identify likely competitors, and prepare a risk-aware bidding plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and company search terms are sent to the third-party service.

Mitigation: Share only the project and company details needed for the analysis; check organizational data-sharing policies first.

Risk: Free-trial registration may send a hashed device identifier, and the API key is stored locally.

Mitigation: Review registration before proceeding and restrict access to ~/.zlbx/config.json; do not disclose the API key.

Risk: Shareable HTML reports may include signed links that allow access without logging in.

Mitigation: Treat reports as sensitive and remove or expire signed links before sharing them broadly.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/ai-bidding-strategy-advisor)
- [Bidding analysis workflow](references/workflow.md)
- [Report template](references/report-template.md)
- [API quick reference](references/api-quick.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, HTML files]

**Output Format:** [Markdown bidding-decision report; optional shareable HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a bid recommendation, suggested price range, competitor analysis, risks, actions, and supporting source links.]

## Skill Version(s):

1.0.8 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
