## Description:

Free Course Share helps Chinese-platform creators produce Xiaohongshu posts about free courses and certificates by combining screening guidance with local scripts for screenshot stitching, certificate redaction, and 3:4 cover generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

External creators and agent users use this skill to evaluate free course topics, prepare certificate/course screenshots, redact sensitive certificate details, generate Xiaohongshu cover images, and draft publishing copy and checklists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Certificate screenshots may retain sensitive personal or account-linked information in verification crops or partially redacted outputs.

Mitigation: Use a private working directory, manually inspect every generated output and verification crop before publishing, and delete verification crops after review.

Risk: OCR-based redaction can miss or misplace text on low-quality images, unusual fonts, or embedded certificate thumbnails.

Mitigation: Prefer manual --box coordinates when OCR misses a target and treat redact.py as an assistive tool rather than a guaranteed privacy control.

## Reference(s):

- [README](README.md)
- [Skill Workflow](SKILL.md)
- [Course Screening Guide](references/course-screening.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated PNG file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local workflow outputs can include course-screening conclusions, two-column screenshot collages, redacted certificate images, 3:4 cover images, verification crops, draft post copy, and publishing checklists.]

## Skill Version(s):

1.1.3 (source: server release metadata and CHANGELOG, released 2026-09-12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
