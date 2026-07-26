## Description: <br>
eKYC Suite Face Compare compares two consented face images for KYC and eKYC selfie verification and returns a structured 0-100 similarity score from the configured eKYC Suite Cloud backend. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agent developers, fintech onboarding teams, compliance engineers, and identity-verification builders use this skill to compare two authorized face images as one signal in human-reviewed KYC onboarding and selfie-to-document checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes biometric face images by sending them to the configured eKYC Suite Cloud endpoint. <br>
Mitigation: Use it only with user authorization for biometric processing, defined retention and access policies, and an operator-controlled HTTPS endpoint. <br>
Risk: A similarity score can be over-relied on as proof of identity. <br>
Mitigation: Treat the score as one verification signal, apply deployment-specific thresholds and retry rules, and route uncertain or high-impact outcomes to human review. <br>
Risk: Optional attribution environment variables are forwarded as request headers when set. <br>
Mitigation: Keep optional source, client, workspace, and install context values free of sensitive data that should not be sent to the backend. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-face-compare) <br>
- [Related npm MCP Package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-face-compare-mcp) <br>
- [Parent eKYC Suite Skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite) <br>
- [eKYC Suite AI Guardian](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-ai-guardian) <br>
- [eKYC Suite Document OCR](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-document-ocr) <br>
- [eKYC Suite Media Labeling](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-media-labeling) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [JSON result with concise explanatory text or Markdown guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns a similarity score and available backend response metadata; the score should be treated as a verification signal rather than standalone legal identity proof.] <br>

## Skill Version(s): <br>
1.0.10 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
