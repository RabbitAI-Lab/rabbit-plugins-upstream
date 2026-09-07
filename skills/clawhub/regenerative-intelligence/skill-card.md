## Description:

Regenerative Intelligence is a documentation-only specification for designing, reviewing, and operating agentic AI memory and recall systems that prioritize harm reduction, non-identifiability, consent-scoped recall, honesty, and energy restraint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[otherpowers](https://clawhub.ai/user/otherpowers)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, architects, reviewers, and auditors use this skill to specify or assess memory, recall, and pattern-stewardship systems for agentic AI. It helps them evaluate conformance to requirements for non-identifiability, consent-scoped recall, transparent refusal, no behavioral surveillance, and energy restraint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An implementation could treat this specification as proof that sensitive memory, deletion, identity separation, or refusal behavior is safe without reviewing the actual system.

Mitigation: Review the implementation against the conformance checklist, threat model, and security guidance before claiming conformance.

Risk: Readers could mistake the documentation for a runtime that stores data, builds a vault, monitors behavior, or enforces protections by itself.

Mitigation: Treat the artifact as governance and design guidance only; require separate implementation evidence for any runtime capability.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/otherpowers/skills/regenerative-intelligence)
- [Regenerative Intelligence specification](artifact/SKILL.md)
- [Conformance Checklist](artifact/conformance-checklist.md)
- [Threat Model](artifact/threat-model.md)
- [Metadata Schema](artifact/metadata-schema.md)
- [Energy Accounting](artifact/energy-accounting.md)
- [Resonance Handshake](artifact/resonance-handshake.md)
- [CARE Principles for Indigenous Data Governance](https://en.wikipedia.org/wiki/CARE_Principles_for_Indigenous_Data_Governance)
- [Elinor Ostrom](https://en.wikipedia.org/wiki/Elinor_Ostrom)
- [Edouard Glissant](https://en.wikipedia.org/wiki/Edouard_Glissant)
- [Differential privacy](https://en.wikipedia.org/wiki/Differential_privacy)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown prose, requirements, schemas, checklists, and review guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only; produces no executable code, hidden actions, data storage, or runtime monitoring.]

## Skill Version(s):

1.0.1 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
