## Description:

Verify signed SAR v0.1 settlement receipts locally with Ed25519 and RFC 8785 canonicalization, and optionally request DefaultVerifier-signed receipts for remote issuance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nutstrut](https://clawhub.ai/user/nutstrut)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to verify whether SAR settlement receipts are cryptographically valid before trusting a task-complete claim, chaining downstream actions, using a receipt as evidence, or acting on settlement-adjacent claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changing SAR_KEYS_REGISTRY_PATH can alter the trust root used for receipt verification.

Mitigation: Use the bundled registry by default; only override it with a registry you independently trust and verify.

Risk: Remote receipt issuance sends the task ID, acceptance spec, and supplied output to defaultverifier.com.

Mitigation: Use local verification for sensitive outputs and request remote issuance only for data suitable to send to that service.

Risk: A cryptographically valid receipt does not prove legal settlement finality, payment finality, fund custody, or approval of downstream actions.

Mitigation: Treat verification results as signed evidence only, and require separate business, legal, or operational checks before acting on them.

Risk: Receipts signed by keys absent from the bundled registry can fail local verification after signer rotation.

Mitigation: Update the skill package or use a verified fresh registry when validating receipts from newer signing keys.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nutstrut/skills/settlement-witness)
- [DefaultVerifier homepage](https://defaultverifier.com)
- [Live SAR public key registry](https://defaultverifier.com/.well-known/sar-keys.json)
- [Receipt explorer](https://defaultverifier.com/verified)
- [SAR v0.1 canonicalization reference](artifact/spec/canonicalization.md)
- [Security and trust model](artifact/SECURITY.md)
- [Network behavior](artifact/EGRESS.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON verifier results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local verification emits typed JSON including validity, receipt ID, key ID, verdict, errors, signer lifecycle status, trust flags, registry snapshot hash, and offline verification notes.]

## Skill Version(s):

0.1.4 (source: frontmatter, changelog, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
