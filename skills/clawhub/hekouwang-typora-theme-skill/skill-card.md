## Description:

Supports Typora theme engineering for Chinese and long-form Markdown by editing design tokens, generating CSS, sampling colors, auditing contrast and layout, and troubleshooting themes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Typora users use this skill to tune or build the free light and dark themes, sample reference colors, check contrast and layout, and install or troubleshoot the generated themes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer overwrites existing theme CSS and removes legacy hekouwang-claude CSS files; it does not create automatic backups.

Mitigation: Review the installer targets and keep any files you need to preserve outside Typora's themes folder before installing.

## Reference(s):

- [Theme tokens and styling guide](artifact/references/tokens.md)
- [Typora theme specification and selector guide](artifact/references/typora-spec.md)
- [Theme workflow](artifact/references/workflow.md)
- [Typora custom themes documentation](https://theme.typora.io/doc/Write-Custom-Theme/)
- [Theme preview site](https://huiyonghkw.github.io/hekouwang-typora-theme-lite-skill/)

## Skill Output:

**Output Type(s):** [Code, Configuration, Shell commands, Guidance]

**Output Format:** [CSS, JSON, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates free V2 light and dark Typora theme files and supporting audit/install guidance.]

## Skill Version(s):

2.0.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
