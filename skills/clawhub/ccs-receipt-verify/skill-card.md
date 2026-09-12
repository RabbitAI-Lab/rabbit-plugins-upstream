## Description:

Verifies CCS AI-agent audit receipts by checking RFC 8785 JSON canonicalization, SHA-256 content hashes, Ed25519 signatures, and schema/tamper evidence, with local verification by default and optional online verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dshcorrectover](https://clawhub.ai/user/dshcorrectover)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security reviewers, and agent operators use this skill to verify whether a CCS audit receipt was signed by a known issuer and whether signed receipt fields were changed after issuance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is not strictly offline despite offline-first positioning; online mode can send receipts and public keys to hosted or custom endpoints.

Mitigation: Use default local mode for sensitive receipts, and use --online or custom endpoints only when the destination is explicitly trusted.

Risk: Online mode may forward configured API keys or payment proof environment variables.

Mitigation: Avoid setting CCS_API_TOKEN, CCS_PAYMENT_PROOF, CCS_PAY_TOKEN, or CCS_API_ENDPOINT unless credential forwarding is intentional for the selected endpoint.

Risk: Bundled signing and MCP-checkup code expands the review surface beyond receipt verification.

Mitigation: Review shipped scripts before deployment and restrict operational use to the receipt verification entry points required for the release.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dshcorrectover/skills/ccs-receipt-verify)
- [Publisher Profile](https://clawhub.ai/user/dshcorrectover)
- [Correctover Homepage](https://correctover.com/?utm_source=clawhub&utm_medium=skill&utm_campaign=ccs_verify)
- [Source Skill Definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with bash command examples and optional machine-readable JSON verification reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exit codes distinguish valid receipts, invalid or tampered receipts, input/network errors, and online payment-required responses.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; artifact frontmatter is 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
