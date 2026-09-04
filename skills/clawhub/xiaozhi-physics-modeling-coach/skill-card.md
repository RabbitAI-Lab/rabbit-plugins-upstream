## Description:

Chinese-language junior-high physics modeling coach that helps students identify physical phenomena, choose an applicable model, and express the model mathematically before solving.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and educators use this skill for Chinese-language junior-high physics tutoring when a learner needs to decide which physical law or model applies before calculation. It focuses on model-selection practice, model transfer, and guided mathematical expression rather than full worked solutions, experiment design, or mistake-log management.

### Deployment Geography for Use:

Global, with Chinese-language and Mainland China educational and crisis-resource assumptions requiring localization before broader deployment.

## Known Risks and Mitigations:

Risk: The skill targets minors and may use learning-profile memory or cross-skill sharing.

Mitigation: Honor the documented consent controls for viewing, correcting, deleting, pausing, exporting, and limiting sharing of profile data; require appropriate guardian involvement where the deployment policy requires it.

Risk: The bundled safety guidance is localized for Chinese/Mainland-China usage.

Mitigation: Document the locale clearly and localize emergency and crisis-referral resources before deploying for users outside that region.

Risk: AI-generated practice items or model-transfer exercises could contain incorrect, ambiguous, or out-of-scope physics content.

Mitigation: Apply the included item self-check for solvability, uniqueness, sufficient conditions, grade-band fit, and reasonable physical quantities before presenting generated items.

Risk: OCR or image understanding may be unavailable or unreliable for physics diagrams and problem statements.

Mitigation: Use the documented fallback path: ask the learner to type the known conditions and question in text before selecting a model.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-modeling-coach)
- [Physics modeling patterns reference](references/physics-modeling-patterns.md)
- [Learning DNA profile schema](https://xiaozhi-skills.openclaw.dev/schemas/dna-profile.schema.json)
- [Handover protocol schema](https://xiaozhi-skills.openclaw.dev/schemas/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Conversational tutoring guidance with equations, model-selection prompts, generated practice items, and consent-gated profile or handover notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use platform memory and OCR capabilities when available; otherwise it degrades to current-session text input.]

## Skill Version(s):

2.1.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
