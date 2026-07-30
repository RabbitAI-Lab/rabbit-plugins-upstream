## Description: <br>
eKYC Suite is a ClawHub KYC skill for AI agents that supports remote KYC onboarding, identity verification, face liveness detection, selfie verification, KYC document OCR, deepfake screening, and media risk review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, fintech onboarding teams, risk and compliance engineers, and KYC workflow developers use this skill to add consent-based identity verification, document OCR, liveness, and media-risk checks to human-reviewed agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles biometric media and identity-document or bank-card images that may contain sensitive personal data. <br>
Mitigation: Install only with user consent, masking where appropriate, access controls, a clear retention policy, and a trusted eKYC backend. <br>
Risk: Verification results could significantly affect a person's access to financial, employment, or other high-trust services. <br>
Mitigation: Use results as review signals and keep human review for decisions that could significantly affect a person. <br>
Risk: The skill depends on an operator-configured cloud endpoint and API key. <br>
Mitigation: Use a trusted HTTPS endpoint, protect the API key, and restrict backend access to the intended eKYC service. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite) <br>
- [Related npm MCP package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-mcp) <br>
- [Related GitHub repository](https://github.com/wefi-ai/ekyc-suite-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [JSON command responses with Markdown usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires EKYC_CLOUD_ENDPOINT and EKYC_CLOUD_API_KEY; commands process only user-supplied media inputs.] <br>

## Skill Version(s): <br>
1.1.22 (source: frontmatter, changelog, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
