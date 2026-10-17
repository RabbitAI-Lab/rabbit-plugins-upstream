## Description:

Helps users review and manage their own SAP Concur expenses, reports, receipts, and travel itineraries through the unofficial concur-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees use this skill to inspect their Concur reports, expenses, unassigned charges, receipts, and trips, and to prepare and explicitly confirm changes to their own expense data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad write authority could change or delete real expense data, including through the GraphQL mutation tool.

Mitigation: Use dedicated tools when available, review the exact preview, and require explicit user confirmation for every write.

Risk: Submitting reports, certifying missing receipts, or sending itineraries can create consequential records or emails.

Mitigation: Explain the consequence to the user and obtain specific confirmation before each action.

Risk: The server uses the user's signed-in Concur browser session.

Mitigation: Install only from a trusted publisher and approve pairing only in the browser holding the intended Concur session.

## Reference(s):

- [Concur skill on ClawHub](https://clawhub.ai/chrischall/skills/concur)
- [concur-mcp npm package](https://www.npmjs.com/package/@chrischall/concur-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration instructions]

**Output Format:** [Text and Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Concur data summaries and write previews; changes require explicit user confirmation.]

## Skill Version(s):

0.3.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
