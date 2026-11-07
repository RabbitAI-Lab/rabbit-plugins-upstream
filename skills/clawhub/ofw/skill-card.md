## Description:

Helps users review and manage their OurFamilyWizard co-parenting messages, calendar, expenses, and journal data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using OurFamilyWizard for co-parenting can review messages, calendar events, expenses, and journal entries, and prepare requested changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate for broad co-parenting requests and route them into OurFamilyWizard workflows; the security scan reports partial coverage, so its assessment is incomplete.

Mitigation: Use it for explicitly requested OurFamilyWizard tasks, and review the requested action before proceeding.

Risk: Reading unread messages can mark them as read, and sending messages or changing shared records can affect a legal co-parenting record.

Mitigation: Tell the user when a read may change message status, and get explicit approval after showing a preview before co-parent-visible writes or deletions.

## Reference(s):

- [OFW skill release](https://clawhub.ai/chrischall/skills/ofw)
- [ofw-mcp package](https://www.npmjs.com/package/ofw-mcp)
- [Project repository (listed in skill documentation)](https://github.com/chrischall/ofw-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Structured data, Shell commands, Configuration instructions]

**Output Format:** [Text and structured tool results, with Markdown summaries and shell or configuration snippets as needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include current co-parenting records or proposed updates; confirm before co-parent-visible changes.]

## Skill Version(s):

2.27.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
