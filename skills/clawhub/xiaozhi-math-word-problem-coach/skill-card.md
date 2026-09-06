## Description:

A Chinese-language junior secondary math tutoring skill that coaches students through translating word-problem text into equations using a three-step quantity-relationship modeling method.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners and education agents use this skill to help junior secondary students identify quantities, state relationships in natural language, and convert those relationships into equations for math word problems. It focuses on modeling before calculation rather than solving equations after they are formed.

### Deployment Geography for Use:

China mainland by default; localize crisis support, curriculum alignment, and minor-data consent before use in other regions.

## Known Risks and Mitigations:

Risk: Optional learning-record memory and cross-skill sharing can involve student math progress data.

Mitigation: Confirm consent before enabling memory or sharing; use the artifact's pause, delete, export, and sharing-restriction controls when requested.

Risk: The skill's default safety contacts, curriculum assumptions, and minor-data consent model are designed for a China-mainland Chinese K12 setting.

Mitigation: Localize emergency contacts, curriculum alignment, and consent requirements before deploying outside that setting.

Risk: AI-generated practice or transfer questions may be invalid, over-scoped, or numerically unsuitable.

Mitigation: Apply the included item self-check before presenting generated questions: solve them, verify uniqueness and sufficient conditions, keep numbers grade-appropriate, and stay within the junior secondary scope.

Risk: Image OCR may be unavailable or unreliable for photographed word problems.

Mitigation: Ask the learner to type the known conditions and the question in one line when the image cannot be read.

## Reference(s):

- [Five word-problem modeling patterns](artifact/references/modeling-patterns.md)
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-word-problem-coach)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Plain text or Markdown tutoring dialogue with short prompts, hints, and equations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The artifact limits each coaching turn to short prompts, uses a staged hint ladder, and hands off equation solving after the modeling step.]

## Skill Version(s):

2.1.10 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
