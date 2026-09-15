## Description:

Operate Notion through an OOMOL-connected account to read, create, update, move, append, archive, search, and render Notion pages, blocks, databases, data sources, users, and metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to operate Notion workspaces from an agent through the OOMOL oo CLI, including workspace search, page and block retrieval, content updates, database and data source management, and Markdown rendering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path asks users to execute remote installer scripts for the oo CLI.

Mitigation: Review the installer path before use and prefer a verified package or inspected installer.

Risk: The skill can create, update, move, append, archive, or delete Notion content in the connected workspace.

Mitigation: Confirm the connected Notion workspace and require user approval for write or destructive actions before running them.

Risk: The OOMOL connection may have broader Notion workspace access than intended for a specific task.

Mitigation: Confirm which workspace and scopes the OOMOL connection can access before allowing state-changing actions.

## Reference(s):

- [ClawHub Notion Skill](https://clawhub.ai/oomol/skills/oo-notion)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Notion Homepage](https://www.notion.so)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Notion data, metadata, execution IDs, and rendered Markdown through the oo CLI connector.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
