## Description:

eKYC Suite Face Compare compares two consented face images for KYC selfie verification and returns a structured 0-100 similarity score through an operator-configured eKYC Suite Cloud backend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, fintech onboarding teams, compliance engineers, and identity-verification builders use this skill to add human-reviewed face comparison for consented KYC onboarding, selfie-to-document matching, and applicant checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Biometric images are sensitive and are sent to a configured cloud backend.

Mitigation: Use the skill only after user authorization for biometric processing, with a trusted HTTPS endpoint and defined retention and access policies.

Risk: A similarity score can be misused as standalone identity proof or a fully automated high-impact decision.

Mitigation: Treat the score as one review signal, apply deployment-specific thresholds and retry rules, and keep consequential decisions in a human-reviewed workflow.

Risk: Misconfigured endpoint or credential handling could send media to the wrong backend or prevent secure processing.

Mitigation: Configure EKYC_CLOUD_ENDPOINT as a trusted HTTPS URL, provide EKYC_CLOUD_API_KEY through environment controls, and review optional attribution headers before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-face-compare)
- [Related MCP Package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-face-compare-mcp)
- [eKYC Suite Parent Skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite)
- [eKYC Suite AI Guardian](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-ai-guardian)
- [eKYC Suite Document OCR](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-document-ocr)
- [eKYC Suite Media Labeling](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-media-labeling)

## Skill Output:

**Output Type(s):** [json, shell commands, guidance]

**Output Format:** [JSON response with a 0-100 similarity score and backend metadata; documentation may include Markdown and shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires EKYC_CLOUD_ENDPOINT and EKYC_CLOUD_API_KEY; accepts two consented face-image inputs as local paths, public HTTPS URLs, or base64 strings.]

## Skill Version(s):

1.0.16 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
