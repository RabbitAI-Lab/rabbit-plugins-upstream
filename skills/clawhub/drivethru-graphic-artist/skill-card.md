## Description:

Generates deterministic product mockups, prepares DTF decoration artwork for production, and cleans degraded flat art for Bacon & Co decoration workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zmtucker](https://clawhub.ai/user/zmtucker)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations agents use this skill to composite decoration artwork onto blank products, clean production art, prepare 300 DPI DTF files, extract colors, and update Bacon & Co/Odoo decoration records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make persistent Odoo business-record changes and upload production artwork with bearer credentials.

Mitigation: Install only in a controlled Bacon & Co/Odoo environment, use a least-privileged Odoo MCP token, avoid passing tokens on the command line, and confirm each record-changing workflow before enabling it.

Risk: Raw HTTP uploads with weak destination controls could send production files to the wrong endpoint.

Mitigation: Restrict ODOO_MCP_URL to the intended HTTPS host and verify the upload route before using production credentials.

Risk: Scheduled routines can update many records if queue scope, caps, or rollback behavior are wrong.

Mitigation: Enable routines only after confirming their queue scope, run limits, monitoring, and rollback process.

Risk: Runtime dependency bootstrapping and first-use model downloads may introduce supply-chain and availability risk.

Mitigation: Preinstall locked dependencies where possible and validate any required model download in the target environment before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zmtucker/skills/drivethru-graphic-artist)
- [Decoration spec](references/decoration_spec.md)
- [Decoration spec sheet](references/decoration_spec_sheet.pdf)
- [Placement rules schema](references/placement_rules_schema.json)
- [Self-review loop](references/self_review.md)
- [Production cleanup workflow](references/production_cleanup.md)
- [Production-ready DTF workflow](references/production_ready.md)
- [Batch mockup routine](references/mockup_routine.md)
- [Web-image routine](references/web_image_routine.md)
- [rembg project](https://github.com/danielgatis/rembg)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON receipts, and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce PNG mockups, cleaned art, 300 DPI production PNGs, thumbnails, placement-rule updates, color lists, and Odoo decoration updates.]

## Skill Version(s):

0.12.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
