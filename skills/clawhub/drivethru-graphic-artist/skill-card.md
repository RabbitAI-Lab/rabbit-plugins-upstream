## Description:

Helps agents create deterministic product mockups, prepare DTF artwork at print size, clean up degraded flat art, and update decoration records for Bacon & Co workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zmtucker](https://clawhub.ai/user/zmtucker)

### License/Terms of Use:

MIT-0

## Use Case:

Graphic artists and operations agents use this skill to place logos on garments, tune placements, prepare DTF production PNGs, and update decoration/sample records. It is intended for Bacon & Co decoration workflows that require reviewed visual output before storefront or production updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify live Odoo decoration, sample, state, and product-image records.

Mitigation: Install it only where those changes are intended, use dedicated Odoo credentials with the narrowest feasible permissions, and review scheduled routines before enabling them.

Risk: Customer artwork or product images may be sent to an external vision-review provider.

Mitigation: Restrict MOCKUP_VISION_BASE_URL to an approved provider and control MOCKUP_VISION_API_KEY or OPENROUTER_API_KEY access before processing customer assets.

Risk: The skill can run unattended and upload generated mockups or production files.

Mitigation: Require operator review for routine configuration and pin or preinstall dependencies where possible before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zmtucker/skills/drivethru-graphic-artist)
- [Decoration spec](references/decoration_spec.md)
- [Production-ready DTF workflow](references/production_ready.md)
- [Production cleanup workflow](references/production_cleanup.md)
- [Self-review loop](references/self_review.md)
- [Web-image routine](references/web_image_routine.md)
- [Placement rules schema](references/placement_rules_schema.json)
- [rembg project](https://github.com/danielgatis/rembg)
- [OpenRouter API endpoint](https://openrouter.ai/api/v1)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Files, API Calls]

**Output Format:** [Markdown guidance with shell commands, JSON receipts, and PNG/JPEG image file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write mockup and production image files, maintain placement-rule state, and upload production or storefront images to Odoo when credentials are configured.]

## Skill Version(s):

0.15.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
