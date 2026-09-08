## Description:

Drivethru Graphic Artist helps agents create deterministic product mockups, prepare DTF production artwork, clean degraded flat art, and update scoped Bacon & Co/Odoo image fields with reviewed outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zmtucker](https://clawhub.ai/user/zmtucker)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and graphic-production agents use this skill to place customer artwork on product blanks, prepare DTF decoration files, clean low-quality flat art, and create reviewed mockup or production outputs for Bacon & Co workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured routines can write mockup, production, and storefront image fields.

Mitigation: Install only for authorized Bacon & Co/Odoo agents and review scheduled routines before enabling them.

Risk: First use can install image-processing packages and may download the rembg model for segmentation.

Mitigation: Pre-approve the dependency and network posture, or use the offline flat-art paths when model download is unavailable.

Risk: Incorrect placement, sizing, or cleanup could misrepresent a product or produce unsuitable print artwork.

Mitigation: Use the documented self-review loop, decoration specifications, and production-scale inspection before returning or uploading outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zmtucker/skills/drivethru-graphic-artist)
- [rembg](https://github.com/danielgatis/rembg)
- [Decoration spec](references/decoration_spec.md)
- [Decoration spec sheet](references/decoration_spec_sheet.pdf)
- [Placement rules schema](references/placement_rules_schema.json)
- [Self-review loop](references/self_review.md)
- [Production cleanup](references/production_cleanup.md)
- [Production ready workflow](references/production_ready.md)
- [Batch mockup routine](references/mockup_routine.md)
- [Web-image routine](references/web_image_routine.md)

## Skill Output:

**Output Type(s):** [files, json, markdown, shell commands, configuration, guidance]

**Output Format:** [PNG image files, JSON receipts, and Markdown guidance with shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include local mockup, cleanup, thumbnail, or DTF production files and, when configured, updates to scoped Odoo image fields.]

## Skill Version(s):

0.9.1 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
