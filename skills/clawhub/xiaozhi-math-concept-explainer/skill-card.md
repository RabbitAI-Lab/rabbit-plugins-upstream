## Description:

Helps Chinese middle-school learners rebuild understanding of math concepts through everyday analogies, visual reasoning, step-by-step decomposition, and short comprehension checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners, guardians, and tutoring agents use this skill when a student is stuck on the meaning of a math concept rather than on a specific problem. It provides concept explanations, guided prompts, generated practice checks, and profile-aware follow-up guidance for junior-middle-school math.

### Deployment Geography for Use:

China Mainland by default; other regions require localized crisis-support channels, curriculum alignment, and minor-data compliance review before student-facing use.

## Known Risks and Mitigations:

Risk: The skill may record math concept mastery in a learning profile and share limited study context with related tutoring skills when memory and sharing are enabled.

Mitigation: Use the disclosed controls to pause memory, disable sharing, export records, correct records, or delete the profile.

Risk: The skill is designed for Chinese K12 tutoring and includes China Mainland safety-channel assumptions.

Mitigation: Before deploying elsewhere, localize crisis-support channels, curriculum expectations, and minor-data consent requirements.

Risk: Generated practice items or analogies can be misleading if they exceed the skill's stated concept boundaries.

Mitigation: Apply the bundled generated-item self-check, keep examples within the junior-middle-school scope, and use the documented analogy boundaries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-concept-explainer)
- [qizhitang publisher profile](https://clawhub.ai/user/qizhitang)
- [初中数学全概念生活类比素材库](references/analogy-bank.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Chinese conversational text and Markdown guidance with short prompts, analogies, checks, and optional practice items]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single responses are constrained to short tutoring turns, with up to three follow-up rounds and generated-item self-checks.]

## Skill Version(s):

2.1.6 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
