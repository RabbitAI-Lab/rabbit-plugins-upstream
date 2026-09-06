## Description:

free-course-share helps agents produce Xiaohongshu posts for free courses and certificates, including course screening, screenshot stitching, certificate redaction, vertical cover generation, draft copy, and a publishing checklist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

Creators and agent users use this skill to turn verified free-course and certificate material into Xiaohongshu-ready assets and copy. It is intended for local production of screening notes, image files, Markdown/text drafts, shell commands, and posting guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Certificate screenshots can contain names, email addresses, employee IDs, registry IDs, account identifiers, or other personal information, and OCR redaction may miss or misplace text.

Mitigation: Inspect every script-generated verification crop before posting; use manual boxes, cropped images, or official desensitized examples when redaction confidence is uncertain.

Risk: Setup includes Python packages and system-level tesseract installation commands.

Mitigation: Install in a dedicated virtual environment from a trusted package index, and treat sudo apt commands as host-level changes that require operator approval.

Risk: Free-course availability, certificate terms, learner counts, and deadlines can change after a post is drafted.

Mitigation: Verify course pages and official notices immediately before publishing, and avoid claims that are not supported by current source pages.

Risk: Company or institution certificates may have confidentiality or sharing restrictions.

Mitigation: Publish only certificates the user owns and has permission to share; when rights are unclear, avoid using the certificate image.

## Reference(s):

- [Course screening guide](references/course-screening.md)
- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/free-course-share)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Text, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown and text guidance with inline shell commands, plus generated PNG image files from local scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and tesseract; image scripts depend on Pillow, NumPy, OpenCV, pytesseract, and Chinese OCR data.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
