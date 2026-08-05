## Description: <br>
eKYC Suite AI Guardian reviews consented face photos or short videos for KYC liveness, replay, forged-media, AI-generated face, and deepfake risk signals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External KYC, fraud review, and identity operations teams use this skill to request photo or video liveness and synthetic-media review signals for consent-based remote onboarding workflows. Results should support retry, routing, or human review decisions rather than serve as final identity proof. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles biometric face media and sends the selected file to a configured cloud backend. <br>
Mitigation: Use it only with authorization for biometric processing, a defined retention policy, and access controls for submitted photos or videos. <br>
Risk: Misconfigured endpoints or unmanaged API keys could expose submitted media or results. <br>
Mitigation: Configure only a trusted HTTPS eKYC backend endpoint and use an API key management process. <br>
Risk: Liveness, replay, and deepfake outputs can be mistaken for final identity decisions. <br>
Mitigation: Treat outputs as review signals requiring human oversight, not as identity proof or an automated final decision. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-ai-guardian) <br>
- [Related npm MCP Package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-ai-guardian-mcp) <br>
- [Parent eKYC Suite Skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite) <br>
- [eKYC Suite Face Compare](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-face-compare) <br>
- [eKYC Suite Document OCR](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-document-ocr) <br>
- [eKYC Suite Media Labeling](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-media-labeling) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [JSON results with concise Markdown guidance and CLI command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires EKYC_CLOUD_ENDPOINT and EKYC_CLOUD_API_KEY; processes only the explicitly supplied face photo or video.] <br>

## Skill Version(s): <br>
1.0.15 (source: frontmatter, changelog, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
