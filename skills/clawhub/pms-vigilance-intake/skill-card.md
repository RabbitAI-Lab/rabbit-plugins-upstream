## Description:

pms-vigilance-intake is a zero-dependency CLI decision-support tool that classifies medical-device adverse event reporting pathways from severity and event type and returns structured JSON IR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

External users and compliance teams use this skill to triage Chinese medical-device adverse event reporting paths, deadlines, recall or re-evaluation flags, and required human review steps. It supports decision preparation only and does not replace regulator determinations or legal advice.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Users could mistake decision-support output for an authoritative regulatory or legal conclusion.

Mitigation: Treat outputs as advisory, verify against current official rules, and require human compliance review before filing, recall, registration, or clinical decisions.

Risk: Documented example commands mention device_class/device_type while the CLI accepts severity/event_type.

Mitigation: Use severity and optional event_type parameters until the documentation examples are corrected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/pms-vigilance-intake)
- [LGD Theory Ledger](https://medxpert.cn/theory)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code]

**Output Format:** [JSON IR from the CLI, with Markdown usage guidance in the skill documentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns rc=0 for completed decisions, rc=1 when warnings are present, and rc=2 for insufficient input; severity is required and event_type is optional.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
