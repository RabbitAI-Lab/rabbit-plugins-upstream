## Description:

sn-da-image-caption helps agents caption and extract structured data from supported image files using a vision model, then analyze, visualize, or export the results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, data analysts, and agents use this skill to convert screenshots, charts, tables, diagrams, and other supported image files into text captions or structured data for downstream analysis, visualization, and CSV or Excel export.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images may contain confidential screenshots, documents, tables, dashboards, or personal data and are sent to an external vision API.

Mitigation: Review the skill before installing, process only approved data, and use approved API credentials and endpoints.

Risk: Extracted caption text is cached locally by default, which may retain sensitive content after processing.

Mitigation: Use --no-cache for sensitive images, then clear or restrict access to the cache directory after use.

Risk: Caption-based extraction can misread or omit values, especially for dense or large tables.

Mitigation: Verify extracted values against the source image, check row counts and totals, and split large tables into multiple caption passes when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-da-image-caption)
- [Publisher profile](https://clawhub.ai/user/sensenova-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Code, Shell commands, Files, Guidance]

**Output Format:** [Plain text captions, Markdown tables, structured JSON, Python code snippets, shell commands, and exported CSV/Excel/chart files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports single-image and batch captioning; JSON output includes file path, detected image type, description, token usage, and cache status.]

## Skill Version(s):

2026.9.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
