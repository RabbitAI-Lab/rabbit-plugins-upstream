## Description:

A chart-first skill that turns a book’s key ideas, quotations, and structure into publication-style visual reading notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yjkj999999](https://clawhub.ai/user/yjkj999999)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, educators, and readers use the skill to transform a book’s key ideas and quotations into concise, chart-led visual reading notes for sharing or presentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The black-and-white image converter can silently overwrite and delete an existing image.

Mitigation: Avoid converting original files until the helper uses a unique temporary file; work on copies in a fresh output directory and preserve any existing DESIGN.md.

Risk: Image analysis may expose confidential page content if sent to a remote service.

Mitigation: Choose local image analysis for confidential pages.

Risk: Optional dependency installation may change the local environment.

Mitigation: Review optional dependency installations separately.

## Reference(s):

- [Content Framework](references/content-framework.md)
- [Graphics Toolchain](references/graphics-toolchain.md)
- [Portrait Magazine Layout](references/ng-magazine-layout.md)
- [Output Pipelines](templates/output-pipelines.md)

## Skill Output:

**Output Type(s):** [Files, HTML, PDF, PPTX, Images, Guidance]

**Output Format:** [Visual reading notes as HTML, PDF, PPTX, or a long image]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chart-led layouts with concise text; slide-style or portrait magazine formats.]

## Skill Version(s):

2.6.0 (source: SKILL.md frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
