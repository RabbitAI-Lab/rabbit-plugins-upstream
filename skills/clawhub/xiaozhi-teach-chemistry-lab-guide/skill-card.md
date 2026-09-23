## Description:

Helps Chinese-language chemistry teachers plan lab teaching, including demonstration-versus-group decisions, grouping and equipment arrangements, classroom safety organization, lab reports, and practical exam preparation for required middle-school experiments and selected high-school required experiments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language chemistry teachers use this skill to draft classroom lab organization plans, classify experiment safety levels, plan groups and equipment, scaffold lab reports, and prepare practical exam routines. It is designed for the Mainland China K12 curriculum context and teacher-reviewed classroom use.

### Deployment Geography for Use:

Mainland China by default; localize crisis contacts, curriculum references, lab-safety rules, and data-consent defaults before use in other regions or languages.

## Known Risks and Mitigations:

Risk: Lab guidance could be misapplied outside local school safety rules or with unsafe experiment classifications.

Mitigation: Require teacher review before classroom use, defer to school laboratory rules, classify each experiment with safetyLevel, and keep high-risk experiments as teacher demonstrations only.

Risk: Use outside the Mainland China K12 context could provide mismatched crisis contacts, curriculum assumptions, safety rules, or consent defaults.

Mitigation: Localize emergency contacts, curriculum references, laboratory safety requirements, and minor-data consent settings before regional or language deployment.

Risk: Class workspace data may include student learning records for minors.

Mitigation: Use the declared class-teaching workspace schema, keep student identifiers limited to aliases or seat numbers, and honor view, correction, deletion, pause, sharing-control, and export controls.

Risk: Drafts could be mistaken for authoritative medical, emergency, or grading decisions.

Mitigation: Keep outputs as teacher-reviewed drafts, avoid medical treatment advice, route emergencies to local adult and emergency channels, and do not let the skill grade or evaluate students autonomously.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-chemistry-lab-guide)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Chemistry lab teaching reference](artifact/references/chemistry-lab-teaching.md)
- [Lab safety agreement](artifact/shared/lab-safety.md)
- [Class teaching workspace schema](artifact/shared/class-teaching-workspace.schema.json)
- [Platform conventions and localization guidance](artifact/shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with structured classroom-planning fields and pending workspace update entries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are teacher-reviewed drafts for lab organization, safety checks, grouping plans, question chains, lab-report tasks, and practical exam routines.]

## Skill Version(s):

2.2.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
