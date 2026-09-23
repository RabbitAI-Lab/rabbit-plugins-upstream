## Description:

初中数学概念的理解与重建：学生不是卡在某道题，而是卡在“这个数学概念本身没懂”时用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese K12 students and supporting educators use this skill to rebuild middle-school math concept understanding through everyday analogies, visual reasoning, step-by-step decomposition, and short comprehension checks. It is intended for concept explanations rather than solving a specific problem, generating word-problem equations, tracking mistakes, or assigning leveled practice.

### Deployment Geography for Use:

Mainland China K12 context; localize curriculum assumptions, consent rules, and crisis contacts before use elsewhere.

## Known Risks and Mitigations:

Risk: The skill assumes Chinese-reading users in a Mainland China K12 context, including curriculum framing, consent expectations, and crisis-contact handling.

Mitigation: Install it only for that context, or localize the curriculum assumptions, guardian consent rules, and crisis referral contacts before deployment.

Risk: The skill can maintain or share learning profile information across related skills when memory and cross-skill sharing are enabled.

Mitigation: Review memory, deletion, export, pause, guardian visibility, and cross-skill sharing controls with students and guardians before enabling long-term profiles.

Risk: Generated example or practice items may be incorrect or outside the intended middle-school scope.

Mitigation: Use the bundled AI item self-check requirements before presenting generated items, and require teacher review before adding AI-generated items to formal resources or exams.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-concept-explainer)
- [Initial middle-school math analogy bank](references/analogy-bank.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Concise Chinese tutoring responses, usually plain text or Markdown with short prompts and checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single message budget is limited to 120 Chinese characters; follow-up questions are limited to three rounds; generated practice items require self-check before use.]

## Skill Version(s):

2.2.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
