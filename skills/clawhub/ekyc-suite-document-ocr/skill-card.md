## Description:

eKYC Suite Document OCR extracts structured fields from consented Chinese ID cards, bank cards, driver's licenses, and vehicle licenses through an operator-configured HTTPS eKYC Suite Cloud endpoint for KYC and document-review workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits)

### License/Terms of Use:

MIT-0

## Use Case:

KYC onboarding, identity operations, fintech document review, and human-reviewed document-verification teams use this skill to request structured OCR extraction from supported document images. It is intended for consented document processing and not for unrestricted OCR, authenticity proof, face comparison, liveness checks, or final high-impact decisions without review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes sensitive identity and financial document images through a configured remote OCR endpoint.

Mitigation: Use it only for authorized KYC workflows with consent, compliant endpoint configuration, access controls, retention limits, and masking of sensitive fields.

Risk: OCR output may be incomplete, unreadable, or unsuitable as proof of document authenticity.

Mitigation: Do not guess missing fields; request a clearer supported image when needed and route uncertain or high-impact cases to an authorized human reviewer.

Risk: Optional source, client, workspace, or install context environment variables can be forwarded as request headers.

Mitigation: Keep optional context variables free of sensitive personal data and configure them only when needed for deployment context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-document-ocr)
- [Related npm MCP package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-document-ocr-mcp)
- [Parent eKYC Suite skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration]

**Output Format:** [JSON OCR response emitted by command-line tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires EKYC_CLOUD_ENDPOINT and EKYC_CLOUD_API_KEY; accepts one local file path, public HTTPS URL, or base64 document image per request.]

## Skill Version(s):

1.0.16 (source: frontmatter, changelog, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
