## Description:

Turns reference images into reusable visual style cards and applies those cards to generate new images from text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

Developers and creators use this skill to extract visual styles from reference images, organize reusable style cards, and create new images from text in those styles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images or generation text may contain sensitive or private content that is sent to a model provider; reference originals are also retained locally.

Mitigation: Use only material authorized for the chosen provider, redact sensitive content before image analysis, and manage retained originals appropriately.

Risk: Optional HTML-to-PNG export uses an unpinned Playwright package and downloads Chromium on first use; generated HTML outputs also contact Google Fonts.

Mitigation: Prefer a reviewed, pinned local Playwright installation and account for the external font request when exporting or sharing HTML.

## Reference(s):

- [Style Card release on ClawHub](https://clawhub.ai/bonniegeng-max/skills/style-card)
- [Reverse style prompt](references/reverse-meta-prompt.md)
- [HTML layout specification](references/html-template.md)
- [Style library index](library/INDEX.json)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Code, Files]

**Output Format:** [Markdown style cards and prompts, with optional standalone HTML and exported PNG images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The available formats depend on the selected style card and the agent's image-generation capabilities.]

## Skill Version(s):

0.6.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
