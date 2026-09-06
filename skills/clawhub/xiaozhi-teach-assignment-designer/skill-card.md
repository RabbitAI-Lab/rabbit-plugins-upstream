## Description:

作业设计师 helps teachers turn a single class assignment into differentiated, time-boxed task cards with scoring rubrics, feedback templates, and completion-summary guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External educators use this skill to design or revise differentiated homework assignments, scoring rubrics, concise feedback templates, and teacher-reviewed completion summaries for elementary and middle-school classes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Assignment writeback could save homework records or completion summaries before a teacher has reviewed them.

Mitigation: Show every homeworkAssignments writeback as pending and save it only after explicit teacher approval.

Risk: AI-generated homework items may contain incorrect answers, unsuitable difficulty, or unverified variants.

Mitigation: Run the bundled item self-check and label AI-generated items as requiring teacher verification before formal use.

Risk: Homework feedback can expose sensitive student or family information if written at the wrong level of detail.

Mitigation: Use de-identified aggregate feedback, enforce sharing and parent-consent controls, and omit real names, addresses, rankings, and unsubmitted-student lists.

Risk: Student distress or safety disclosures may appear while the teacher is working on assignments.

Mitigation: Stop assignment generation and follow the bundled crisis referral protocol, recording only that referral occurred.

## Reference(s):

- [作业评分标准与分层任务卡模板](references/assignment-rubric.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown task cards, rubrics, feedback templates, and structured assignment-record guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes per-task estimated time, total estimated assignment time, teacher verification notes for AI-generated items, and optional completion-summary guidance.]

## Skill Version(s):

2.1.10 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
