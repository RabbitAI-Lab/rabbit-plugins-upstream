## Description: <br>
eKYC Suite Face Compare is a focused KYC face-comparison skill for AI agents that compares two consented face images and returns a structured similarity score. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agent developers, fintech onboarding teams, compliance engineers, and identity-verification builders use this skill to compare two consented face images for selfie verification, selfie-to-document checks, and human-reviewed KYC onboarding. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Face images are sensitive biometric data and are sent to a configured HTTPS eKYC backend. <br>
Mitigation: Use the skill only with user authorization, a trusted EKYC_CLOUD_ENDPOINT, and clear backend retention, access, and compliance controls. <br>
Risk: A similarity score can be misused as the sole basis for a high-impact identity decision. <br>
Mitigation: Treat the score as one verification signal and apply deployment-specific thresholds, retry rules, and human review. <br>
Risk: Endpoint or credential misconfiguration could route submitted media to an unintended backend. <br>
Mitigation: Configure only a trusted HTTPS endpoint, keep EKYC_CLOUD_API_KEY protected, and verify deployment settings before processing images. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-face-compare) <br>
- [Related npm MCP Package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-face-compare-mcp) <br>
- [Parent eKYC Suite Skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite) <br>
- [eKYC Suite AI Guardian](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-ai-guardian) <br>
- [eKYC Suite Document OCR](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-document-ocr) <br>
- [eKYC Suite Media Labeling](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-media-labeling) <br>


## Skill Output: <br>
**Output Type(s):** [json, shell commands, guidance] <br>
**Output Format:** [JSON response plus Markdown command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns a structured 0-100 similarity score and cloud response metadata from the configured eKYC backend.] <br>

## Skill Version(s): <br>
1.0.15 (source: frontmatter, changelog, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
