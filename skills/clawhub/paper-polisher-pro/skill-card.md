## Description:

Helps academic authors self-check AI-writing signals and improve style, terminology, translation quality, and disclosure through local writing reports and polishing guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Academic authors and editors use this skill to review drafts for writing quality, terminology consistency, advisory AI-writing signals, and AI-assistance disclosure. It can report on individual documents or batches without uploading their contents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-detection scores may be mistaken for conclusive evidence of authorship or institutional compliance.

Mitigation: Treat scores as advisory self-checks, review the underlying writing, and follow institutional AI-use and disclosure policies.

Risk: Calibration and freshness commands with --apply can change bundled scoring patterns and undermine reproducibility.

Mitigation: Back up or version-control the skill files before applying changes, then rerun the bundled evaluation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/docsor1212/skills/paper-polisher-pro)
- [Article review workflow](references/article-review-workflow.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, JSON, HTML, CSV]

**Output Format:** [Text and JSON reports; optional HTML paragraph report and CSV batch results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local file processing; reports include advisory scoring and academic-integrity notices.]

## Skill Version(s):

4.1.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
