## Description:

Analyzes resting older adults' bedroom video for breathing rate and flags possible rapid breathing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and elder-care providers use resting video to review respiratory-rate estimates, alerts, and historical reports. This is monitoring support, not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive bedroom health video or video URLs may be sent to external lifeemergence services.

Mitigation: Obtain explicit consent from the monitored person or guardian and review service retention controls before use.

Risk: Reports may be linked to a silently managed persistent identity, with authentication tokens stored in a local workspace database.

Mitigation: Review account controls and protect local token storage; limit access to reports and credentials.

Risk: Visual respiratory estimates and alerts may be mistaken for a clinical diagnosis.

Mitigation: Use results only as monitoring support and arrange human or clinical follow-up when warranted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-elderly-tachypnea-detection-analysis)
- [Skill API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured breathing analysis or Markdown historical-report table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include respiratory-rate estimates, alerts, and report links.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
