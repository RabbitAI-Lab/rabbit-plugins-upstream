## Description:

eKYC Suite AI Guardian helps agents run consented KYC face-liveness, replay-risk, and deepfake screening checks on face photos or short videos through a configured eKYC Suite Cloud backend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits)

### License/Terms of Use:

MIT-0

## Use Case:

External identity, fraud, and KYC operations teams use this skill to screen user-authorized face photos and short face videos for liveness, replay, forged-media, AI-generated-image, and deepfake risk during remote onboarding. Results are review signals and should not be treated as identity proof or final high-impact decisions without human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends selected biometric media to the configured cloud backend.

Mitigation: Use it only with authorization to process the media, configure only a trusted HTTPS eKYC backend, and verify the backend's retention and access policies before deployment.

Risk: Liveness and deepfake results could be misused as identity proof or as a final high-impact decision.

Mitigation: Treat returned risk levels and tags as review signals, route ambiguous or high-risk results to an authorized human reviewer, and keep face comparison or document OCR in separate workflows.

Risk: Poor lighting, glare, cropping, face coverage, or compression can make media-risk results unreliable.

Mitigation: Request a retry when input quality is poor and avoid describing the tool as guaranteeing that a person is genuine.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-ai-guardian)
- [Related npm MCP package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-ai-guardian-mcp)
- [Parent eKYC Suite skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite)
- [eKYC Suite Face Compare skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-face-compare)

## Skill Output:

**Output Type(s):** [JSON, Guidance, Shell commands]

**Output Format:** [JSON results with Markdown command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns cloud liveness and media-risk signals for user-supplied photo or video inputs; ambiguous or high-risk results require human review.]

## Skill Version(s):

1.0.18 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
