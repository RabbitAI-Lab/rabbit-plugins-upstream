## Description:

Helps users read and manage their own SAP Concur expense reports, expenses, receipts, and travel itineraries through concur-mcp tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees use this skill to review and update their own Concur expense reports, receipts, unassigned charges, and trip details, with explicit confirmation before changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party MCP package and browser bridge can access a signed-in Concur session.

Mitigation: Install only if you trust both components with your Concur session.

Risk: The general GraphQL mutation tool may allow financial actions beyond the skill's stated limits.

Mitigation: Avoid the mutation escape hatch unless the exact operation is understood; never use it for approvals, travel booking, or travel cancellation.

Risk: Some expense changes, declarations, and emailed itineraries cannot be undone.

Mitigation: Review each write preview and obtain the user's explicit confirmation before proceeding.

## Reference(s):

- [ClawHub concur release](https://clawhub.ai/chrischall/skills/concur)
- [concur-mcp npm package](https://www.npmjs.com/package/@chrischall/concur-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration guidance]

**Output Format:** [Markdown guidance, write previews, and a JSON setup example]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the user's signed-in Concur session; changes require an explicit preview confirmation.]

## Skill Version(s):

0.3.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
