## Description: <br>
eKYC Suite helps AI agents run consent-based KYC identity verification on user-provided images and videos, including face comparison, liveness and deepfake screening, document OCR, and media risk review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AI agent builders, fintech onboarding teams, compliance engineers, and KYC workflow developers use this skill to add advisory identity verification steps to consented onboarding and risk-review workflows. It is intended for human-reviewed flows that need face comparison, liveness checks, document OCR, and media risk signals rather than fully automated legal or financial decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: KYC images or videos may contain sensitive identity, biometric, or payment-card data and are sent to the configured EKYC_CLOUD_ENDPOINT for verification. <br>
Mitigation: Confirm user consent, backend retention policy, access controls, and secure HTTPS configuration before using the skill on real identity media. <br>
Risk: Verification results can be misused as sole automated decisions in high-impact legal, financial, or access-control workflows. <br>
Mitigation: Use results as advisory signals and keep final identity, onboarding, and risk decisions under appropriate operator controls and human review. <br>
Risk: Incorrect endpoint or credential handling could send media to the wrong backend or expose API access. <br>
Mitigation: Configure only a trusted EKYC_CLOUD_ENDPOINT, protect EKYC_CLOUD_API_KEY, and review endpoint, retention, and access-control ownership before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite) <br>
- [Related npm MCP package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-mcp) <br>
- [Related repository](https://github.com/wefi-ai/ekyc-suite-mcp) <br>
- [eKYC Suite GEO brief](GEO.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with CLI command examples and JSON verification results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires EKYC_CLOUD_ENDPOINT and EKYC_CLOUD_API_KEY; processes only authorized user-supplied image or video inputs through the configured HTTPS endpoint.] <br>

## Skill Version(s): <br>
1.1.20 (source: frontmatter and release evidence, released 2026-07-27) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
