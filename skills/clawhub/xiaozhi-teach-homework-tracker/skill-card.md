## Description:

Helps independent teachers track in-class practice and student-provided schoolwork or exam errors, classify recurring mistakes, and plan what to cover next lesson.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers use this Chinese-language skill to track in-class exercises and student-provided schoolwork, group errors by learning dimension, and prepare a next-lesson diagnosis. It stores limited student-alias progress records, with teacher confirmation before persistent weakness labels are added.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent student tracking could expose sensitive information about minors.

Mitigation: Use aliases instead of real names, omit answer text and personal details, confirm sharing consent, and use pause, export, or deletion controls when needed.

Risk: Mistake classifications or recurring-weakness labels could misdirect teaching or reach later reports.

Mitigation: Have teachers review every writeback and confirm a weakness label before adding it to a student's profile.

Risk: AI-generated validation questions may be incorrect or unsuitable for a student.

Mitigation: Manually check each generated question before using it with a student.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-homework-tracker)
- [Completion tracking views](artifact/references/completion-tracking-views.md)
- [Error reflow checklist](artifact/references/error-reflow-checklist-template.md)
- [Next-lesson pre-diagnosis template](artifact/references/pre-diagnosis-output-template.md)
- [Student homework profile template](artifact/references/student-homework-profile-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Chinese-language tracking summaries, lesson-planning reports, and structured workspace updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tracks student aliases and error dimensions; proposed persistent weakness labels require teacher confirmation.]

## Skill Version(s):

2.11.0 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
