## Description:

This skill should be used when the user asks about OurFamilyWizard (OFW) co-parenting data. Triggers on phrases like "check OFW", "OurFamilyWizard inbox", "OFW messages", "OFW calendar", "OFW expenses", "what did my co-parent say", "log an expense in OFW", "OFW journal", or any request involving co-parenting messages, calendar events, shared expenses, or journal entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People managing co-parenting through OurFamilyWizard use this skill to review messages, calendars, expenses, and journal entries, and to prepare or carry out related account actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Opening unread messages can create permanent timestamps visible to the co-parent.

Mitigation: Restrict activation to explicit OFW requests or an established OFW conversation, and require approval before opening unread messages; use OFW_CONFIRM_MARK_READ or allowMarkRead:false.

Risk: Messages, expense changes, and other shared account actions can affect a legal co-parenting record or become visible to the co-parent.

Mitigation: Review the action preview and obtain explicit user approval before sending, deleting, or making a shared change.

Risk: Credentials and cached family records contain sensitive information, and the separately installed server implementation is unverified.

Mitigation: Protect stored credentials and cached records, and inspect a pinned server release before installation.

## Reference(s):

- [OFW MCP package](https://www.npmjs.com/package/ofw-mcp)
- [Project repository listed in the skill documentation](https://github.com/chrischall/ofw-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration instructions]

**Output Format:** [Markdown and structured text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sensitive family, message, calendar, expense, or journal information.]

## Skill Version(s):

2.25.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
