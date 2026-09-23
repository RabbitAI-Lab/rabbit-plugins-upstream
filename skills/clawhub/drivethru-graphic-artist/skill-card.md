## Description:

Creates deterministic apparel and product mockups, cleans flat artwork, removes backgrounds, and prepares DTF production PNGs with sizing, color extraction, upload, and sample-creation steps for Bacon & Co decoration workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zmtucker](https://clawhub.ai/user/zmtucker)

### License/Terms of Use:

MIT-0

## Use Case:

Graphic artists and operations agents use this skill to place existing decoration art on product blanks, tune placement, clean degraded flat art, and prepare DTF production files for decoration records. It is intended for apparel and merchandise production workflows that need deterministic image processing rather than model-generated artwork.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run unattended routines that upload images and change live Odoo production or catalog records.

Mitigation: Review before installing in a live Odoo environment, avoid scheduled routines unless unattended writes are acceptable, and prefer dry-run or explicit operator approval before production uploads, sample creation, state changes, or catalog image updates.

Risk: Incorrect Odoo credentials or vision endpoint settings could send work to the wrong service.

Mitigation: Confirm the Odoo URL, token, and vision endpoint are exactly the intended services before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zmtucker/skills/drivethru-graphic-artist)
- [Publisher profile](https://clawhub.ai/user/zmtucker)
- [Decoration spec](references/decoration_spec.md)
- [Self-review loop](references/self_review.md)
- [Production-ready DTF workflow](references/production_ready.md)
- [Production cleanup workflow](references/production_cleanup.md)
- [Web image routine](references/web_image_routine.md)
- [Placement rules schema](references/placement_rules_schema.json)
- [rembg](https://github.com/danielgatis/rembg)
- [OpenRouter API endpoint](https://openrouter.ai/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON receipts, and generated image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local PNG assets for reviewed mockups, thumbnails, cleaned art, and print-ready DTF production files.]

## Skill Version(s):

0.14.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
