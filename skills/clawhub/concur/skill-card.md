## Description:

This skill should be used when the user asks about SAP Concur through the concur-mcp tools — expense reports, expenses, available (unassigned) card transactions and e-receipts, receipt images, or Concur Travel trips. Triggers on phrases like "Concur", "expense report", "submit my expenses", "what's unsubmitted", "reimbursement status", "attach this receipt", "card charges not on a report", "my upcoming trip", or any request to read or change the user's own Concur expense or travel data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees use the skill to review their own SAP Concur expense reports, transactions, receipts, and trips, and to make supported changes after reviewing a preview and explicitly confirming it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party server uses the user's signed-in Concur session.

Mitigation: Install only if you trust the third-party server with that session.

Risk: Some expense actions can have consequential or irreversible effects, including deletions, submissions, declarations, and emails.

Mitigation: Review every change preview and require explicit approval, especially for these actions.

Risk: The security review does not establish the external server's runtime safety.

Mitigation: Consider pinning the package version and limiting receipt upload folders.

## Reference(s):

- [Concur MCP package](https://www.npmjs.com/package/@chrischall/concur-mcp)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/concur)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Concur records and tool responses summarized in natural language or returned as structured data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions return a preview and require explicit user confirmation before changes are made.]

## Skill Version(s):

0.3.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
