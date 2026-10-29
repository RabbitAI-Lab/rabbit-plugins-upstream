## Description:

Reverse-engineers a reference image into a reusable style card, then uses the card to create new images in that style from text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to describe a reference image as a reusable visual style, build a style-card library, and create new visual content that follows a selected card.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images or text may contain sensitive or private content that is sent to the selected model.

Mitigation: Share only material you are authorized to send; confirm first when content may be sensitive, or use a redacted image.

Risk: Reference originals are saved locally during the workflow.

Mitigation: Store and handle the local originals according to their sensitivity.

Risk: HTML rendering contacts Google Fonts, and optional PNG export uses Playwright, which downloads Chromium on first use.

Mitigation: Account for the external font request and use a reviewed, pinned Playwright version before PNG export.

## Reference(s):

- [Style reverse-engineering prompt](references/reverse-meta-prompt.md)
- [HTML template guide](references/html-template.md)
- [HTML base stylesheet](references/html-base.css)
- [frontend-slides (workflow inspiration)](https://github.com/zarazhangrui/frontend-slides)

## Skill Output:

**Output Type(s):** [Markdown, HTML, Images, Files]

**Output Format:** [Reusable style-card Markdown, image-generation prompts, HTML documents, or generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The output depends on the selected style card and rendering engine; optional PNG export uses Playwright.]

## Skill Version(s):

0.6.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
