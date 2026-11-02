## Description:

Generates frontend color palettes and UI color schemes with mechanical checks and visual previews to support design decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers use the skill to generate and evaluate color palettes, UI color roles, contrast, and chart palettes. It supports frontend and visual-design work with palette analysis, visual previews, and exportable design tokens or styles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Preview and PASS labels may be mistaken for accessibility certification.

Mitigation: Independently check actual text/background contrast pairs and chart distinguishability before relying on the result.

Risk: Installer and MCP package versions may change over time.

Mitigation: Use reviewed, pinned installer and MCP versions.

Risk: Design preferences and feedback remain in local skill files.

Mitigation: Review locally stored profile and verdict data, and avoid sharing those files unless intended.

## Reference(s):

- [Color theory and contrast guidance](references/color-theory.md)
- [Data visualization color guidance](references/data-viz.md)
- [Critique and review workflow](references/critique.md)
- [Responsive design guidance](references/responsive.md)
- [ClawHub skill release](https://clawhub.ai/docsor1212/skills/aesthete-agent)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, JSON, Code, Configuration, HTML, Markdown, Shell commands]

**Output Format:** [Palette recommendations, analysis reports, visual previews, and exportable design tokens or styles in the selected format.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output format and detail vary by selected task; no fixed token cap.]

## Skill Version(s):

0.14.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
