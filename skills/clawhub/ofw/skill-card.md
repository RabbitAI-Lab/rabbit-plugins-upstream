## Description:

This skill helps an agent work with OurFamilyWizard co-parenting data, including messages, calendar events, expenses, and journal entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect and manage OurFamilyWizard co-parenting records, including inbox messages, sent-message status, drafts, calendar events, shared expenses, attachments, and journal entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive OurFamilyWizard co-parenting records to the agent.

Mitigation: Install only when that access is acceptable, and limit use to agents and workspaces that are trusted to handle legal co-parenting records.

Risk: Credentials may be configured in plaintext files or project-scoped MCP settings.

Mitigation: Prefer environment variables or a secret manager, and avoid storing OFW credentials in shared project files.

Risk: Some operations can change legal-record state, including sending messages, deleting drafts, changing calendar entries, creating expenses, and marking messages read.

Mitigation: Require explicit user confirmation before sends, deletes, calendar changes, expense creation, and actions that mark messages read or update last-seen status.

Risk: Cached messages, attachments, or downloaded files may persist locally with unclear retention behavior.

Mitigation: Review cache and attachment storage locations before use, and clear local data according to the user's retention requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ofw)
- [npm package](https://www.npmjs.com/package/ofw-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tool names, MCP configuration snippets, workflow steps, and cautions about OFW state changes.]

## Skill Version(s):

2.19.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
