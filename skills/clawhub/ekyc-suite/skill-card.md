## Description:

eKYC Suite helps agents conduct consent-based face comparison, liveness checks, identity-document OCR, deepfake screening, and media risk review through a configured cloud service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits)

### License/Terms of Use:

MIT-0

## Use Case:

Fintech onboarding teams, risk and compliance engineers, and agent developers use this skill to obtain advisory identity and media-review signals for authorized, human-reviewed KYC workflows.

### Deployment Geography for Use:

Global, subject to local privacy and identity-verification requirements and service availability.

## Known Risks and Mitigations:

Risk: Identity documents, bank cards, selfies, and videos contain highly sensitive personal data and are sent to the configured cloud service.

Mitigation: Use only an operator-trusted HTTPS endpoint after confirming user authorization, with defined retention and access-control rules.

Risk: Verification and risk signals may be insufficient for consequential identity, financial, or eligibility decisions.

Mitigation: Keep appropriate business controls and human review; never use these results as the sole basis for significant automated decisions.

## Reference(s):

- [eKYC Suite ClawHub release](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite)
- [Related GitHub repository (metadata link; release provenance unavailable)](https://github.com/wefi-ai/ekyc-suite-mcp)
- [Related npm package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries of structured verification results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Explain scores and OCR fields, mask sensitive details where possible, and treat results as advisory rather than final decisions.]

## Skill Version(s):

1.1.28 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
