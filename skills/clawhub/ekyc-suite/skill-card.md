## Description: <br>
eKYC Suite is a ClawHub KYC skill that lets AI agents run remote KYC onboarding, KYC identity verification, selfie verification, face liveness detection, KYC document OCR, deepfake screening, and media risk review from consented image or video uploads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, fintech onboarding teams, risk and compliance engineers, and KYC workflow developers use this skill to add consent-based identity checks to AI-agent workflows. It supports human-reviewed face comparison, liveness and deepfake screening, document OCR, and media risk labels for uploaded images or videos. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends biometric or identity media to the configured eKYC Suite Cloud endpoint for processing. <br>
Mitigation: Install only with a trusted EKYC_CLOUD_ENDPOINT, a valid API key, user consent, and a documented retention and access-control policy. <br>
Risk: KYC outputs may influence legal, financial, or other high-impact decisions. <br>
Mitigation: Treat outputs as review signals, not as the sole basis for automated decisions; require appropriate business controls and human review. <br>
Risk: Uploaded identity documents, bank-card images, and OCR results can contain sensitive personal data. <br>
Mitigation: Mask sensitive fields where possible and avoid submitting typed names, ID numbers, phone numbers, or other personal text through chat. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite) <br>
- [Related npm MCP package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-mcp) <br>
- [Related repository](https://github.com/wefi-ai/ekyc-suite-mcp) <br>
- [eKYC Suite Face Compare](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-face-compare) <br>
- [eKYC Suite AI Guardian](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-ai-guardian) <br>
- [eKYC Suite Document OCR](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-document-ocr) <br>
- [eKYC Suite Media Labeling](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-media-labeling) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured JSON tool results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Tool calls require EKYC_CLOUD_ENDPOINT and EKYC_CLOUD_API_KEY; local media inputs are limited to 20MB and HTTP URLs are rejected.] <br>

## Skill Version(s): <br>
1.1.23 (source: frontmatter, changelog, and server release evidence, released 2026-08-03) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
