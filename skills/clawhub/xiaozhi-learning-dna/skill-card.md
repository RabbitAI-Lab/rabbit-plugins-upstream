## Description:

学习DNA helps an agent create, view, correct, export, delete, and selectively share long-term student learning profiles only after explicit authorization, with separate controls for emotions, interests, parent-visible output, teacher writeback, cross-skill sharing, and crisis referral facts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Student-facing tutoring agents and related education workflows use this skill as a consent-controlled long-term learning profile layer. It supports personalization through profile records, growth milestones, profile export or deletion, and limited cross-skill handoff while avoiding default reads during ordinary tutoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive student learning records may be read, written, or shared without sufficient authorization if runtime identity and consent checks are weak.

Mitigation: Deploy only where the platform enforces student identity, guardian consent when required, current-consent checks, deletion and export controls, and field-level read/write allowlists.

Risk: Cross-skill handoff and teacher writeback can expose or modify minor data beyond the intended task.

Mitigation: Treat schemas as structure only, require explicit runtime authorization for each handoff, and restrict writes for emotion, teacher, interest, and crisis-related records to the documented allowed fields.

Risk: Crisis-support contact guidance may be inappropriate outside the configured region.

Mitigation: Confirm the user's country or region before giving crisis contacts, localize emergency resources, and avoid presenting China mainland numbers as universal.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-dna)
- [SKILL.md](artifact/SKILL.md)
- [Learning DNA profile schema](artifact/schemas/dna-profile.schema.json)
- [Schema README](artifact/schemas/README.md)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)
- [Crisis exception guidance](artifact/shared/crisis-exception.md)
- [Crisis referral protocol](artifact/references/crisis-referral-protocol.md)
- [Learning DNA template](artifact/references/dna-template.md)
- [Growth milestones](artifact/references/growth-milestones.md)
- [Cross-subject connections](artifact/references/cross-subject-connections.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Natural-language guidance, Markdown profile summaries, and structured JSON profile or handover records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are consent-gated and should use only the minimum profile fields needed for the current tutoring task.]

## Skill Version(s):

2.1.10 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
