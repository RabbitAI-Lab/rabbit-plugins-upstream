## Description:

A Chinese writing coach for upper-elementary and middle-school learners that uses questioning, rubric-based feedback, debate practice, and consent-gated writing-style memory to help students develop their own essays without ghostwriting for them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese K-12 learners and learning platforms use this skill to brainstorm, check logic, receive targeted composition feedback, and practice argumentation while keeping the student's own wording and ideas central.

### Deployment Geography for Use:

Mainland China by default; deployments elsewhere require localized crisis-support guidance and minor-consent rules before student-facing use.

## Known Risks and Mitigations:

Risk: Consent controls for remembering student writing patterns may not be enforced by every host platform.

Mitigation: Deploy only where the platform enforces explicit consent plus view, correct, delete, pause, export, and sharing controls before profile data is read or written.

Risk: Grammar-profile data permissions may exceed the intended boundary for a writing coach.

Mitigation: Route grammar-error profile updates through the designated grammar-tracking flow or a platform-confirmed handoff, rather than allowing direct grammar-profile writes by this skill.

Risk: Crisis-support channels and minor-consent assumptions are tailored to mainland China.

Mitigation: Localize crisis resources and legal consent rules before using the skill outside mainland China, and ask the learner's region before giving crisis phone numbers.

Risk: Students may try to use the skill to obtain a finished essay instead of learning to write.

Mitigation: Preserve the no-ghostwriting workflow: require student attempts, use progressive hints, and restrict examples to unrelated topics or partial scaffolds.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-writing-coach)
- [Writing 5-step state machine](artifact/references/writing-5step-statemachine.md)
- [Writing rubric](artifact/references/writing-rubric.md)
- [Debate script guide](artifact/references/debate-script-guide.md)
- [Platform conventions](artifact/shared/platform-conventions.md)
- [Crisis exception protocol](artifact/shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Conversational Chinese markdown with optional structured handoff data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not produce completed student essays; provides questions, feedback, revision directions, and consent-gated profile handoffs.]

## Skill Version(s):

2.1.12 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
