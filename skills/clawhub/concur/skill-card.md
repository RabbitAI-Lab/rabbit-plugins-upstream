## Description:

Helps users review and manage their own SAP Concur expenses, reports, card transactions, and receipts, and view their travel trips through an unofficial integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees use this skill to check and update their own expense reports, expenses, unassigned transactions, and receipts, or review upcoming and past trips. Report submission and other changes require explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An authenticated session can expose sensitive financial and travel details to an external integration.

Mitigation: Review the external package before installing, pair only the intended signed-in browser session, and limit use to your own Concur data.

Risk: The raw GraphQL mutation option may change financial or workflow data beyond the skill's stated scope.

Mitigation: Prefer dedicated tools; review the exact preview and scope of each proposed change before explicitly confirming it.

Risk: Deleting expenses or reports and submitting reports may have irreversible consequences.

Mitigation: Check affected items and downstream effects in the preview before approval; never repeat a write solely because its follow-up verification failed.

## Reference(s):

- [Concur skill listing](https://clawhub.ai/chrischall/skills/concur)
- [concur-mcp package](https://www.npmjs.com/package/@chrischall/concur-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include expense and trip summaries or change previews; writes require explicit user confirmation.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
