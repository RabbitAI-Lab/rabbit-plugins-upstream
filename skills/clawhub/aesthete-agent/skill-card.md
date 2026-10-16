## Description:

Helps agents choose, validate, and export accessible color systems for frontend and visual design using palette matching, contrast checks, and visual review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and design-focused agents use this skill to select color palettes, check contrast and color-blind accessibility, generate design tokens, and review visual options for interfaces, charts, and other digital artwork.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated files and preference learning may change local files, including the profile and palette library.

Mitigation: Review output locations and keep backups of profile.json and palettes.json before enabling write-back.

Risk: Third-party palette harvesting instructions may conflict with site permissions or terms.

Mitigation: Avoid harvesting unless authorized and after reviewing the site's terms.

Risk: Unpinned install paths can execute code that differs from a previously reviewed release.

Mitigation: Use pinned releases or a reviewed local checkout for the MCP server.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/docsor1212/skills/aesthete-agent)
- [Color theory and accessibility](artifact/references/color-theory.md)
- [Five-lens critique method](artifact/references/critique.md)
- [Palette selection methodology](artifact/references/curation.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration, Markdown]

**Output Format:** [Text and Markdown guidance; CSS and JSON color tokens; optional HTML previews and critique reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write generated files and update the local preference profile or palette library.]

## Skill Version(s):

0.4.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
