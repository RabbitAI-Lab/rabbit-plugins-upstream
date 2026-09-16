## Description:

AI-powered financial statement analysis assistant for banks that analyzes balance sheets, income statements, cash flows, peer comparisons, credit risk, and investment theses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

Bank analysts, investment researchers, credit officers, and portfolio managers use this skill to review provided financial statement data, calculate ratios, compare peers, identify red flags, and draft human-reviewed credit or investment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may include confidential financial statements, bank records, borrower details, or other non-public business information.

Mitigation: Provide summarized key metrics where possible, avoid pasting unnecessary raw records, and handle any confidential inputs under the workspace's approved data controls.

Risk: Generated ratios, ratings, fraud indicators, or peer comparisons may be incorrect when inputs are incomplete, unsourced, stale, or use inconsistent accounting assumptions.

Mitigation: Verify source dates, units, accounting scope, and calculations before relying on the analysis.

Risk: Financial analysis output may be mistaken for an audit opinion, legal advice, lending approval, or investment decision.

Mitigation: Use the skill as analytical support only and require qualified human review and approval for audit, lending, legal, or investment workflows.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown report text with tables, ratio calculations, risk ratings, and review notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Conversation-only analytical support; users provide sourced financial data and review outputs before use.]

## Skill Version(s):

5.1.2 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
