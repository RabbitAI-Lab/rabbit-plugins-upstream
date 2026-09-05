## Description:

A Chinese middle-school physics problem-solving coach that guides students through one current physics problem using a four-step flow: read and draw the physical scene, build the model, calculate, then check and reflect.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and learning assistants use this skill to work through a specific middle-school physics problem in Chinese, especially mechanics, circuits, optics, heat, pressure, buoyancy, and power questions. The skill emphasizes drawing the physical scene before formulas, escalating hints only as needed, and requiring explicit consent before profile use, wrong-answer handoff, or reminders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The packaged schemas give broader student-profile and handoff authority than the tutoring instructions require.

Mitigation: Use only where the host enforces field-level profile projection and fail-closed consent checks; do not expose interest, safety, non-physics subject records, or unrelated consent fields to this skill.

Risk: Wrong-answer or reminder handoffs could be created without the required learner or guardian consent.

Mitigation: Reject wrong-answer and reminder handoffs unless cross-skill sharing, current-item consent, and any required guardian consent are verified.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-problem-coach)
- [Physics four-step state machine](artifact/references/physics-4step-statemachine.md)
- [Physics Socratic questioning guide](artifact/references/physics-socrates-guide.md)
- [Physics diagram guide](artifact/references/physics-diagram-guide.md)
- [Physics CLAW templates](artifact/references/claw-templates-physics.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown conversational tutoring responses with optional structured handoff guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language middle-school physics coaching; profile reads, wrong-answer handoffs, and reminders are consent-gated.]

## Skill Version(s):

2.1.6 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
