## Description:

Analyzes driver-facing video for blink rate and eye-closure patterns, returning fatigue indicators, warnings, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Fleet safety teams and developers use driver-facing video to review blink and eye-closure indicators, receive fatigue warnings, and retrieve historical reports. Alerts are aids to driver judgment, not medical diagnoses or substitutes for safe driving.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Driver-facing footage or video URLs are sent to the LifeEmergence cloud service.

Mitigation: Obtain informed consent and clarify retention, deletion, and data-protection controls before uploading sensitive footage.

Risk: Report history is tied to an automatically managed identity, with authentication and profile data stored for reuse.

Mitigation: Ask the publisher how identities, tokens, and report history are stored and protected; avoid production fleet or employee footage until these controls are clear.

Risk: Fatigue alerts may be unreliable when eyes are obscured or lighting is poor.

Mitigation: Treat visual indicators as advisory only and retain human oversight of driving decisions.

## Reference(s):

- [Driver fatigue detection API documentation](references/api_doc.md)
- [LifeEmergence skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-driver-blink-fatigue-detection-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured JSON or Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include fatigue indicators, warnings, suggested actions, historical report listings, and report links.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
