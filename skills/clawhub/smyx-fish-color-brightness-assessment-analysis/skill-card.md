## Description:

Analyzes ornamental fish photos or videos to assess body color and brightness, returning a vibrancy score and structured assessment report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers and ornamental fish farm operators can use the skill to review fish coloration from images or video and track assessment results. The report offers husbandry guidance and color signals, not a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected fish footage is sent to a remote service, and charges, retention, and deletion practices are not independently verified.

Mitigation: Review the service terms and account controls before uploading; use only footage appropriate to share with that service.

Risk: Account setup may expose persistent service credentials.

Mitigation: Review credential handling before installation, and rotate API_SECRET_KEY if it was configured during registration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-color-brightness-assessment-analysis)
- [API interface reference](references/api_doc.md)
- [Usage overview](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance]

**Output Format:** [Structured assessment report with color measurements, vibrancy score, trends, and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include HSV measurements, a 0–100 vibrancy score, trend information, husbandry suggestions, and a report link. Results depend on image quality and reference color calibration.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
