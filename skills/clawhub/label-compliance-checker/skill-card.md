## Description:

Checks medical device label and instructions fields against stated official rule sources and emits deterministic JSON decision-support output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, compliance teams, and medical device operators use this CLI as a convenience checklist for label and instructions completeness. Its outputs support human review and must not be treated as legal, regulatory, clinical, registration, or recall conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Checklist output could be mistaken for an authoritative medical-device compliance conclusion.

Mitigation: Treat outputs as decision support only, require human review, and verify conclusions against current official NMPA rules before registration, clinical, recall, or other regulated decisions.

Risk: Documentation examples or embedded rule references may become stale as regulations change.

Mitigation: Review the current official text before relying on any field-level determination, especially before production or regulated use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/label-compliance-checker)
- [LGD theory ledger](https://medxpert.cn/theory)

## Skill Output:

**Output Type(s):** [JSON, Guidance, Shell commands]

**Output Format:** [JSON IR from a Python CLI, with warnings and return codes for decision-support review]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes rc status codes, missing-field lists, obligations, notes, warnings, and GB45438-2025 AIGC metadata.]

## Skill Version(s):

1.0.0 (source: server release metadata, skill frontmatter, and script metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
