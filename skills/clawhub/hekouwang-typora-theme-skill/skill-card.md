## Description:

Helps agents maintain and adapt the Hekouwang Typora light and dark themes by generating CSS from design tokens, sampling colors, verifying font rendering, and guiding installation and publishing workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and theme maintainers use this skill to modify or create Typora themes for CJK long-form Markdown, tune theme tokens, validate rendering behavior, install themes locally, and prepare a theme gallery submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shell scripts or publishing commands referenced by the source repository may change local files or create public repository updates.

Mitigation: Review scripts such as install.sh and publishing commands before execution, and run publishing steps only when public repository changes are intended.

Risk: Optional local Anthropic font usage may involve proprietary font licensing constraints.

Mitigation: Use the local Anthropic font option only after reviewing the licensing note; rely on distributable fallback fonts when publishing or sharing theme assets.

Risk: Typora can silently keep stale CSS, list backup files as themes, or fall back to system fonts without an error.

Mitigation: Install backups into subdirectories, fully restart Typora after CSS changes, and run the documented font and rendering verification probes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huiyonghkw/skills/hekouwang-typora-theme-skill)
- [Hekouwang Typora Theme Homepage](https://github.com/huiyonghkw/hekouwang-typora-theme)
- [Typora Custom Theme Documentation](https://theme.typora.io/doc/Write-Custom-Theme/)
- [tokens.md](references/tokens.md)
- [typora-spec.md](references/typora-spec.md)
- [fonts.md](references/fonts.md)
- [workflow.md](references/workflow.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, file paths, CSS/token configuration details, and validation steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include proposed edits to theme tokens, build and install commands, font checks, color sampling steps, and publishing guidance.]

## Skill Version(s):

1.3.3 (source: server release metadata, frontmatter, and changelog dated 2026-08-12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
