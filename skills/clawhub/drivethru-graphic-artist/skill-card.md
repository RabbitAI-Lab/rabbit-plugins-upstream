## Description:

Graphic-artist tasks for Bacon & Co decorations: generate deterministic product mockups, prepare DTF decoration art for production, and clean degraded flat art before print.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zmtucker](https://clawhub.ai/user/zmtucker)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and decoration-production agents use this skill to composite customer artwork onto blank product photos, prepare DTF production PNGs at print size, upload production assets, update decoration records, and review outputs before customers or production staff see them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can update production decoration records and upload production files.

Mitigation: Install it only for agents authorized to modify Bacon & Co/Odoo decoration data, and restrict access to Odoo credentials and decoration MCP tools.

Risk: The scheduled mockup routine can write mockup images without a person watching each request.

Mitigation: Enable the routine only when unattended updates are acceptable, keep queue limits conservative, and review the per-request outcome log.

Risk: Image-byte transfer paths can be confused with record-update APIs or push large files through the token stream.

Mitigation: Use MCP tool calls for record changes, and reserve raw HTTP only for CDN downloads or the documented production-file upload helper when credentials are present.

Risk: Automated cleanup can alter artwork if applied to the wrong source or without review.

Mitigation: Use cleanup only for degraded flat art, preserve declared inks and letterforms, and inspect the proof image before using the cleaned file for production.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zmtucker/skills/drivethru-graphic-artist)
- [Decoration spec](references/decoration_spec.md)
- [Decoration spec sheet](references/decoration_spec_sheet.pdf)
- [Self-review loop](references/self_review.md)
- [Production-ready DTF workflow](references/production_ready.md)
- [Production cleanup guide](references/production_cleanup.md)
- [Batch mockup routine](references/mockup_routine.md)
- [Iterative feedback](references/iterative_feedback.md)
- [Placement rules schema](references/placement_rules_schema.json)
- [Location dimensions](references/location_dimensions.json)
- [rembg](https://github.com/danielgatis/rembg)

## Skill Output:

**Output Type(s):** [Files, JSON, Shell commands, API Calls, Guidance]

**Output Format:** [PNG image files, JSON receipts, shell commands, API/tool-call instructions, and concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces deterministic image-processing outputs; mockups and cleanup proofs require visual self-review before returning or uploading.]

## Skill Version(s):

0.8.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
