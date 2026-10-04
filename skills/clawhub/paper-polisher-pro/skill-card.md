## Description:

Provides local Chinese and English academic-writing self-checks, AI-writing signals, and guidance on style, terminology, translation, and disclosure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT No Attribution (MIT-0)

## Use Case:

Academic authors use this skill to review their own drafts for writing quality, terminology consistency, possible AI-writing signals, and AI-use labeling before submission. Its scores are advisory, not proof of authorship or a substitute for institutional disclosure requirements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Processing sensitive or unpublished manuscripts reads local files and may save reports or revised text nearby.

Mitigation: Use only manuscripts and output locations you are authorized to handle; review generated files before sharing.

Risk: AI-writing scores and rewriting advice may be mistaken for definitive authorship findings or used to evade disclosure.

Mitigation: Treat scores as advisory, review revisions yourself, and follow institutional AI-use and disclosure policies.

Risk: Optional supervised detection requires separately obtained model and tokenizer files.

Mitigation: Obtain optional model files from the publisher channel and use the supplied setup verification before enabling them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/docsor1212/skills/paper-polisher-pro)
- [Article review workflow](references/article-review-workflow.md)
- [Publisher documentation](https://docsor.cn)

## Skill Output:

**Output Type(s):** [Text, Guidance, JSON reports, CSV reports]

**Output Format:** [Markdown guidance and local text, JSON, or CSV reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include advisory risk scores and writing suggestions; some operations write files beside the input manuscript.]

## Skill Version(s):

4.5.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
