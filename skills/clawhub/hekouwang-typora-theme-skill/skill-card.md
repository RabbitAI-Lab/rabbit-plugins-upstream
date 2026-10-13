## Description:

Guides developers through building, customizing, installing, and checking light and dark Typora themes for CJK long-form writing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and theme authors use this skill to adjust Typora theme colors, typography, and layout; create light and dark variants; troubleshoot installations and fonts; and prepare themes for publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The build, install, unlock, and GitHub publishing scripts are in an external repository, not the reviewed package.

Mitigation: Review those scripts and GitHub API commands in the cloned project before running them.

Risk: Proprietary fonts may be unsuitable for redistribution.

Mitigation: Use proprietary fonts only when locally installed; do not package or redistribute them.

Risk: Browser previews can miss Typora-specific rendering and font fallback issues.

Mitigation: Check the installed theme and fonts in Typora before release.

## Reference(s):

- [Theme project homepage](https://github.com/huiyonghkw/hekouwang-typora-theme)
- [Typora custom theme documentation](https://theme.typora.io/doc/Write-Custom-Theme/)
- [Theme workflow](references/workflow.md)
- [Theme tokens](references/tokens.md)
- [Typora theme specification](references/typora-spec.md)
- [Font strategy](references/fonts.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with CSS, configuration, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Theme changes require the separate project repository; generated CSS and font behavior should be checked in Typora.]

## Skill Version(s):

1.4.1 (source: frontmatter, CHANGELOG, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
