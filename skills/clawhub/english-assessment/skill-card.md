## Description:

An adaptive English assessment assistant that administers quizzes, scores responses, explains mistakes, and tracks learning progress.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-zihan](https://clawhub.ai/user/z-zihan)

### License/Terms of Use:

MIT-0

## Use Case:

English learners use this skill for adaptive CEFR B1–C2 quizzes, scoring, explanations of mistakes, progress tracking, and optional learning-data export or import.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Learning history and assessment results are stored in local files.

Mitigation: Review local file access and retention before use, and protect exported backups.

Risk: An optional Feishu sync uploads exported assessment data to a cloud document with potentially broad sharing permissions.

Mitigation: Sync only after explicit consent and check the resulting document's access settings.

Risk: External searches retrieve exam material from multiple sources.

Mitigation: Review retrieved content for accuracy and suitability before relying on it.

Risk: The search integration exposes API signing material.

Mitigation: The publisher should remove the exposed material and rotate the signing secret before deployment.

## Reference(s):

- [English Assessment on ClawHub](https://clawhub.ai/z-zihan/skills/english-assessment)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON files]

**Output Format:** [Feishu-compatible Markdown for assessments and feedback; JSON for optional local exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Adaptive quiz and error-review modes; cloud backup requires explicit user consent.]

## Skill Version(s):

4.16.1 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
