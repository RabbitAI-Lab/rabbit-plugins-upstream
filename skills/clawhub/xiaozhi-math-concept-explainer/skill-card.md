## Description:

A Chinese-language junior-high math tutoring skill that helps students rebuild conceptual understanding through everyday analogies, visual reasoning, step-by-step decomposition, and brief comprehension checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and learning-support agents use this skill when a junior-high math learner is stuck on the meaning of a concept rather than on a specific problem. It guides the agent to explain with analogies, diagrams in words, and staged checks so the student can restate, transfer, and apply the concept.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Learning-profile records and cross-skill sharing may expose student learning data if consent and sharing controls are not set correctly.

Mitigation: Confirm profile sharing, reminder, parent-sharing, export, pause, and deletion controls before using the skill with a student.

Risk: The included crisis-resource text is tailored to Mainland China and may be unsuitable for students in other regions.

Mitigation: Replace or supplement emergency and youth-support contacts with local resources before deploying outside Mainland China.

Risk: AI-generated practice or transfer-check questions may be inaccurate or outside the intended grade band.

Mitigation: Use the included self-check protocol before presenting generated items and require teacher review before teacher-facing storage or reuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-concept-explainer)
- [Initial junior-high math analogy bank](artifact/references/analogy-bank.md)
- [AI-generated item self-check protocol](artifact/shared/ai-item-check.md)
- [Crisis exception protocol](artifact/shared/crisis-exception.md)
- [Platform capability conventions](artifact/shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Chinese-language conversational Markdown or plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teaching turns are intended to be concise and may include follow-up questions, comprehension checks, profile-control text, or cross-skill handoff guidance.]

## Skill Version(s):

2.1.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
