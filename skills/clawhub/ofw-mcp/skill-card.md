## Description:

This skill helps an agent work with OurFamilyWizard co-parenting data, including messages, calendar events, expenses, and journal entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill for explicit OurFamilyWizard tasks such as checking co-parenting messages, reviewing calendar events, managing shared expenses, and drafting or sending OFW communications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The broad trigger could activate sensitive OurFamilyWizard read/write tools for general co-parenting requests.

Mitigation: Use the skill only for explicit OFW tasks and confirm user intent before accessing account data.

Risk: Some reads can change user-visible state, such as last-seen status or marking unread messages as read.

Mitigation: Warn the user and require confirmation before calling notifications or reading unread messages when visible status could change.

Risk: Write operations can affect legal co-parenting records, including sent messages, drafts, events, expenses, and journal entries.

Mitigation: Require clear confirmation before sending messages, deleting drafts or events, creating expenses or journal entries, or updating calendar data.

Risk: Cached message or draft state can be stale and lead to incorrect statements about current OFW records.

Mitigation: Use live status, freshness, and completeness checks before reporting current states, counts, or whether a draft still exists.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/ofw-mcp)
- [npm Package](https://www.npmjs.com/package/ofw-mcp)
- [Artifact-Linked GitHub Repository](https://github.com/chrischall/ofw-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use OFW tools that read or update sensitive account data; require clear user confirmation before operations that change records or visible read status.]

## Skill Version(s):

2.10.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
