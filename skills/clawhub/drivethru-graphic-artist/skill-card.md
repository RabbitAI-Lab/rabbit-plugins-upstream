## Description: <br>
Helps agents create deterministic product mockups, clean degraded flat artwork, remove backgrounds, and prepare DTF decoration files for Bacon & Co production workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zmtucker](https://clawhub.ai/user/zmtucker) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External operators and production-support agents use this skill to place logos on blank product photos, tune mockups, prepare DTF artwork at production size, and update decoration records after review. It is intended for Bacon & Co graphic-production workflows where deterministic image processing and human-facing review are required. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can update Odoo decoration records and upload production artwork when asked to make art production-ready. <br>
Mitigation: Install it only in environments authorized for Bacon & Co decoration work, scope Odoo credentials, and verify target record IDs before production actions. <br>
Risk: Incorrect print size, placement, color extraction, or cleanup could produce misleading proofs or unsuitable production files. <br>
Mitigation: Review generated mockups, cleanup proofs, production files, dimensions, and colors before accepting or uploading final artwork. <br>
Risk: Production uploads depend on an Odoo MCP endpoint and token when using the upload helper. <br>
Mitigation: Use a trusted HTTPS ODOO_MCP_URL, keep tokens scoped, and fall back to approved MCP image-setting tools when direct upload credentials are unavailable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zmtucker/skills/drivethru-graphic-artist) <br>
- [Publisher profile](https://clawhub.ai/user/zmtucker) <br>
- [Decoration spec](references/decoration_spec.md) <br>
- [Production ready procedure](references/production_ready.md) <br>
- [Production cleanup procedure](references/production_cleanup.md) <br>
- [Self-review loop](references/self_review.md) <br>
- [Iterative feedback](references/iterative_feedback.md) <br>
- [Location dimensions](references/location_dimensions.json) <br>
- [Placement rules schema](references/placement_rules_schema.json) <br>
- [rembg](https://github.com/danielgatis/rembg) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON receipts from helper scripts, and generated PNG files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include deterministic mockup, thumbnail, cutout, cleanup proof, and production PNG files; production workflows also rely on user review of sizes, colors, target records, and generated proofs.] <br>

## Skill Version(s): <br>
0.7.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
