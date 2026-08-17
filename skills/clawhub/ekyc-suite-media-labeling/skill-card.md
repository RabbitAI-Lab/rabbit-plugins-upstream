## Description:

eKYC Suite Media Labeling helps agents request selected portrait, behavior, and scene labels from consented KYC images or videos through a configured cloud labeling service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits)

### License/Terms of Use:

MIT-0

## Use Case:

KYC onboarding, fraud review, identity operations, and human-review teams use this skill when an agent needs narrow media-review labels for consented images or videos without open-ended captioning, face comparison, document OCR, or final automated decisioning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: KYC images and videos may contain sensitive personal data.

Mitigation: Process only user-authorized media under an appropriate retention policy and confirm the configured cloud service is approved for the data.

Risk: Media labels can be incomplete, ambiguous, or unsuitable for final identity decisions.

Mitigation: Treat labels as review signals and escalate sensitive or ambiguous results to an authorized human reviewer.

Risk: The client sends selected media to an operator-configured HTTPS endpoint.

Mitigation: Configure EKYC_CLOUD_ENDPOINT and EKYC_CLOUD_API_KEY intentionally, and verify downstream retention, access control, and processing terms before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-media-labeling)
- [Related npm MCP package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-media-labeling-mcp)

## Skill Output:

**Output Type(s):** [JSON, text, guidance]

**Output Format:** [JSON label results or JSON error objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts one image or video input and 1-5 requested label codes; outputs should be treated as review signals rather than definitive facts.]

## Skill Version(s):

1.0.19 (source: release evidence, SKILL.md frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
