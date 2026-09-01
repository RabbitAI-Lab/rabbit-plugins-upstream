## Description:

Provides guidance for extracting body text from legacy Word .doc (OLE compound document) files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and document-processing teams use this skill to handle legacy .doc files, including government or regulatory attachments, and to turn extracted text into structured content for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger words such as doc or extract may activate the skill outside the intended legacy Word .doc context.

Mitigation: Confirm that the user is working with a legacy .doc or OLE compound document before applying the extraction guidance.

Risk: Extracted regulatory or legal text may be incomplete or inaccurate if the source document is complex or malformed.

Mitigation: Verify extracted text against the original source document before relying on it for regulatory, legal, or compliance work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/doc-legacy-extract)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Code, Shell commands]

**Output Format:** [Markdown guidance with text extraction steps and optional code or shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable code is bundled in the artifact; outputs should be reviewed against the source document when accuracy matters.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
