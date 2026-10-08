## Description:

Helps academic authors review drafts for possible AI-written passages, writing quality, terminology, translation artifacts, and AI-use labeling, with local reports and polishing guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Academic authors and editors use this local toolkit to self-review Chinese and English drafts, identify passages worth closer inspection, improve clarity and consistency, and check AI-use disclosures before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Drafts may contain sensitive or unpublished writing, and requested operations can create reports or corrected files.

Mitigation: Use only drafts you are authorized to process and review input and output paths before running file-writing commands.

Risk: AI-writing scores and paragraph labels can be uncertain and may be mistaken for definitive authorship judgments.

Mitigation: Use scores to prioritize manual review, not as a verdict; follow institutional AI-use and disclosure rules rather than concealing assistance.

Risk: Optional supervised-model setup writes model files to the local cache.

Mitigation: Use only the author-approved model files accepted by the supplied setup check.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/docsor1212/skills/paper-polisher-pro)
- [Article review workflow](references/article-review-workflow.md)
- [Paragraph-level calibration thresholds](references/para_thresholds.json)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown reports, JSON reports, HTML reports, CSV reports]

**Output Format:** [Text and optional Markdown, JSON, HTML, or CSV files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local processing; some commands write reports or corrected files to user-selected locations.]

## Skill Version(s):

4.9.0 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
