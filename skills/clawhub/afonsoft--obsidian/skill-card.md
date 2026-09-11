## Description:

Helps agents work with Obsidian vaults by using the Obsidian CLI, authoring Obsidian Flavored Markdown, building Bases, and supporting plugin or theme development.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, knowledge workers, and agents working on a user-named Obsidian vault use this skill to create, read, search, and manage notes, build .base views, write Obsidian-specific Markdown, and support plugin or theme development.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide actions that read or modify notes in an Obsidian vault.

Mitigation: Confirm the target vault and each Obsidian command before execution, and keep operations within the named vault.

Risk: The optional mcp-obsidian-cli fallback may install or run a third-party package.

Mitigation: Use the fallback only after user approval and only with a selected, verified, pinned package version.

## Reference(s):

- [Obsidian CLI Reference](references/obsidian-cli.md)
- [Obsidian Bases Reference](references/obsidian-bases.md)
- [Obsidian Flavored Markdown Reference](references/obsidian-markdown.md)
- [Bases Functions Reference](references/FUNCTIONS_REFERENCE.md)
- [Callouts Reference](references/CALLOUTS.md)
- [Embeds Reference](references/EMBEDS.md)
- [Properties Reference](references/PROPERTIES.md)
- [Obsidian CLI Documentation](https://help.obsidian.md/cli)
- [Obsidian Flavored Markdown Documentation](https://help.obsidian.md/obsidian-flavored-markdown)
- [Obsidian Bases Syntax](https://help.obsidian.md/bases/syntax)
- [Publisher Metadata URL](https://github.com/afonsoft/skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with command examples, YAML snippets, and Obsidian-specific syntax]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-approved Obsidian vault and a running Obsidian app for CLI or MCP operations.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact metadata reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
