## Description:

Stores and tags Chinese writing materials, retrieves them by topic, and summarizes confirmed usage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students use this skill to organize Chinese writing materials with source and topic tags, find relevant items for a writing topic, and review usage records when they consent to tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student writing materials and usage records may be stored across sessions or shared with another skill.

Mitigation: Check the learning-profile dependency and platform retention and deletion controls before enabling sharing; honor consent and the “这次不要记忆” pause command.

Risk: The skill is intended for school-age learners, including elementary students.

Mitigation: Require a parent or teacher to accompany elementary-school use.

## Reference(s):

- [语文素材库 on ClawHub](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-material-library)
- [Learning DNA profile schema](https://xiaozhi-skills.openclaw.dev/schemas/dna-profile.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language text or Markdown lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tagged material entries, source notes, retrieval suggestions, and summaries based on confirmed usage records.]

## Skill Version(s):

2.12.6 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
