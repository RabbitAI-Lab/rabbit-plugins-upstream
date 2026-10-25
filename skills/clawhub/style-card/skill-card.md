## Description:

Turns reference images into reusable style cards and applies those styles to create visuals from new text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

Creators and developers use this skill to turn a reference image into a reusable visual style card, then apply it to new text to produce consistent visual assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PNG export may silently install browser tooling globally.

Mitigation: Provision a reviewed Playwright version locally and disable the automatic global-install fallback before exporting.

## Reference(s):

- [ClawHub release](https://clawhub.ai/bonniegeng-max/skills/style-card)
- [Reverse style analysis prompt](references/reverse-meta-prompt.md)
- [HTML visual template guidance](references/html-template.md)
- [Export and generation gotchas](gotchas.md)
- [Frontend Slides inspiration](https://github.com/zarazhangrui/frontend-slides)

## Skill Output:

**Output Type(s):** [Markdown, HTML, Images, Prompts]

**Output Format:** [Markdown style cards and prompts; HTML and PNG visual assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Style cards are reusable; HTML exports can be rendered to PNG.]

## Skill Version(s):

0.6.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
