## Description:

This skill helps agents work with OurFamilyWizard (OFW) co-parenting data, including messages, calendar events, shared expenses, and journal entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent read, summarize, and manage OFW co-parenting records across messages, calendars, expenses, and journal entries. It is useful when the user explicitly wants help checking OFW data or preparing OFW updates with appropriate confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive legal co-parenting records.

Mitigation: Install it only when the user intends the agent to access their OFW account and store OFW credentials carefully.

Risk: Some OFW actions are visible or irreversible, including sending messages, marking messages read, updating last-seen status, deleting items, and changing calendar, expense, or journal records.

Mitigation: Require explicit user confirmation before write operations or actions that change read/last-seen state.

Risk: Cached message and draft data can be stale or incomplete.

Mitigation: Use the skill's freshness, completion, and live status checks before presenting current OFW state as fact.

## Reference(s):

- [ofw-mcp npm package](https://www.npmjs.com/package/ofw-mcp)
- [ofw-mcp source repository](https://github.com/chrischall/ofw-mcp)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ofw)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Shell commands, Configuration]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce OFW tool calls that read, create, update, delete, send, download, or upload account data.]

## Skill Version(s):

2.15.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
