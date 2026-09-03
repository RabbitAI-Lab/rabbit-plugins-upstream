## Description:

Removes watermarks, text, logos, price badges, coupon strips, and decorative frames from images, then reconstructs covered areas with image-generation tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and developers use this skill to prepare cleaner product images by removing watermark, text, logo, badge, and promotional overlays before reuse in downstream image workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and prompts may be sent to dlazy or another configured image provider.

Mitigation: Use the skill only with images and prompts that are appropriate to upload to the configured provider, and prefer local files or trusted public image URLs.

Risk: Cloud image generation may consume paid credits.

Mitigation: Run dry-run or cost-estimation flows before paid generation when cost matters.

Risk: Removed or covered image regions are reconstructed and may not preserve the original pixels or facts.

Mitigation: Review generated areas before relying on the result, especially when overlays cover product details or important image content.

Risk: Watermark or logo removal can be misused on images the user does not have rights to edit.

Mitigation: Use the skill only for images the user is authorized to modify and do not use it to misrepresent ownership, branding, legal marks, warnings, certifications, ingredients, or other required labels.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/remove-watermark)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [gpt-image-2 model flags](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, code]

**Output Format:** [Markdown guidance with command examples and optional JSON envelopes from generation scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save generated image files through configured provider CLIs; cloud calls can upload inputs and consume paid credits.]

## Skill Version(s):

1.0.4 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
