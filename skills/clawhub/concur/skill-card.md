## Description:

This skill should be used when the user asks about SAP Concur through the concur-mcp tools — expense reports, expenses, available (unassigned) card transactions and e-receipts, receipt images, or Concur Travel trips.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees use this skill to review and manage their own SAP Concur expense reports, expenses, receipts, and travel details. It supports expense and receipt updates with confirmation and can read trip information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The raw API tool can reach financial approval actions beyond the skill’s stated personal-expense scope.

Mitigation: Prefer dedicated expense tools and disable the generic mutation tool where possible, especially for accounts with approval authority. Review every write preview and pin a reviewed server version; the security evidence does not establish that the separately downloaded server enforces these safeguards.

## Reference(s):

- [npm package](https://www.npmjs.com/package/@chrischall/concur-mcp)
- [Project repository (linked in the skill file)](https://github.com/chrischall/concur-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Files]

**Output Format:** [Text or Markdown; receipt images may be returned inline or saved as files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include expense, receipt, report, and trip details; write previews are presented for confirmation.]

## Skill Version(s):

0.4.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
