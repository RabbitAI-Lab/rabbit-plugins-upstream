## Description:

Verify CCS AI-agent audit receipts locally by checking Ed25519 signatures, RFC 8785 JCS canonicalization, SHA-256 content hashes, schema validity, and tamper evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dshcorrectover](https://clawhub.ai/user/dshcorrectover)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to verify whether a CCS audit receipt was signed by the issuer and whether signed receipt fields changed after issuance. It is suited for local receipt authenticity checks, tamper review, and optional hosted verification when the user explicitly chooses online mode.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional online verification can send receipts, issuer public keys, and environment-provided credentials to a configured service endpoint.

Mitigation: Use default local mode for sensitive receipts; use --online only when the endpoint is trusted and endpoint overrides cannot be influenced.

Risk: Environment variables such as CCS_API_TOKEN, CCS_PAYMENT_PROOF, and CCS_PAY_TOKEN may be sent during online verification.

Mitigation: Avoid setting those variables in shared or untrusted environments, especially when endpoint configuration is not tightly controlled.

Risk: Canonicalization compatibility may be imperfect for receipts involving Unicode or floating-point values.

Mitigation: Treat related verification failures as review triggers and confirm results against the issuer or a trusted reference verifier before making high-impact decisions.

## Reference(s):

- [Correctover CCS homepage](https://correctover.com/?utm_source=clawhub&utm_medium=skill&utm_campaign=ccs_verify)
- [ClawHub skill listing](https://clawhub.ai/dshcorrectover/skills/ccs-receipt-verify)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Human-readable text reports or machine-readable JSON reports, with Markdown usage examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default local mode performs offline verification; online mode is explicit and may require endpoint and credential configuration.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
