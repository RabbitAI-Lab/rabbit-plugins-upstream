## Description:

An interactive English assessment companion that adapts questions to past performance and provides scores, explanations, error review, and progress tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-zihan](https://clawhub.ai/user/z-zihan)

### License/Terms of Use:

MIT-0

## Use Case:

English learners use this skill for adaptive CEFR B1–C2 practice assessments, feedback on weak areas, error review, and learning-progress tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill embeds web-search signing material that could expose credentials.

Mitigation: Remove and rotate the exposed signing secret; keep credentials out of model-visible skill text.

Risk: Searches rely on a local token broker and fetch content from external sources.

Mitigation: Review the token broker and limit search and diagnostic requests to trusted, documented sources before installation.

Risk: Assessment history is stored locally, and optional Feishu backups transfer it to the cloud.

Mitigation: Protect local files and obtain explicit consent for each Feishu upload; check document access and sharing settings.

## Reference(s):

- [English Assessment on ClawHub](https://clawhub.ai/z-zihan/skills/english-assessment)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON data]

**Output Format:** [Interactive Feishu-compatible Markdown messages and optional local JSON export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes scored reports, explanations, and progress summaries; optional Feishu backup requires user consent.]

## Skill Version(s):

4.16.2 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
