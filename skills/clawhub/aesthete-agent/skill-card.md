## Description:

Helps developers create and compare frontend color palettes and themes with automated contrast checks and visual previews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers use the skill to generate, evaluate, and preview color systems for frontend interfaces, charts, and other visual materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Accessibility badges and aggregate PASS results may overstate accessibility, particularly for charts and status indicators.

Mitigation: Independently inspect the rendered design, including charts and status indicators, before relying on accessibility claims.

Risk: Preference learning writes verdicts to local skill files.

Mitigation: Review and back up affected local files before accepting verdict write-back.

Risk: Unreviewed or unpinned installer and MCP versions may change behavior.

Mitigation: Use reviewed, pinned installer and MCP versions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/docsor1212/skills/aesthete-agent)
- [Color theory and validation](references/color-theory.md)
- [Visual critique guidance](references/critique.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration, JSON, Shell commands]

**Output Format:** [Text, Markdown, JSON, CSS, HTML, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output depends on the selected palette or theme task; automated results should be reviewed in context.]

## Skill Version(s):

0.8.0 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
