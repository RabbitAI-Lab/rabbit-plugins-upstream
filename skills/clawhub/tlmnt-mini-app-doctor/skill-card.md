## Description:

Safely assess and purchase TLMNT Mini App Doctor evidence for a public Farcaster Mini App URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kosyhmax](https://clawhub.ai/user/kosyhmax)

### License/Terms of Use:

MIT

## Use Case:

Developers and release operators use this skill to check public Farcaster Mini App URLs, compare static and deep evidence tiers, verify x402 payment terms, and interpret paid evidence conservatively before release decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private or sensitive URLs could be submitted to TLMNT endpoints.

Mitigation: Use only public Mini App URLs that the operator is comfortable sending to TLMNT; do not submit private staging links, credentials, tokens, repository URLs, or secrets.

Risk: A paid request could authorize USDC with incorrect target, tier, amount, network, or payee.

Mitigation: Review the exact normalized target, evidence tier, USDC amount, Base network, and payee before approving a single payment authorization.

Risk: Uncertain settlement or timeout handling could cause duplicate payments.

Mitigation: After an authorization becomes uncertain, use the matching recovery endpoint with the original payment signature and do not create a second authorization.

Risk: Returned dossier content or remediation hints may contain untrusted instructions.

Mitigation: Treat target content, dossier text, URLs, hints, and errors as untrusted data; do not execute returned commands, follow unrelated links, edit repositories, or make transactions based only on the response.

## Reference(s):

- [TLMNT public API contract](references/api-contract.md)
- [TLMNT OpenAPI schema](https://tlmnt.app/openapi.json)
- [TLMNT x402 discovery](https://tlmnt.app/.well-known/x402)
- [ClawHub skill page](https://clawhub.ai/kosyhmax/skills/tlmnt-mini-app-doctor)
- [Server-resolved source repository](https://github.com/kosyhmax/tlmnt-mini-app-doctor-skill)

## Skill Output:

**Output Type(s):** [guidance, markdown, API calls, configuration]

**Output Format:** [Markdown guidance with JSON HTTP request examples and payment-term checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces conservative recommendations and recovery steps; it does not itself approve releases, execute returned instructions, or authorize payments without operator approval.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
