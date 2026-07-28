## Description: <br>
eKYC Suite Media Labeling returns selected portrait, behavior, and scene labels from consented KYC images or videos for onboarding media review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External KYC onboarding, fraud review, identity operations, and human-review teams use this skill to request supported media labels from consented images or videos and route those labels into review or risk triage. It should not be used for final high-impact decisions, unrestricted image captioning, or unsupported classifications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive KYC onboarding media is uploaded to an operator-configured cloud endpoint. <br>
Mitigation: Install only for consented KYC media-review workflows, use a trusted HTTPS endpoint, and verify backend retention and access policies before deployment. <br>
Risk: Optional liveness and comparison checks may run when they are not intended for a workflow. <br>
Mitigation: Set liveness and comparison options off unless those biometric checks are explicitly authorized and required. <br>
Risk: Structured labels can be misleading when media is cropped, dark, ambiguous, or outside the supported label taxonomy. <br>
Mitigation: Treat labels as review signals, request clearer uploads when needed, and escalate sensitive or ambiguous results to an authorized human reviewer. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-media-labeling) <br>
- [Related npm MCP Package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-media-labeling-mcp) <br>
- [Parent eKYC Suite Skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite) <br>
- [eKYC Suite Face Compare](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-face-compare) <br>
- [eKYC Suite AI Guardian](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-ai-guardian) <br>
- [eKYC Suite Document OCR](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-document-ocr) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Configuration] <br>
**Output Format:** [JSON returned by a command-line cloud client] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires EKYC_CLOUD_ENDPOINT and EKYC_CLOUD_API_KEY; accepts one image or video plus 1-5 supported label codes.] <br>

## Skill Version(s): <br>
1.0.12 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
