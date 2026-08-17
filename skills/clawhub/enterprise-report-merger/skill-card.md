## Description:

Merges Excel, PDF, and image-based enterprise reports, fills Word templates, and can generate financial analysis reports when explicitly requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[merlinbeard000](https://clawhub.ai/user/merlinbeard000)

### License/Terms of Use:

MIT-0

## Use Case:

Business analysts, finance teams, and agents use this skill to merge enterprise financial or department reports, populate Word templates, and generate review-ready Excel or Word outputs. Analysis-report generation is appropriate only when the user explicitly requests it and no template is provided.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads user-provided business and financial reports and writes new report outputs.

Mitigation: Use explicit input and output filenames, keep source templates unchanged, and review generated Excel or Word files before relying on them.

Risk: PDF extraction and image-based recognition can misread financial numbers.

Mitigation: Prefer original Excel or text-based PDF inputs, manually verify extracted numbers, and cross-check image/PDF-derived figures before using generated reports.

Risk: Incorrect Word placeholder mappings or reused output paths can produce misleading reports or overwrite important files.

Mitigation: Provide explicit Word placeholder mappings, use separate output paths, and inspect the final document formatting and values.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/merlinbeard000/skills/enterprise-report-merger)
- [Merge Modes](artifact/references/merge_modes.md)
- [PDF Extraction](artifact/references/pdf_extraction.md)
- [Image PDF Guide](artifact/references/image_pdf_guide.md)
- [Standard Report Template](artifact/references/standard_report_template.md)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration, Guidance, Markdown]

**Output Format:** [Markdown guidance with bash commands plus Excel (.xlsx), Word (.docx), and JSON configuration artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local Excel, Word, JSON, and image output files based on user-provided paths.]

## Skill Version(s):

1.0.0 (source: evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
