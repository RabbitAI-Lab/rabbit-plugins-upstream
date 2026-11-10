## Description:

Extracts text, numbers, tables, code, and formulas from images, scans, and multi-page PDFs into text, Markdown, CSV, or JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

People who need content from screenshots, photos, scanned documents, or multi-page PDFs can use this skill to extract printed text and organize it as text, tables, code, or formulas. Handwriting-heavy or degraded images may need manual review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanners report language-model downloads during normal OCR and online dependency installation during setup repair, despite the offline claim.

Mitigation: Review the download and repair behavior first, and use the skill only if those network requests are acceptable.

Risk: The security review is incomplete: 35 of 38 components were scanned, and tool-misuse analysis was partial for three files.

Mitigation: Review the remaining components and the partially analyzed files before relying on the skill.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/lisong2003-lgtm/skills/image-ocr)
- [Feature log](references/feature-log.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV, JSON]

**Output Format:** [Plain text, Markdown tables, CSV, or per-line JSON with coordinates and confidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Batch results can be grouped by filename; JSON can include confidence and uncertainty fields.]

## Skill Version(s):

0.3.8 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
