## Description:

Analyzes home-camera footage for prolonged bed rest and reduced eating, then provides behavioral-change reports and alerts for caregivers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Families, community care teams, and developers use the skill to review changes in bed-rest and eating patterns from home-camera footage and receive caregiver-facing reports. Its observations are not a depression diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive in-home footage and identity-linked requests are sent to the publisher's cloud services.

Mitigation: Obtain the monitored person's informed consent and confirm where footage, identifiers, and credentials are transmitted and stored before use.

Risk: Cloud report history may expose private behavioral-health information if access controls or retention are unclear.

Mitigation: Avoid the history feature until access control and retention details are confirmed; limit report access to authorized caregivers.

Risk: Behavioral signals may be mistaken for a medical diagnosis.

Mitigation: Treat reports as observations only and involve a qualified clinician for assessment or care decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-depression-behavioral-markers-analysis)
- [API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured behavioral-change report or history listing, with optional report link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include bed-rest and eating metrics, alerts, suggested follow-up, and a saved report file.]

## Skill Version(s):

1.0.15 (source: server-resolved ClawHub release; bundled frontmatter says 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
