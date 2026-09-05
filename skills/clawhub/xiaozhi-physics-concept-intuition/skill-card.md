## Description:

初中物理概念的直觉建立器，用生活类比、头脑实验、公式推导三种模型把概念从“背下来”变成“真的懂了”。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners and education agents use this skill to help Chinese middle-school students build intuition for physics concepts before applying formulas. It focuses on concept explanation, guided mental experiments, analogy-based reasoning, and short validation checks rather than full problem-solving workflows.

### Deployment Geography for Use:

China mainland; deployments elsewhere require localized crisis channels, curriculum alignment, and minor-data consent review.

## Known Risks and Mitigations:

Risk: The skill can write or use concept mastery records for minors when platform memory is enabled.

Mitigation: Require explicit profile consent, honor view/correct/delete/export controls, and enforce cross-skill and parent-sharing consent before any record is shared.

Risk: The skill is written for Chinese middle-school physics and China-mainland safety channels.

Mitigation: Localize curriculum assumptions, crisis referral contacts, and minor-data consent requirements before deploying outside mainland China.

Risk: Analogy-based explanations can oversimplify physics concepts or leave misconceptions unchecked.

Mitigation: Use the built-in validation checks, counterexample questions, and concept-transfer prompts before marking a concept as mastered.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-concept-intuition)
- [physics-analogy-bank.md](references/physics-analogy-bank.md)
- [platform-conventions.md](shared/platform-conventions.md)
- [crisis-referral-protocol.md](shared/crisis-referral-protocol.md)
- [vocab.md](shared/vocab.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese conversational tutoring responses with structured explanations, questions, checks, and consent-gated memory notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose concept mastery writeback or reminder handoff only when the platform capability and user consent evidence are present.]

## Skill Version(s):

2.1.6 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
