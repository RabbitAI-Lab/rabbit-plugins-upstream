## Description:

This skill should be used when the user asks about OurFamilyWizard (OFW) co-parenting data. Triggers on phrases like "check OFW", "OurFamilyWizard inbox", "OFW messages", "OFW calendar", "OFW expenses", "what did my co-parent say", "log an expense in OFW", "OFW journal", or any request involving co-parenting messages, calendar events, shared expenses, or journal entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People managing co-parenting through OurFamilyWizard can use the skill to retrieve and review messages, calendar events, expenses, and journal entries, and to prepare or make updates when requested. It also provides setup and usage guidance for connecting to OFW.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan flags credential-handling guidance that may expose OFW passwords; the scan was partial and did not assess every referenced component.

Mitigation: Review how OFW credentials are stored and passed. Avoid exposing them in files, shell history, or command arguments, and review unresolved referenced components before relying on the scan.

Risk: Reading some unread messages changes their read status, and sending messages or changing shared records can have lasting effects in a co-parenting record.

Mitigation: Follow the skill's confirmation steps before sending or deleting anything, and check the read-status consequences before opening unread messages.

## Reference(s):

- [ofw-mcp package](https://www.npmjs.com/package/ofw-mcp)
- [Repository listed in the skill documentation](https://github.com/chrischall/ofw-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text and Markdown, including OFW summaries and records, setup instructions, and configuration or command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include extracted attachment content or calendar data in iCalendar format]

## Skill Version(s):

2.28.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
