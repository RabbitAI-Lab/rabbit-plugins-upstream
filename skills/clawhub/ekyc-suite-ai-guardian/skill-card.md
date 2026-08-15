## Description:

eKYC Suite AI Guardian checks consented face photos and short videos for KYC face liveness, replay, forged-media, AI-generated face, and deepfake risk signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits)

### License/Terms of Use:

MIT-0

## Use Case:

External identity, fraud-review, and KYC operations teams use this skill to send authorized face media to a configured eKYC Suite Cloud endpoint for liveness and synthetic-media risk review. Results should be used as human-reviewed risk signals, not identity proof or an automatic decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face photos and videos are sensitive biometric media sent to a configured cloud endpoint.

Mitigation: Install only with a trusted HTTPS eKYC Cloud endpoint, valid API key, authorization for biometric processing, and clear retention and access policies.

Risk: Liveness, replay, and deepfake results can be mistaken for identity proof or automatic decision authority.

Mitigation: Use returned results only as review signals and route ambiguous or high-risk cases to an authorized human reviewer.

Risk: Low-quality, compressed, cropped, glared, or poorly lit media may reduce reliability.

Mitigation: Request a retry when media quality makes the input unreliable before escalating or acting on the result.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-ai-guardian)
- [Related npm MCP Package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-ai-guardian-mcp)
- [Parent eKYC Suite Skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite)
- [eKYC Suite Face Compare](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-face-compare)
- [eKYC Suite Document OCR](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-document-ocr)
- [eKYC Suite Media Labeling](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-media-labeling)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Guidance]

**Output Format:** [JSON printed to stdout with success, error, risk, tag, and trace fields returned by the configured backend]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts a user-supplied face photo or short face video path; files over 20MB are rejected by the local client.]

## Skill Version(s):

1.0.16 (source: frontmatter, changelog, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
