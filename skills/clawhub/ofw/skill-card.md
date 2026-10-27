## Description:

This skill lets an agent work with OurFamilyWizard (OFW) co-parenting data, including messages, calendar events, shared expenses, and journal entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Users can ask an agent to work with their OurFamilyWizard co-parenting data, including messages, calendar events, expenses, and journal entries. The agent can summarize records and assist with supported drafts and updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A generic co-parenting request could trigger access to private OFW records or leave a permanent read receipt on an unread message.

Mitigation: Require the user to select OFW explicitly before accessing records; obtain approval before opening unread messages, and honor allowMarkRead:false when unread status should be preserved.

Risk: Messages and other co-parent-visible changes can create consequential or irreversible records.

Mitigation: Show the full write preview and get explicit approval before confirming a write; do not retry an ambiguous write until its result has been checked.

## Reference(s):

- [ofw-mcp npm package](https://www.npmjs.com/package/ofw-mcp)
- [ofw-mcp project page](https://github.com/chrischall/ofw-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Markdown]

**Output Format:** [Natural-language responses and structured summaries of OFW records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sensitive personal or family information.]

## Skill Version(s):

2.22.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
