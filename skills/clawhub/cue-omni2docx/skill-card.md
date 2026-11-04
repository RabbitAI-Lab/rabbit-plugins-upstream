## Description:

Rebuilds Omni-parsed source documents as structured Word, HTML, PDF, and PowerPoint files with page anchors and source references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and document analysts use this skill to turn Omni-parsed material into structured Word, HTML, PDF, or presentation documents with page anchors, tables, citations, and source appendices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External Omni parsing may upload document contents, and retention details are unclear.

Mitigation: Confirm what is uploaded and how it is retained before enabling Omni; use local --md conversion when external processing is unsuitable.

Risk: The --prose skip control may leave confidential text in the output, and validation does not compare merged document contents.

Mitigation: Remove sensitive text from the source, inspect speaker notes, and independently review merged documents before sharing.

Risk: Remote image URLs and installer or repository revisions need review.

Mitigation: Review remote image URLs and use reviewed installer versions and repository revisions.

## Reference(s):

- [Omni Reader configuration](https://cuecue.cn/hub/omni-reader)
- [Omni Reader setup guide](https://github.com/sensedeal/cue-skills/blob/main/cue-omni-reader/references/setup.md)
- [ClawHub skill release](https://clawhub.ai/huhoo/skills/cue-omni2docx)

## Skill Output:

**Output Type(s):** [DOCX files, HTML files, PDF files, PPTX files]

**Output Format:** [Structured Word, HTML, PDF, and PowerPoint documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Page-anchored content with source references; presentation output is organized as a briefing deck.]

## Skill Version(s):

0.6.19 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
