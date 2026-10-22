## Description:

Screens facial images or video alongside optional physiological indicators for stroke-risk warnings, lifestyle suggestions, and guidance on seeking medical care.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

People seeking a preliminary stroke-risk screening can submit a facial image or video and optional health indicators to receive a risk report and care guidance, or request their previous reports. The result is not a medical diagnosis or a substitute for professional assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Facial media and physiological information may be transmitted to external services and linked to a persistent identity without clear user control.

Mitigation: Inform users and obtain consent before submitting sensitive data; restrict use to a single-user or tightly controlled workspace.

Risk: Shared agent workspaces may expose one person's cloud report history to another.

Mitigation: Do not use the history feature in shared workspaces unless the publisher fixes identity isolation.

Risk: Screening warnings could be mistaken for a medical diagnosis.

Mitigation: Present results as preliminary screening only and encourage prompt professional evaluation for high-risk findings.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-stroke-risk-screening-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Text or JSON risk report; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and lifestyle or medical follow-up suggestions]

## Skill Version(s):

1.0.16 (source: ClawHub release metadata; bundled SKILL.md lists 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
