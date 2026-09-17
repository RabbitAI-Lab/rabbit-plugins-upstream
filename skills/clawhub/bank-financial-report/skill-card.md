## Description:

AI-powered financial statement analysis assistant for banks that helps analyze corporate balance sheets, income statements, cash flows, peer comparisons, credit risk, and investment theses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

Bank analysts, credit officers, investment researchers, and portfolio managers use this skill to turn provided financial statement data into ratio analysis, cash-flow diagnostics, peer comparisons, red-flag screening, and draft credit or investment analysis. Outputs require user-supplied source dates, independent data checks, and qualified human review before use in lending or investment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may over-rely on generated financial ratings, credit suggestions, valuation discussion, or fraud indicators as final decisions.

Mitigation: Treat outputs as analytical drafts only; require qualified human review, independent ratio recalculation, and formal approval by the appropriate credit, investment, audit, or compliance function.

Risk: Sensitive borrower, customer, supplier, bank-statement, or non-public financial details could be exposed in prompts.

Mitigation: Provide only summarized and necessary financial metrics, omit confidential originals and detailed counterparty lists, and keep non-public data out of the conversation unless approved controls are in place.

Risk: Regulatory and market facts embedded in the skill may become outdated or may not match the user's jurisdiction or reporting period.

Mitigation: Verify current regulatory requirements, market data, source dates, and accounting basis independently before relying on the analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gechengling/skills/bank-financial-report)
- [ClawHub publisher profile](https://clawhub.ai/user/gechengling)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown financial analysis narrative with tables, checklists, ratings, and model-limitations notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Text-only conversational output; no tool calls, file reads, network requests, or automated submissions are configured in the artifact.]

## Skill Version(s):

5.1.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
