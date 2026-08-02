## Description: <br>
eKYC Suite Face Compare compares two consented face images for KYC and selfie verification and returns a structured 0-100 similarity score through a configured eKYC Suite Cloud backend. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agent developers, fintech onboarding teams, compliance engineers, and identity-verification builders use this skill to compare two authorized face images during human-reviewed KYC, selfie verification, and selfie-to-document workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends biometric face images to an operator-configured HTTPS eKYC backend. <br>
Mitigation: Install and run it only when the workflow is authorized to process biometric face images and the configured endpoint's retention and access policies are trusted. <br>
Risk: Optional client, workspace, source, and install metadata can add deployment identifiers to outbound requests. <br>
Mitigation: Set optional EKYC metadata variables only when deployment attribution is required. <br>
Risk: A face similarity score can be misused as standalone identity proof. <br>
Mitigation: Treat the score as one verification signal and apply business thresholds, retry rules, and human review appropriate to the deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-face-compare) <br>
- [Related npm MCP package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-face-compare-mcp) <br>
- [Parent eKYC Suite skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite) <br>
- [eKYC Suite AI Guardian](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-ai-guardian) <br>
- [eKYC Suite Document OCR](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-document-ocr) <br>
- [eKYC Suite Media Labeling](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-media-labeling) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [JSON response from the face comparison command, with setup and usage guidance in Markdown.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns a structured similarity score and backend response metadata from the configured deployment.] <br>

## Skill Version(s): <br>
1.0.14 (source: frontmatter, changelog, and server evidence; released 2026-07-29) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
