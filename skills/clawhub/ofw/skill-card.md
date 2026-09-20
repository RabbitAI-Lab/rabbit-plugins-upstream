## Description:

This skill helps an agent work with OurFamilyWizard co-parenting data, including messages, calendar entries, expenses, journal entries, drafts, and attachments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when a user explicitly asks to access or manage OurFamilyWizard co-parenting records. It provides setup and tool guidance for reading and changing OFW messages, calendar events, shared expenses, journal entries, drafts, and attachments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and change sensitive co-parenting records.

Mitigation: Invoke it only for explicit OFW requests and require user confirmation before sending messages, deleting items, changing read state, updating calendar entries, logging expenses, creating journal entries, or moving attachments.

Risk: Some read operations can alter OFW-visible state, including last-seen status or first-viewed timestamps.

Mitigation: Warn the user before operations that may mark content as seen or read, and use refusal or non-marking options when the user wants to preserve unread state.

Risk: Cached OFW data may be stale or incomplete.

Mitigation: Verify current state with the live status or freshness tools before presenting current facts, counts, draft status, or absence of records.

Risk: Credentials and downloaded or cached OFW data are sensitive.

Mitigation: Review credential and cache storage locations and limit access to environments where this legal-record integration is intentionally enabled.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ofw)
- [ofw-mcp npm package](https://www.npmjs.com/package/ofw-mcp)
- [ofw-mcp source repository](https://github.com/chrischall/ofw-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides MCP setup instructions, tool usage guidance, and cautions for sensitive OFW operations.]

## Skill Version(s):

2.18.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
