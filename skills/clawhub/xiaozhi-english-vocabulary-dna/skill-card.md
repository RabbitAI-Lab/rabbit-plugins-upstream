## Description:

为中小学生安排英语词汇间隔复习，生成每日到期词卡、课前预热和词汇进度反馈。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and their guardians use this Chinese-language skill to build an English vocabulary list, review words on an adaptive schedule, and prepare for upcoming lessons. Educators may use its progress feedback where sharing is authorized.

### Deployment Geography for Use:

Mainland China; localize crisis contacts, legal defaults, and language expectations elsewhere.

## Known Risks and Mitigations:

Risk: Student vocabulary history or progress could be stored or shared without appropriate permission.

Mitigation: Enable profile memory and cross-skill or guardian sharing only with the appropriate student or guardian consent; honor pause, export, and deletion requests.

Risk: Unwanted or excessive vocabulary reminders could disrupt students.

Mitigation: Require reminder consent, limit the skill to one consolidated daily card, and allow students to pause reminders.

Risk: China-specific crisis contacts and legal assumptions may be unsuitable in other regions.

Mitigation: Confirm the student's location and localize crisis contacts, legal defaults, and language expectations before deployment outside mainland China.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-english-vocabulary-dna)
- [High-school English vocabulary reference](references/english-hs-vocabulary.md)
- [Vocabulary preview topics](references/vocabulary-radar-topics.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Chinese-language vocabulary cards and review guidance; consent-gated profile and reminder handoffs in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [At most one consolidated due-word card per day; proactive reminders depend on enabled reminders and consent.]

## Skill Version(s):

2.11.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
