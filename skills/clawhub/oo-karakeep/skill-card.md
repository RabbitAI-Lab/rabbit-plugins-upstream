## Description:

Karakeep lets agents read, create, update, organize, and delete Karakeep bookmarks, tags, lists, highlights, feeds, assets, backups, and administrative jobs through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

People using Karakeep use this skill to manage saved links, notes, tags, lists, highlights, feeds, assets, and backups from an agent. It also supports administrative recrawl, reindex, inference, and user-management workflows when the connected Karakeep account has admin privileges.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands that pipe downloaded content directly into a shell.

Mitigation: Install the oo CLI only from a verified source, or inspect and verify the installer before executing it.

Risk: Write, destructive, backup, signed URL, and admin actions can change or expose Karakeep account data.

Mitigation: Require clear user confirmation for the exact action, target, and payload, and use admin credentials only for actions that require them.

Risk: Large content, backups, assets, and signed download URLs can expose sensitive saved material.

Mitigation: Request only the needed content, avoid unnecessary includeContent usage, and share temporary file or signed URLs only with intended recipients.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-karakeep)
- [Karakeep homepage](https://karakeep.app)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector calls return JSON data with execution metadata; asset and backup downloads may return temporary file URLs.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
