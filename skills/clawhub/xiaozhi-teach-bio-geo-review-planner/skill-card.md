## Description:

Helps Chinese middle- and high-school biology and geography teachers plan examination review from local exam guidance, class-level learning needs, and the time remaining before the exam.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Biology and geography teachers in Chinese K–12 schools use the skill to map their current local exam guidance to curriculum topics, prioritize class-level weak areas, schedule lab or fieldwork preparation, and draft a day-by-day review plan. Teachers review the draft before using it with students or saving it.

### Deployment Geography for Use:

China (subject to local examination guidance)

## Known Risks and Mitigations:

Risk: Review plans could expose student information or be saved without authorization.

Mitigation: Use aggregated class-level learning data and pseudonyms; exclude real names, individual scores and rankings, and save or change plans only after explicit teacher confirmation.

Risk: Unpublished examination materials could be disclosed.

Mitigation: Request only publicly available local exam guidance; do not enter unpublished questions, answer keys or scoring materials.

Risk: A plan based on another region's rules could misdirect preparation.

Mitigation: Have the teacher supply current local exam guidance, and mark missing requirements for teacher confirmation instead of guessing.

Risk: Unsafe independent lab or fieldwork practice.

Mitigation: Keep lab practice in teacher-supervised school facilities and fieldwork under adult supervision; follow the skill's lab-safety guidance.

## Reference(s):

- [Biology and geography exam review reference](references/bio-geo-exam-review.md)
- [Laboratory safety guidance](shared/lab-safety.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown review schedules and topic-priority tables; optional structured review plan after teacher confirmation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local exam details must come from the teacher; unconfirmed details are flagged rather than guessed.]

## Skill Version(s):

2.8.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
