## Description:

Use when working with Obsidian vaults, notes, tasks, properties, bases, plugins, or themes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and note-taking power users use this skill to manage named Obsidian vaults, create or edit notes, build Bases views, and author Obsidian-flavored Markdown. It also guides plugin and theme development workflows when the user has confirmed the target vault and commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional MCP fallback and developer debug commands are high-trust actions that can expose or change vault and app state.

Mitigation: Prefer the official Obsidian CLI, require user approval before installing MCP tooling, pin a reviewed MCP version, and use debug or plugin/theme commands only for a confirmed target vault and task.

Risk: Vault commands may read from or modify the wrong Obsidian vault if the target is ambiguous.

Mitigation: Confirm the vault name and command with the user before execution and keep Obsidian CLI access inside the named vault root.

Risk: Generated Bases, formulas, properties, or Obsidian Markdown may fail to render if syntax is invalid.

Mitigation: Validate YAML and formula syntax, quote special characters, and verify rendered output in Obsidian reading view or the Bases interface.

## Reference(s):

- [Obsidian CLI Reference](references/obsidian-cli.md)
- [Obsidian Bases Reference](references/obsidian-bases.md)
- [Obsidian Flavored Markdown Reference](references/obsidian-markdown.md)
- [Bases Functions Reference](references/FUNCTIONS_REFERENCE.md)
- [Callouts Reference](references/CALLOUTS.md)
- [Embeds Reference](references/EMBEDS.md)
- [Properties Reference](references/PROPERTIES.md)
- [Obsidian CLI Documentation](https://help.obsidian.md/cli)
- [Obsidian Download](https://obsidian.md/download)
- [Declared Project URL](https://github.com/afonsoft/skills)
- [ClawHub Skill Page](https://clawhub.ai/afonsoft/skills/obsidian)
- [ClawHub Publisher Profile](https://clawhub.ai/user/afonsoft)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline code blocks, shell commands, YAML, JSON, and Obsidian syntax examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Obsidian CLI or MCP commands only after the user confirms the target vault and action.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
