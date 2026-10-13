## Description:

Helps employees view and manage their own SAP Concur expense reports, receipts, and travel itineraries through an unofficial MCP integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees use this skill to review and update their own Concur reports and expenses, handle receipts, and check travel itineraries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration accesses sensitive expense and travel information through the signed-in Concur browser session.

Mitigation: Install only when this access is intended; revoke bridge trust when no longer needed.

Risk: Broad activation and raw GraphQL escape hatches may expose more Concur data or write scope than an ambiguous request requires.

Mitigation: Clarify that the request concerns Concur and prefer narrowly scoped read tools.

Risk: Confirmed writes can delete expenses, submit reports, certify missing receipts, or send emails; some actions cannot be undone.

Mitigation: Review the exact write preview and obtain explicit user approval before confirming each action.

## Reference(s):

- [ClawHub concur release](https://clawhub.ai/chrischall/skills/concur)
- [concur-mcp package](https://www.npmjs.com/package/@chrischall/concur-mcp)
- [Repository linked by the skill (not verified release provenance)](https://github.com/chrischall/concur-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration instructions]

**Output Format:** [Markdown and structured tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions require a preview and explicit user confirmation; receipt images may be saved locally.]

## Skill Version(s):

0.3.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
