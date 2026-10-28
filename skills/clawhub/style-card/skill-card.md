## Description:

Reverse-engineers a reference image into a reusable style card, then uses that card to generate new images from text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

Creators and developers use the skill to turn reference images into reusable visual style cards, build a style library, and create new graphics from text in a selected style.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images may contain sensitive or private content when sent to an AI service for analysis.

Mitigation: Confirm the image can be shared first, or use a redacted image.

Risk: HTML output contacts Google Fonts, and optional PNG export may download Chromium through Playwright.

Mitigation: Use local fonts for offline or reproducible output, and review and pin the Playwright installation when exporting PNGs.

## Reference(s):

- [Style Card on ClawHub](https://clawhub.ai/bonniegeng-max/skills/style-card)
- [Reverse-engineering prompt template](references/reverse-meta-prompt.md)
- [HTML output template](references/html-template.md)

## Skill Output:

**Output Type(s):** [Markdown, HTML, Image-generation prompts, PNG images]

**Output Format:** [Markdown style cards, standalone HTML, and generated PNG images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reusable style-card library; optional HTML-to-PNG export.]

## Skill Version(s):

0.6.4 (source: server-resolved release metadata, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
