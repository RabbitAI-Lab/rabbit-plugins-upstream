## Description:

Turns reference images into reusable, slot-based visual style cards, then uses those cards to create new images from text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

External users and developers can turn a reference image into a reusable style card, maintain a library of visual styles, and apply a selected style to new text or image work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images may contain private or sensitive material, and image analysis sends them to a model service; reference images are also saved locally.

Mitigation: Confirm before sending sensitive references, or use a redacted image, and let the user know the reference is stored locally.

Risk: Image generation may incur charges.

Mitigation: Tell the user about possible generation costs before creating images.

Risk: Rendering HTML examples can contact Google Fonts, and optional PNG export downloads Chromium on first use.

Mitigation: Make these network and download steps clear before rendering or exporting, and pin a reviewed Playwright version for export.

## Reference(s):

- [Reverse style prompt](references/reverse-meta-prompt.md)
- [HTML layout and export guidance](references/html-template.md)
- [HTML base styles](references/html-base.css)
- [Usage gotchas](gotchas.md)
- [Design reference: frontend-slides](https://github.com/zarazhangrui/frontend-slides)
- [ClawHub release page](https://clawhub.ai/bonniegeng-max/skills/style-card)
- [Publisher profile](https://clawhub.ai/user/bonniegeng-max)

## Skill Output:

**Output Type(s):** [Markdown, HTML, Images, Guidance]

**Output Format:** [Markdown style cards, HTML layouts, and generated images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local style-card files; PNG export is optional and uses Playwright with Chromium.]

## Skill Version(s):

0.6.4 (source: SKILL.md frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
