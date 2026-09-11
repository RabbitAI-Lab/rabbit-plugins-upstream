## Description:

Helps an agent work with OurFamilyWizard co-parenting data, including messages, calendar events, shared expenses, and journal entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to configure and operate an OurFamilyWizard MCP server for co-parenting records. It supports reading and acting on messages, calendar entries, expenses, and journal content with cautions around irreversible or visible account actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive co-parenting records and visible account state.

Mitigation: Review the skill before installation, run it with limited local permissions, and confirm sensitive reads or writes before execution.

Risk: The release uses unpinned third-party package execution in setup examples.

Mitigation: Use a pinned, reviewed version or commit of ofw-mcp before connecting an OurFamilyWizard account.

Risk: OFW credentials may be exposed if stored in project files or shell commands.

Mitigation: Keep credentials in a protected secret store and avoid committing or sharing local MCP configuration files.

Risk: Sends, deletes, expense creation, uploads, downloads, notification checks, and unread message reads can affect legal co-parenting records or visible account state.

Mitigation: Require explicit user confirmation for irreversible or externally visible actions, and warn before actions that mark messages read or update last-seen status.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ofw)
- [npm package: ofw-mcp](https://www.npmjs.com/package/ofw-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide MCP tool calls that read, create, update, send, delete, upload, or download OurFamilyWizard account data.]

## Skill Version(s):

2.16.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
