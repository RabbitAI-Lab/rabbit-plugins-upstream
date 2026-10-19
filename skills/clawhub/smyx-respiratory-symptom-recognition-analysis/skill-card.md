## Description:

Analyzes respiratory videos to count coughing, sputum, and wheezing episodes and provide health-monitoring reports and alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals, caregivers, and healthcare teams use video-based symptom monitoring to review episode counts, potential health alerts, and historical reports. Results support observation rather than medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive respiratory videos and report history are sent to the publisher's cloud service and linked to a silently managed persistent identity.

Mitigation: Obtain consent before use and review the publisher's privacy, retention, deletion, and account-token practices before uploading health footage.

Risk: Automated symptom alerts and severity assessments may be mistaken for a medical diagnosis.

Mitigation: Use reports only as a monitoring aid; seek professional assessment for concerning symptoms and urgent care for severe breathing difficulty.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-respiratory-symptom-recognition-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured report or JSON; historical reports as a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include symptom counts, risk alerts, care suggestions, report links, and an optional saved result file.]

## Skill Version(s):

1.0.19 (source: ClawHub release metadata; bundled SKILL.md lists 1.0.22)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
