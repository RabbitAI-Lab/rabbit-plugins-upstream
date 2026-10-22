## Description:

Analyzes ornamental fish images or videos to report color brightness, saturation, vibrancy scores, trends, and husbandry-oriented suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers and fish-farm operators use camera images or video to monitor ornamental fish coloration over time and review cloud-hosted assessment reports. Results support husbandry decisions, not disease diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fish images and videos are sent to the LifeEmergence remote service for analysis.

Mitigation: Obtain permission before uploading media and avoid submitting images or footage you are not comfortable sharing with the service.

Risk: The skill silently creates or reuses an account and stores access tokens locally; report history is linked to that identity.

Mitigation: Disclose account-linked history to users and review or delete the local data database and tokens when persistent identity reuse is unwanted.

Risk: Lighting, camera angle, or missing white reference can make color scores unreliable.

Mitigation: Use a side-view image with a white reference and treat unreliable scores as a request to retake the image, not as a diagnosis.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-color-brightness-assessment-analysis)
- [Fish color assessment API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured assessment report or Markdown history table; optional JSON or saved report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include vibrancy scores, color measurements, trends, husbandry suggestions, and links to remote reports.]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
