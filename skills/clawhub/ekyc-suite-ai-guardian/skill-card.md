## Description: <br>
eKYC Suite AI Guardian checks consented face photos and short face videos for liveness, replay, forged-media, AI-generated face, and deepfake risk signals in remote KYC workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External identity operations teams, fraud reviewers, and developers use this skill to request face-media liveness and synthetic-media risk checks during consent-based KYC onboarding. Results should be treated as review signals and routed to authorized human review for ambiguous or high-risk cases. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends selected biometric face media to a configured eKYC cloud backend. <br>
Mitigation: Install and run it only with authorization to process the media, and confirm endpoint ownership, API-key handling, retention policy, and access controls before use. <br>
Risk: Liveness, replay, and deepfake outputs can be misused as final identity proof. <br>
Mitigation: Treat results as risk-review signals, route ambiguous or high-risk cases to authorized human review, and do not use the skill for final high-impact decisions by itself. <br>
Risk: Poor lighting, glare, face coverage, cropping, compression, or oversized media can make checks unreliable. <br>
Mitigation: Request a retry when input quality is inadequate and enforce the documented short-video and 20 MB media boundary. <br>


## Reference(s): <br>
- [ClawHub Skill page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-ai-guardian) <br>
- [Related npm MCP package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-ai-guardian-mcp) <br>
- [Parent eKYC Suite skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite) <br>
- [eKYC Suite Face Compare skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-face-compare) <br>
- [eKYC Suite Document OCR skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-document-ocr) <br>
- [eKYC Suite Media Labeling skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-media-labeling) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Shell commands, Configuration, Guidance, JSON] <br>
**Output Format:** [JSON responses from CLI commands with concise operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires EKYC_CLOUD_ENDPOINT and EKYC_CLOUD_API_KEY; reads only the user-supplied media path and sends it to the configured HTTPS backend.] <br>

## Skill Version(s): <br>
1.0.14 (source: frontmatter, changelog, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
