## Description:

Screens consented face photos and short videos for liveness, replay, and synthetic-media risk during KYC onboarding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits)

### License/Terms of Use:

MIT-0

## Use Case:

Identity and fraud-review teams use this skill to screen authorized face media during remote KYC onboarding and route uncertain or high-risk results to human reviewers. It does not perform identity matching or make final identity decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Biometric face media is uploaded to the configured cloud endpoint.

Mitigation: Use only an endpoint you operate or trust, obtain authorization for biometric processing, and establish a retention policy before submitting media.

Risk: Liveness and deepfake screening signals may be uncertain or misleading.

Mitigation: Treat results as review signals, retry poor-quality inputs, and route ambiguous or high-risk cases to an authorized human reviewer rather than making final identity decisions.

## Reference(s):

- [eKYC Suite AI Guardian on ClawHub](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-ai-guardian)
- [Related eKYC Suite AI Guardian MCP package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-ai-guardian-mcp)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [JSON liveness and media-risk results with review guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Photo or video checks return risk signals for human review, not identity proof.]

## Skill Version(s):

1.0.20 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
