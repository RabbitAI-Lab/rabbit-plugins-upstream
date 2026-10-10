## Description:

Helps users read and manage their own SAP Concur expense reports, expenses, receipts, and travel itineraries through an unofficial MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People with a signed-in SAP Concur account use this skill to review and manage their own expense reports, card transactions, receipts, and trip details. Changes require explicit approval of a preview.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The unofficial MCP server accesses a signed-in Concur session and can read or change sensitive expense and receipt data.

Mitigation: Review the package before installing, use it only with an account you are authorized to access, and approve only the intended changes.

Risk: The generic GraphQL mutation tool can make account changes beyond the task-specific workflow.

Mitigation: Prefer task-specific tools; inspect every preview carefully and explicitly confirm only the exact change requested.

## Reference(s):

- [Concur skill on ClawHub](https://clawhub.ai/chrischall/skills/concur)
- [concur-mcp package](https://www.npmjs.com/package/@chrischall/concur-mcp)
- [concur-mcp source linked by the skill](https://github.com/chrischall/concur-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text with report details and previews for proposed changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return downloaded receipt images; write actions require explicit confirmation.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
