## Description:

Medical-device AI/ML change-control judgment per the LGD three laws (有籍 Recorded / 有证 Evidenced / 有门禁 Gated). Trigger when the user asks whether a device-software or algorithm change requires change control, asks for a risk verdict (pass/hold/reject), asks for change-level classification (minor/major/critical), or asks for an LGD-theory judgment with auditable reasons. Applies to regulated environments (FDA 510(k)/PMA, EU MDR, ISO 13485) and other AI/ML medical-device change evaluations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

Apache 2.0

## Use Case:

Medical-device software developers, quality teams, and regulatory reviewers use the skill to assess whether an AI/ML change needs change control and to produce a traceable pass, hold, or reject judgment with a change level and supporting reasons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The engine can approve incomplete cases.

Mitigation: Require qualified human review and validate missing-input and verdict-handling paths before relying on any go result.

Risk: Case details may be retained in local memory or audit storage.

Mitigation: Use only sanitized cases until full-input storage is disclosed and controlled.

Risk: Regulatory correctness and production suitability have not been validated.

Mitigation: Have qualified reviewers assess the judgment and its regulatory basis before operational use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/lgd-change-gate)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON]

**Output Format:** [Structured change-control judgment with verdict, change level, reasons, and citations; may be presented as text or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May identify missing or pending evidence.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
