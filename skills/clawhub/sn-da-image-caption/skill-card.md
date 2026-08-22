## Description:

Helps agents caption image files, extract chart or table data, describe UI screenshots and diagrams, and turn those captions into structured data, visualizations, CSV, or Excel outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when an uploaded or referenced image needs captioning, OCR-like data extraction, chart/table reconstruction, UI screenshot analysis, diagram understanding, or export to structured files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images are sent to the configured vision API for captioning.

Mitigation: Avoid confidential screenshots unless the endpoint is trusted, and configure the vision API deliberately before use.

Risk: Caption results may be cached locally and can contain sensitive image-derived text.

Mitigation: Use --no-cache for sensitive work, and review or delete the local caption cache when needed.

Risk: Extracted chart or table values may be imperfect or incomplete, especially for dense images.

Mitigation: Verify extracted data against the source image, check row counts and totals, and use targeted prompts or multiple passes for large tables.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-da-image-caption)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Plain text, JSON, Markdown tables, Python snippets, shell commands, CSV, Excel, and generated chart files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May cache image captions locally; JSON output can include detected image type, token usage, and cache status.]

## Skill Version(s):

2026.8.19 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
