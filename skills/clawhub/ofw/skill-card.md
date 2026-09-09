## Description:

This skill guides an agent in using the ofw-mcp server for OurFamilyWizard messages, calendar events, shared expenses, and journal entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to configure and operate an MCP server for OurFamilyWizard co-parenting workflows, including messages, calendar items, expenses, attachments, and journal entries. It is intended for tasks where freshness, user confirmation, and careful handling of legal co-parenting records matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive co-parenting records and OFW credentials.

Mitigation: Install only after reviewing the package or commit, keep credentials out of project files and git, and restrict local file permissions.

Risk: Some reads can mark OFW messages as seen, and send/delete actions are irreversible or legally sensitive.

Mitigation: Require explicit user confirmation before message reads that may mark content viewed and before any write, send, upload, or delete action.

Risk: Cached OFW data can be stale or incomplete while still appearing usable.

Mitigation: Check freshness, completeness, and live status before presenting current-state conclusions or counts.

## Reference(s):

- [ofw-mcp npm package](https://www.npmjs.com/package/ofw-mcp)
- [ofw-mcp source link listed in artifact](https://github.com/chrischall/ofw-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Text]

**Output Format:** [Markdown guidance with JSON configuration examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cautions for confirmation, cache freshness, irreversible sends/deletes, and message-read side effects.]

## Skill Version(s):

2.16.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
