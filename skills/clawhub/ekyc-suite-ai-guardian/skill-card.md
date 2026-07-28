## Description: <br>
eKYC Suite AI Guardian checks consented face photos and short face videos for liveness, replay, forged-media, AI-generated face, and deepfake risk in remote KYC onboarding. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
KYC, fraud review, identity operations, and developer teams use this skill to route consented face photos or short videos through face-liveness, replay-risk, and deepfake-screening checks. Results should support human-reviewed onboarding workflows rather than final identity decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive biometric media and sends the supplied photo or video to a configured cloud backend. <br>
Mitigation: Use it only with user authorization, a defined retention and access policy, and an intended HTTPS EKYC_CLOUD_ENDPOINT. <br>
Risk: Liveness, replay, and deepfake outputs could be mistaken for final identity decisions. <br>
Mitigation: Treat the returned signals as inputs to human-reviewed risk routing, retry, or escalation workflows. <br>
Risk: An incorrect endpoint or credential configuration could send media to the wrong service. <br>
Mitigation: Verify EKYC_CLOUD_ENDPOINT and EKYC_CLOUD_API_KEY before installation or execution. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-ai-guardian) <br>
- [Related npm MCP package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-ai-guardian-mcp) <br>
- [Parent eKYC Suite skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite) <br>
- [eKYC Suite Face Compare](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-face-compare) <br>
- [eKYC Suite Document OCR](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-document-ocr) <br>
- [eKYC Suite Media Labeling](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-media-labeling) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, JSON, Guidance] <br>
**Output Format:** [JSON response from a CLI command] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns liveness, replay, and synthetic-media risk signals from the configured cloud backend; outputs are review signals, not identity proof.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
