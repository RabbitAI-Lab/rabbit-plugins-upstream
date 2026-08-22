## Description:

Using a fixed classroom camera, the skill analyzes student facial expressions, head pose, and interaction signals to produce class-level engagement scores, anonymous low-engagement seat coordinates, heatmaps, alerts, teacher suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers, school staff, smart-classroom operators, and education-technology developers use this skill to analyze classroom video or image inputs for aggregate engagement trends and anonymous seat-level reminders. It is intended as teaching support, not student ranking, discipline, performance evaluation, psychological diagnosis, or individual profiling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student classroom videos or images may be processed by a third-party cloud service.

Mitigation: Use only with school and parent consent, confirm the publisher's retention and access controls, and avoid submitting footage unless cloud processing is acceptable.

Risk: Cloud report history is tied to persistent user-linked state.

Mitigation: Treat report history as identity-linked data, restrict access to authorized school personnel, and periodically review stored reports and account linkage.

Risk: Engagement signals and low-engagement seat coordinates may be misused for individual ranking, discipline, or performance evaluation.

Mitigation: Use outputs only as aggregate classroom support for teachers, and prohibit student ranking, disciplinary action, parent communications, psychological diagnosis, or individual profiling based on the skill output.

Risk: Facial-expression and attention estimates can misclassify normal classroom behavior such as thinking, note-taking, or transitions between teaching phases.

Mitigation: Interpret results as advisory signals, review them with human classroom context, and avoid acting on short-term dips without corroborating observations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-classroom-engagement-analysis-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Student classroom engagement API documentation](artifact/references/api_doc.md)
- [Shared SMYX analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured analysis text, with optional saved report output files and report export links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include engagement scores, emotion distributions, anonymous seat coordinates, heatmap links, alerts, teacher suggestions, history report lists, and cloud report export URLs.]

## Skill Version(s):

1.0.9 (source: server release metadata and target metadata; artifact/SKILL.md frontmatter states 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
