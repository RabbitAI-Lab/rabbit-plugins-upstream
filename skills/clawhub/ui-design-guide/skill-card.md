## Description:

Use when users need visual direction, interface hierarchy, layout decisions, design specifications, or prototypes before implementing a Web or mini program UI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to establish visual direction, interface hierarchy, layout strategy, typography, color palettes, and prototype requirements before generating web or mini program interfaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may lead an agent to download external images, icons, or fonts with shell commands.

Mitigation: Require the agent to show each HTTPS URL and reason before download, and keep downloads limited to trusted public sources.

## Reference(s):

- [UI Design Activation Checklist](artifact/checklist.md)
- [ClawHub skill listing](https://clawhub.ai/binggg/skills/ui-design-guide)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with design specifications, implementation guidance, code snippets, and shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to fetch public HTTPS assets for UI prototypes; downloads should be reviewed before execution.]

## Skill Version(s):

1.18.43 (source: server release metadata; artifact frontmatter says 2.32.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
