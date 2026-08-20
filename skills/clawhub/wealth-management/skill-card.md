## Description:

Wealth Management is a Chinese-language assistant suite for fund analysis, client reporting, market snapshots, financial planning, tax planning, and asset allocation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ebandao777-oss](https://clawhub.ai/user/ebandao777-oss)

### License/Terms of Use:

MIT-0

## Use Case:

Financial advisors, private bankers, and wealth-management teams use this skill to route client requests to structured templates for research-style fund analysis, market summaries, client reports, financial plans, tax optimization outlines, and asset-allocation proposals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may handle identifiable or sensitive client financial data.

Mitigation: Use it only with data permitted by the user's organization, minimize client identifiers, and review outputs before sharing.

Risk: The skill can write reports to Notion without clear built-in consent, privacy, or retention controls.

Mitigation: Require explicit user confirmation before any Notion export and apply the organization's retention and access-control policy.

Risk: Reusable model or risk-matrix updates could preserve client-specific assumptions.

Mitigation: Confirm before updating reusable models or risk matrices and remove client-specific details from reusable artifacts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ebandao777-oss/skills/wealth-management)
- [Source repository](https://github.com/ebandao777-oss/wealth-management)
- [Publisher profile](https://clawhub.ai/user/ebandao777-oss)
- [Fund analysis template](references/fund-analysis.md)
- [Client reporting template](references/client-reporting.md)
- [Market snapshot template](references/market-snapshot.md)
- [Financial planning template](references/financial-planning.md)
- [Tax planning template](references/tax-planning.md)
- [Asset allocation template](references/asset-allocation.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown reports, tables, checklists, and structured recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include optional Notion export when a connector is available and the user explicitly confirms export.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter and README changelog mention 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
