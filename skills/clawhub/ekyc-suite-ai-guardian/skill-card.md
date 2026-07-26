## Description: <br>
eKYC Suite AI Guardian helps an agent check consented face photos or short face videos for face liveness, replay, forged-media, AI-generated-image, and deepfake risk in remote KYC onboarding. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and identity operations teams use this skill to add photo and video liveness, replay-risk, and deepfake-risk checks to consent-based, human-reviewed KYC workflows. Results should be treated as review signals, not identity proof or an automated final decision. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Face photos and videos are sensitive biometric media. <br>
Mitigation: Use the skill only with authorization to process the media, a clear retention policy, and appropriate access controls. <br>
Risk: The skill sends media to an operator-configured eKYC cloud endpoint. <br>
Mitigation: Configure only a trusted HTTPS endpoint and protect EKYC_CLOUD_API_KEY as a credential. <br>
Risk: Liveness and deepfake results can be misused as final identity proof. <br>
Mitigation: Treat results as risk-review signals and route ambiguous or high-risk cases to an authorized human reviewer. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-ai-guardian) <br>
- [Related npm MCP package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-ai-guardian-mcp) <br>
- [Parent eKYC Suite skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite) <br>
- [eKYC Suite Face Compare](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-face-compare) <br>
- [eKYC Suite Document OCR](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-document-ocr) <br>
- [eKYC Suite Media Labeling](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-media-labeling) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON responses from CLI commands, with Markdown usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires EKYC_CLOUD_ENDPOINT and EKYC_CLOUD_API_KEY; reads only the explicitly supplied face photo or video and sends it to the configured HTTPS endpoint.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release, frontmatter, GEO.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
