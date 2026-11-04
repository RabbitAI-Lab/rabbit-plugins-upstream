## Description:

Analyzes emergency shelter video for visible behaviors associated with acute stress and produces alerts for psychological support teams to review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Emergency response coordinators and licensed psychological support teams use the skill to review shelter footage for visible behavior patterns and prioritize in-person checks. Alerts are observations for human review, not clinical diagnoses.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill can upload sensitive footage despite an export-only request, and may silently create accounts and retain credentials.

Mitigation: Use synthetic footage until export-only and destination controls, credential routing, and automatic account provisioning are corrected. Before using identifiable shelter footage, approve the external processor and verify retention, face blurring, access controls, and human review arrangements.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release](https://clawhub.ai/18072937735/skills/smyx-trauma-stress-behavior-detection-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance]

**Output Format:** [Structured behavior observations and alert results, typically JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include alert level, shelter zone, responder suggestions, and report links; alerts require human review.]

## Skill Version(s):

1.0.16 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
