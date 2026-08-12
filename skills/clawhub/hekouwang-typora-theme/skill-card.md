## Description:

Helps developers and Typora theme maintainers build, modify, install, verify, and publish the Hekouwang light and dark Typora themes using token-driven CSS generation, color sampling, and font-rendering checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT

## Use Case:

Developers, designers, and Typora theme maintainers use this skill to adjust CJK long-form writing themes, troubleshoot local Typora theme installation issues, verify font and color behavior, and prepare theme updates for publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation and publishing commands can modify local Typora theme files or create public theme-gallery pull requests.

Mitigation: Review proposed shell commands before execution and confirm the target files, backup location, and publishing destination.

Risk: Theme verification can pass in a headless browser while still differing inside Typora's embedded Chromium runtime.

Mitigation: After building and installing a theme, fully quit and reopen Typora and perform a visual check in the actual application.

Risk: Font licensing mistakes can occur if proprietary fonts are bundled or redistributed.

Mitigation: Use local font probing for proprietary fonts, keep redistributable fonts under documented licenses, and review font license metadata before packaging.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huiyonghkw/skills/hekouwang-typora-theme)
- [Project homepage](https://github.com/huiyonghkw/hekouwang-typora-theme)
- [Typora custom theme documentation](https://theme.typora.io/doc/Write-Custom-Theme/)
- [Token workflow reference](references/tokens.md)
- [Typora selector and theme specification reference](references/typora-spec.md)
- [Font strategy reference](references/fonts.md)
- [Theme workflow reference](references/workflow.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are agent-facing recommendations, edits, and commands for Typora theme files; commands should be reviewed before execution.]

## Skill Version(s):

1.3.1 (source: frontmatter, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
