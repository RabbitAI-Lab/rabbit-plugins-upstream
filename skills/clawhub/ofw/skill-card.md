## Description:

This skill should be used when the user asks about OurFamilyWizard (OFW) co-parenting data. Triggers on phrases like "check OFW", "OurFamilyWizard inbox", "OFW messages", "OFW calendar", "OFW expenses", "what did my co-parent say", "log an expense in OFW", "OFW journal", or any request involving co-parenting messages, calendar events, shared expenses, or journal entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users who manage co-parenting through OurFamilyWizard can review messages, calendar events, expenses, and journal entries, and prepare requested updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The broad activation wording may route unrelated calendar, expense, or journal requests to OFW.

Mitigation: Review the trigger and setup instructions before enabling the connector, and install only if this routing is intended. ClawScan reported partial coverage, so available scan evidence is incomplete.

Risk: Reading an unread message may mark it read, and sending messages or changing shared records can have lasting effects in a co-parenting account.

Mitigation: Follow the skill's confirmation steps for writes and warn the user before actions that change read status.

## Reference(s):

- [OFW skill release page](https://clawhub.ai/chrischall/skills/ofw)
- [ofw-mcp package information](https://www.npmjs.com/package/ofw-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Natural-language responses and action previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize co-parenting messages, calendar events, expenses, and journal entries, or prepare requested updates.]

## Skill Version(s):

2.27.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
