## Description:

Helps agents read, create, update, and delete content in a connected Notion workspace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams with a connected Notion workspace use this skill to find and read pages, blocks, comments, and data sources, or to create and update workspace content with approval for changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup suggests running remote installers directly in a shell.

Mitigation: Use the official installation guide and verify installer provenance before executing setup commands.

Risk: Write and destructive actions can alter or remove Notion content.

Mitigation: Review the exact target and payload before approving writes; require explicit approval for destructive actions.

Risk: Notion operations are routed through OOMOL's connected service.

Mitigation: Install only if you trust OOMOL to handle operations in the connected workspace.

## Reference(s):

- [Notion skill on ClawHub](https://clawhub.ai/oomol/skills/oo-notion)
- [oo CLI documentation and source](https://github.com/oomol-lab/oo-cli)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown, with commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include retrieved Notion content or confirmation of requested changes.]

## Skill Version(s):

1.0.5 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
