## Description:

Helps coding agents create and review frontend color systems with palette matching, color validation, accessibility checks, and visual previews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the skill to select, validate, and export color palettes and semantic tokens for user interfaces, charts, and visual assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan is incomplete and reports scope and validation mismatches; its suspicious verdict is not a finding of malicious behavior.

Mitigation: Review the skill's behavior before installation and independently check accessibility or safety claims before relying on them.

Risk: The skill records accept/reject feedback in local profile and critique files, so its use can persist user preferences and review notes.

Mitigation: Review the write-back behavior and limit filesystem access to the intended skill workspace.

Risk: The security guidance flags unpinned installation routes.

Mitigation: Use a pinned release where available and inspect the installed files before use.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/docsor1212/skills/aesthete-agent)
- [Online showcase](https://docsor1212.github.io/aesthete-agent/)
- [Color theory reference](artifact/references/color-theory.md)
- [Critique and evidence reference](artifact/references/critique.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Text, Markdown, Code, Configuration, HTML]

**Output Format:** [Palette recommendations, validation reports, CSS or JSON design tokens, HTML previews, and targeted code edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update a local preference profile and critique notes when recording user verdicts.]

## Skill Version(s):

0.23.0 (source: server-resolved release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
