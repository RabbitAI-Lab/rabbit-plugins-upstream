## Description:

This skill helps agents maintain and customize the Hekouwang Typora theme for CJK long-form Markdown, including token-driven CSS builds, color sampling, font verification, local installation, and theme publishing guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, theme maintainers, and technical writers use this skill to adjust Typora theme colors, typography, layout, installation, troubleshooting, and publishing workflows for the Hekouwang light and dark themes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Theme installation may write CSS files and backups into the user's Typora themes directory.

Mitigation: Review the referenced repository scripts before running installation commands and install only when local Typora theme changes are intended.

Risk: The optional local Anthropic font path involves proprietary font assets.

Mitigation: Use the default Inter or system font fallback unless the user deliberately opts in and has the required local font rights.

Risk: Publishing commands can create files, branches, or pull requests in a user's fork.

Mitigation: Review target repository, branch, generated files, and GitHub CLI commands before executing publishing steps.

## Reference(s):

- [Hekouwang Typora Theme Repository](https://github.com/huiyonghkw/hekouwang-typora-theme)
- [Typora Custom Theme Documentation](https://theme.typora.io/doc/Write-Custom-Theme/)
- [Token Reference](references/tokens.md)
- [Font Strategy](references/fonts.md)
- [Typora Theme Specification](references/typora-spec.md)
- [Theme Workflow](references/workflow.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline code, shell commands, and configuration edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local file edits and shell commands for Typora theme build, install, verification, and publishing workflows.]

## Skill Version(s):

1.3.2 (source: server release metadata, frontmatter, CHANGELOG released 2026-08-12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
