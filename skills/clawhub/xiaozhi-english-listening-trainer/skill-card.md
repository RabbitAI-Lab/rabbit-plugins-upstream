## Description:

根据学生的词汇水平和兴趣生成英语听力练习，并帮助定位理解障碍。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in upper primary through high school use this skill to practice English listening with interest-matched passages, comprehension questions, targeted follow-up, and progress summaries.

### Deployment Geography for Use:

China (mainland); other regions require localized curriculum, safeguarding contacts, and minor-data consent rules.

## Known Risks and Mitigations:

Risk: Student profiles from other skills may be read without an explicit consent check.

Mitigation: Enforce consent before profile access: require profileEnabled=true for long-term profiles and crossSkillSharing=true before reading other skills' Learning DNA, vocabulary DNA, or speaking profiles.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-english-listening-trainer)
- [Listening topic templates](references/listening-topic-templates.md)
- [English error dimensions](shared/english-error-dimension-table.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text and Markdown practice materials or progress reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Listening playback requires platform speech support; otherwise the skill offers a clearly labeled reading alternative.]

## Skill Version(s):

2.7.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
