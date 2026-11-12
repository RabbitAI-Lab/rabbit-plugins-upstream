## Description:

Audits existing PowerPoint decks, reviews rendered slides, and applies targeted layout, copy, and color refinements while preserving the original file by default.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cxdanger123-commits](https://clawhub.ai/user/cxdanger123-commits)

### License/Terms of Use:

MIT-0

## Use Case:

Presenters and teams with existing PowerPoint decks use this skill to find layout and copy issues, review slides visually, and apply consistent, targeted refinements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review notes that some local references could not be resolved, so its benign assessment is incomplete and has medium confidence.

Mitigation: Review the local references and confirm the skill's file access fits your needs before use.

Risk: The skill reads and edits PowerPoint files, which the security review flags as a least-privilege consideration.

Mitigation: Grant access only to the files and folders needed, and keep the default behavior of saving a new file.

## Reference(s):

- [Color strategy](artifact/references/color-strategy.md)
- [Redesign methodology](artifact/references/redesign-methodology.md)
- [PPT美化体检 on ClawHub](https://clawhub.ai/cxdanger123-commits/skills/ppt-polish)

## Skill Output:

**Output Type(s):** [Files, Analysis, Configuration]

**Output Format:** [Refined PowerPoint (.pptx), text audit results, and optional JSON refinement rules.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Windows with WPS Office or Microsoft PowerPoint; the refined deck is saved as a new file by default.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
