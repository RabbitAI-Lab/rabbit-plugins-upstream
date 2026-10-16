## Description:

Helps developers build, customize, test, install, and publish light and dark Typora themes for Chinese long-form writing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and theme maintainers use this skill to adjust Typora colors, typography, and layout; diagnose installation or font issues; and prepare theme variants or gallery submissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running commands from a cloned repository may execute scripts that have not been reviewed.

Mitigation: Review scripts before running build, verification, or installation commands.

Risk: Installing the theme into the wrong Typora themes directory may change unintended files or disrupt the theme menu.

Mitigation: Confirm the installation target and keep CSS backups in a subdirectory before installing.

Risk: GitHub API and pull-request commands can publish files to a fork and open a public PR.

Mitigation: Check the repository, branch, files, and command arguments before publishing.

## Reference(s):

- [Hekouwang Typora Theme homepage](https://github.com/huiyonghkw/hekouwang-typora-theme)
- [Typora custom theme documentation](https://theme.typora.io/doc/Write-Custom-Theme/)
- [Theme tokens and tuning](references/tokens.md)
- [Typora theme specification](references/typora-spec.md)
- [Font strategy](references/fonts.md)
- [Theme workflow](references/workflow.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with CSS, configuration, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Theme changes may require a separate repository checkout; paid theme assets are not included in the public skill package.]

## Skill Version(s):

1.5.2 (source: frontmatter, CHANGELOG, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
