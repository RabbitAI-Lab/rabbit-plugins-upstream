## Description: <br>
eKYC Suite Face Compare helps agents compare two consented face images for KYC and selfie verification and returns a structured 0-100 similarity score through a configured eKYC Suite Cloud backend. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agent developers, fintech onboarding teams, compliance engineers, and identity-verification builders use this skill to compare two consented face images for human-reviewed KYC onboarding, selfie-to-document matching, and face-similarity checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Face images are biometric data and may be regulated or sensitive. <br>
Mitigation: Install and run the skill only where consent, a lawful processing basis, retention policy, and access controls are already in place. <br>
Risk: The skill sends the two supplied images to an operator-configured eKYC cloud endpoint. <br>
Mitigation: Configure only a trusted HTTPS endpoint, protect EKYC_CLOUD_API_KEY, and confirm the backend's retention and access controls before use. <br>
Risk: A similarity score can be misleading if treated as standalone identity proof. <br>
Mitigation: Use the score as one review signal with deployment-specific thresholds, retry rules, and human review for high-impact decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-face-compare) <br>
- [Related npm MCP package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-face-compare-mcp) <br>
- [Parent eKYC Suite skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite) <br>
- [eKYC Suite AI Guardian](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-ai-guardian) <br>
- [eKYC Suite Document OCR](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-document-ocr) <br>
- [eKYC Suite Media Labeling](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-media-labeling) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples; command output is JSON containing the face-comparison result and available response metadata.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires EKYC_CLOUD_ENDPOINT and EKYC_CLOUD_API_KEY; accepts two consented image inputs as local file paths, public HTTPS URLs, or base64 image strings.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release evidence and SKILL.md frontmatter; changelog released 2026-07-27) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
