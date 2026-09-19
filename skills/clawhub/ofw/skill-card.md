## Description:

This skill helps an agent work with OurFamilyWizard (OFW) co-parenting data, including messages, calendar events, shared expenses, journal entries, drafts, and attachments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to configure and operate an OFW MCP integration for co-parenting messages, calendar items, expenses, journals, drafts, and attachments. It is intended for sensitive account workflows where the agent must verify freshness, completeness, lifecycle state, and user approval before taking actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent OFW account access can expose sensitive co-parenting and legal-record data.

Mitigation: Install only when ongoing OFW account access is acceptable, prefer task-specific use, and remove or rotate stored OFW credentials when the integration is no longer needed.

Risk: Send, delete, create, update, upload, and privacy-impacting read operations can change legal-record data or reveal activity.

Mitigation: Confirm every such action with the user, avoid silent notification or message reads, and warn before reads that may mark messages read or update last-seen state.

Risk: Cached OFW message or draft state can be stale and may not reflect current server state.

Mitigation: Use live status or freshness checks before making current-state claims, quoting counts, or sending, deleting, or replacing drafts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ofw)
- [ofw-mcp npm package](https://www.npmjs.com/package/ofw-mcp)
- [ofw-mcp GitHub repository linked by artifact](https://github.com/chrischall/ofw-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, code]

**Output Format:** [Markdown with JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes OFW MCP setup steps, tool-call guidance, workflow sequencing, freshness checks, and caution notes for sensitive account actions.]

## Skill Version(s):

2.17.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
