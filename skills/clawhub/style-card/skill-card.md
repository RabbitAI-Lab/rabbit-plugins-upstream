## Description:

Turns reference images into reusable visual style cards and applies saved styles to new content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

Content creators and designers use the skill to turn a reference image into a reusable visual style guide, then apply saved styles to new content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HTML export can install Playwright globally when it is missing, despite the skill's zero-dependency claim.

Mitigation: Before HTML export, remove the automatic global-install fallback and arrange a fixed local Playwright installation through a separate setup step.

Risk: HTML rendering contacts Google Fonts, and image generation may incur provider charges.

Mitigation: Check that the network request is acceptable and confirm provider pricing before generating images.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bonniegeng-max/skills/style-card)
- [Reverse style analysis prompt](references/reverse-meta-prompt.md)
- [HTML output structure guide](references/html-template.md)
- [HTML base styles](references/html-base.css)
- [Workflow design inspiration: frontend-slides](https://github.com/zarazhangrui/frontend-slides)

## Skill Output:

**Output Type(s):** [Text and guidance, Markdown, Code, Images, Shell commands]

**Output Format:** [Markdown style cards and image prompts, standalone HTML/CSS/JavaScript, and exported PNG images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Style cards can be added to a reusable library; visual results depend on the selected image-generation model.]

## Skill Version(s):

0.6.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
