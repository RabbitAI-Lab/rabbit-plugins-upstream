## Description: <br>
eKYC Suite is a ClawHub KYC identity verification skill for AI agents that supports consent-based media checks for remote onboarding, document OCR, face comparison, liveness detection, deepfake screening, and human-reviewed risk workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AI agent builders, fintech onboarding teams, compliance engineers, and KYC workflow developers use this skill to add identity-document OCR, selfie-to-document face comparison, liveness and deepfake screening, and media risk review to human-reviewed KYC workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends sensitive identity documents, bank-card images, face images, and videos to a configured cloud endpoint for KYC processing. <br>
Mitigation: Install only with a trusted eKYC backend, operator-confirmed user consent, a retention policy, access controls, and confirmation of where submitted media and OCR results are stored or processed. <br>
Risk: Verification outputs may influence high-impact identity, legal, financial, or onboarding decisions. <br>
Mitigation: Treat outputs as advisory review signals and require human review and appropriate business controls before making consequential decisions. <br>
Risk: Typed names, ID numbers, phone numbers, or other personal text in chat may create unnecessary privacy exposure. <br>
Mitigation: Do not accept or transmit personal text through chat; request authorized image or video inputs through the supported media flow instead. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite) <br>
- [Related npm MCP package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-mcp) <br>
- [Related repository](https://github.com/wefi-ai/ekyc-suite-mcp) <br>
- [eKYC Suite Face Compare](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-face-compare) <br>
- [eKYC Suite AI Guardian](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-ai-guardian) <br>
- [eKYC Suite Document OCR](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-document-ocr) <br>
- [eKYC Suite Media Labeling](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-media-labeling) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires EKYC_CLOUD_ENDPOINT and EKYC_CLOUD_API_KEY; processes only user-supplied media paths, public HTTPS URLs, or base64 media strings required by the selected command.] <br>

## Skill Version(s): <br>
1.1.18 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
