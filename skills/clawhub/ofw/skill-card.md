## Description:

This skill should be used when the user asks about OurFamilyWizard (OFW) co-parenting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using an AI agent can retrieve and summarize OurFamilyWizard co-parenting messages, calendar events, expenses, and journal entries, and prepare requested updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: General co-parenting questions can lead to access of sensitive OFW records, and fetching unread messages can permanently reveal when they were viewed.

Mitigation: Require explicit OFW selection for ambiguous requests and approval before fetching unread messages; use allowMarkRead:false when preserving unread status.

Risk: Stored credentials and cached family records are sensitive, and the installed external server version may need review.

Mitigation: Protect credentials and cached family records, and review the external server version before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ofw)
- [ofw-mcp package on npm](https://www.npmjs.com/package/ofw-mcp)

## Skill Output:

**Output Type(s):** [Text, Structured data, Guidance]

**Output Format:** [Text summaries and structured OurFamilyWizard records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available outputs depend on the requested OFW data and server permissions.]

## Skill Version(s):

2.23.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
