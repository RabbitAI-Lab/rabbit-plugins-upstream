## Description:

化学错误DNA helps Simplified Chinese K12 learners analyze chemistry mistake patterns across symbol, microscopic, macroscopic, reading, experiment, and calculation dimensions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners, guardians, teachers, and education agents use this skill to classify chemistry wrong-answer root causes, maintain consent-controlled chemistry weakness summaries, and plan follow-up practice for China-mainland K12 chemistry contexts.

### Deployment Geography for Use:

China mainland by default; localize curriculum assumptions, crisis resources, and minor-consent rules before use elsewhere.

## Known Risks and Mitigations:

Risk: Use outside the intended China-mainland Simplified Chinese K12 context may present unsuitable curriculum, crisis-resource, or minor-consent assumptions.

Mitigation: Localize curriculum mapping, emergency resources, and minor-consent policy before deployment in other regions or languages.

Risk: The skill can write chemistry learning summaries and enqueue reminders when the user has authorized those actions.

Mitigation: Review profile, sharing, parent-visible summary, and reminder consent settings before deployment; preserve the skill's pause, delete, export, and sharing-control affordances.

Risk: Chemistry experiment guidance can create safety risk if converted into unsupervised home procedures.

Mitigation: Apply the bundled lab-safety guidance: avoid dangerous home experiment steps, require teacher-supervised lab contexts for hazardous work, and direct active accidents to local emergency help.

Risk: Learning anxiety or crisis signals could be mishandled as ordinary study frustration.

Mitigation: Use the bundled crisis exception and referral protocols before tutoring, reports, data display, or parent summaries when self-harm, severe despair, abuse, bullying, or immediate safety concerns appear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-chemistry-error-dna)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Chemistry error dimension table](references/chemistry-error-dimension-table.md)
- [DNA profile schema](shared/dna-profile.schema.json)
- [Handover protocol schema](shared/handover-protocol.schema.json)
- [Lab safety guidance](shared/lab-safety.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Conversational text and markdown summaries, with structured handover/profile fields when authorized]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce chemistry weakness summaries, root-cause labels, practice guidance, consent-gated profile writebacks, and reminder enqueue requests.]

## Skill Version(s):

2.3.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
