## Description:

为小学高段和初中学生按词汇量、兴趣话题和年级生成英语听力材料，并通过四步练习定位词义、结构或语速卡壳点。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students, parents, and educators use this skill to generate level-matched English listening practice, guide a listen-retell-compare-review workflow, and identify whether comprehension breaks down at vocabulary, sentence structure, or speed.

### Deployment Geography for Use:

Global; operators outside mainland China should localize school assumptions, minor-consent rules, and crisis-contact guidance before student use.

## Known Risks and Mitigations:

Risk: The skill is designed around Chinese K12 tutoring assumptions, student profile memory, and cross-skill learning-data sharing.

Mitigation: Deploy only where those uses are intended and consent-enabled; localize language, school assumptions, minor-consent rules, and crisis contacts before using it outside mainland China.

Risk: Listening workflows can expose student learning records or cross-skill profile updates.

Mitigation: Honor the documented privacy controls for viewing, correcting, deleting, pausing, exporting, and limiting sharing of the listening profile.

Risk: The skill may encounter self-harm, abuse, bullying, or serious despair signals during tutoring interactions.

Mitigation: Stop the learning flow and follow the crisis exception protocol, including adult referral and localized emergency-contact guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-listening-trainer)
- [Listening topic templates](references/listening-topic-templates.md)
- [English error dimension table](shared/english-error-dimension-table.md)
- [Platform conventions and localization guidance](shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown conversational guidance with generated listening passages, comprehension questions, vocabulary notes, and progress summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include consent-gated profile handoff records and reminder handoff suggestions when supported by the host platform.]

## Skill Version(s):

2.2.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
