## Description:

Helps academic authors review Chinese and English drafts for AI-writing signals, terminology, style, and disclosure labels, with local reports and revision guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT No Attribution (MIT-0)

## Use Case:

Academic authors and editors use this skill to self-review drafts, check consistency and AI-use labeling, and receive actionable polishing guidance without uploading documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Batch review can read sensitive drafts across a selected directory.

Mitigation: Provide only approved document paths and scope recursive batches carefully.

Risk: Freshness or recalibration runs with --apply change local detector reference data.

Mitigation: Review planned changes and back up local reference data before applying them.

Risk: AI-risk estimates may be mistaken or misused to conceal AI assistance.

Mitigation: Treat scores as self-review guidance, verify findings, and follow applicable AI-use disclosure rules.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/docsor1212/skills/paper-polisher-pro)
- [Article review workflow](references/article-review-workflow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Text or structured reports with revision suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional local HTML or CSV reports; texts under 100 characters receive no AI-risk verdict.]

## Skill Version(s):

4.4.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
