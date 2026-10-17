## Description:

Generates and evaluates color palettes for interfaces and visual assets, with design tokens, contrast checks, color-vision simulations, and visual previews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers use this skill to select and refine color systems for web interfaces, slides, charts, and other visual assets, then check contrast and color-vision accessibility before delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled MCP server can write to local paths beyond the intended project when run with broad filesystem access.

Mitigation: Review the release before installing and constrain server output paths and permissions to a workspace directory.

Risk: Bundled instructions for collecting third-party palette data may bypass a site's access controls.

Mitigation: Do not use those collection instructions without confirming authorization and compliance.

Risk: Demo validation results may be mistaken for a guarantee of accessible generated interfaces.

Mitigation: Treat demo claims as illustrative and validate contrast, interaction states, and real layouts independently.

Risk: Preference and palette-library write-backs can alter future palette rankings.

Mitigation: Review changes to the profile and library before relying on subsequent recommendations.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/docsor1212/skills/aesthete-agent)
- [Color theory and contrast](artifact/references/color-theory.md)
- [Palette curation](artifact/references/curation.md)
- [Visual critique](artifact/references/critique.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration, Markdown]

**Output Format:** [Markdown guidance, CSS and design tokens, JSON reports, and HTML/SVG previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Palette scores and accessibility checks inform review; final visual and accessibility decisions require human validation.]

## Skill Version(s):

0.5.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
