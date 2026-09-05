## Description:

Analyzes fish aquarium or underwater camera images and videos for visible signs of white spot, hyperemia, and fin rot, then returns symptom classifications with confidence, location, severity, recommendations, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium owners, public aquariums, ornamental fish farms, and developers of aquarium monitoring workflows use this skill to inspect fish media for surface symptom indicators and retrieve historical body-surface health reports. The output is intended as visual screening guidance, not a veterinary diagnosis or medication plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fish media, media URLs, report requests, and identity fields may be sent to backend services.

Mitigation: Review the publisher and data handling before installation, and use the skill only with media and report data that users are authorized to submit.

Risk: The security evidence reports silent identity management and local token storage.

Mitigation: Confirm the identity and token handling behavior is acceptable for the deployment environment before normal use.

Risk: The security evidence reports private development HTTP endpoint configuration.

Mitigation: Fix or explain the endpoint configuration and prefer documented production HTTPS endpoints before installing for normal users.

Risk: Visual symptom analysis can be mistaken for veterinary diagnosis or treatment guidance.

Mitigation: Present results as visual screening only, avoid specific medication names or dosing instructions, and direct users to a qualified aquarium veterinarian or professional for diagnosis and treatment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fish-surface-symptom-detection-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [API documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown reports and JSON or structured text from command-line API calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes symptom labels, confidence scores, affected locations, severity, recommended non-medication actions, disclaimers, and report links when returned by backend services.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
