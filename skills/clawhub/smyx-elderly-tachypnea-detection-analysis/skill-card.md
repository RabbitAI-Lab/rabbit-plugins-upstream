## Description:

This skill analyzes infrared or low-light bedroom video of an older adult at rest to estimate respiratory rate and flag elevated tachypnea risk without providing a medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, family members, and elder-care platform operators can use this skill to analyze resting chest or abdominal video and receive structured respiratory-rate findings, risk labels, alerts, and report links. It is intended as auxiliary monitoring for home elderly care, nursing homes, and rehabilitation wards, not as clinical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive bedroom video and respiratory report data may be processed through external cloud APIs.

Mitigation: Use only with informed consent from the monitored person or guardian, avoid unrelated private footage, and confirm how uploaded media and reports are protected.

Risk: Historical reports may be linked to a locally persisted identity or token.

Mitigation: Review token storage, report-link access controls, and deletion procedures before deployment.

Risk: Respiratory-rate alerts can be mistaken for medical diagnosis.

Mitigation: Present outputs as auxiliary visual monitoring, require human follow-up for urgent alerts, and direct users to appropriate medical care when needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-elderly-tachypnea-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown and structured JSON text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include respiratory-rate fields, signal quality, risk level, alert text, medical follow-up hints, and exported report links.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter says 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
