## Description:

英语听力训练：按你的词汇量和兴趣生成一段听力材料，练完帮你定位卡在哪一层。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners use this skill to generate level-appropriate English listening passages based on vocabulary level and interests, then practice comprehension through listening, summary, transcript comparison, and targeted follow-up. It supports upper-primary and middle-school listening practice, including new-word capture and listening profile updates when consent controls are enforced.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read or write a child's saved learning, interest, oral, or vocabulary profile without clearly requiring consent checks at each access.

Mitigation: Before deployment, confirm speaker identity, profileEnabled, guardian requirements, and crossSkillSharing are enforced before any profile read or write.

Risk: Personalization based on saved profiles can expose more student information than needed for a listening exercise.

Mitigation: If platform consent controls are not enforced, run the skill with current-session information only or ask the student to choose the topic manually.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-listening-trainer)
- [listening-topic-templates.md](references/listening-topic-templates.md)
- [english-error-dimension-table.md](shared/english-error-dimension-table.md)
- [vocab.md](shared/vocab.md)
- [platform-conventions.md](shared/platform-conventions.md)
- [crisis-exception.md](shared/crisis-exception.md)
- [crisis-referral-protocol.md](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown and conversational text with structured handoff snippets when profiles or vocabulary records are updated]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces listening passages, vocabulary notes, comprehension questions, targeted feedback, progress summaries, and consent-gated profile or vocabulary handoffs.]

## Skill Version(s):

2.1.12 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
