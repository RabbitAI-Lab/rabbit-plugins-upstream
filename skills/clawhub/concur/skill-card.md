## Description:

This skill should be used when the user asks about SAP Concur through the concur-mcp tools — expense reports, expenses, available (unassigned) card transactions and e-receipts, receipt images, or Concur Travel trips.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees use this skill to review their own Concur expense reports, expenses, card transactions, receipts, and travel itineraries. It can also make changes after the user explicitly approves the exact preview.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill accesses a signed-in Concur session through the npm server and browser bridge.

Mitigation: Trust both components before granting session access, and consider pinning a reviewed package version.

Risk: Some actions can permanently delete data, submit reports, certify a missing receipt, replace attendees, or send itinerary email.

Mitigation: Review each exact preview and confirm it explicitly; take extra care with deletions, submissions, declarations, attendee changes, and email.

Risk: Receipt upload access may include more local folders than needed.

Mitigation: Narrow the allowed receipt folders to the locations required for the task.

## Reference(s):

- [Concur MCP npm package](https://www.npmjs.com/package/@chrischall/concur-mcp)
- [Project page listed in the skill documentation](https://github.com/chrischall/concur-mcp)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/concur)

## Skill Output:

**Output Type(s):** [Text, Guidance, Files]

**Output Format:** [Natural-language summaries and instructions; receipt images may be returned inline or saved as files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read or change the user's own Concur data; all writes require explicit confirmation.]

## Skill Version(s):

0.3.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
