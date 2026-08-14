## Description:

eKYC Suite is a ClawHub KYC skill for AI agents that supports remote KYC onboarding, identity verification, face liveness detection, selfie verification, KYC document OCR, deepfake screening, and media risk review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits)

### License/Terms of Use:

MIT-0

## Use Case:

AI agent builders, fintech onboarding teams, risk and compliance engineers, and KYC workflow developers use this skill to run consent-based identity media checks, document OCR, liveness screening, and media risk review inside human-reviewed onboarding workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Identity images, videos, and document photos are sent to the configured eKYC backend.

Mitigation: Run the skill only after confirming user authorization and the backend's retention, storage, and access-control policy.

Risk: KYC outputs may influence legal, financial, or similarly high-impact decisions.

Mitigation: Treat results as advisory review signals and require human review plus appropriate business controls before final decisions.

Risk: Uploaded identity documents and bank-card images may contain sensitive personal data.

Mitigation: Use masking where possible, restrict access to outputs, and avoid sending typed personal identifiers through chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite)
- [Related npm MCP package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-mcp)
- [Related repository link from metadata](https://github.com/wefi-ai/ekyc-suite-mcp)
- [eKYC Suite Face Compare focused skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-face-compare)
- [eKYC Suite AI Guardian focused skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-ai-guardian)
- [eKYC Suite Document OCR focused skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-document-ocr)
- [eKYC Suite Media Labeling focused skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-media-labeling)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns advisory identity verification, OCR, liveness, and media risk signals for human review.]

## Skill Version(s):

1.1.24 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
