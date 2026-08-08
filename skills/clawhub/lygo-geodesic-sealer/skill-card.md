## Description:

LYGO Geodesic Sealer signs local software attestations, locks them to dual-ledger Merkle roots, and phase-aligns nodes without collapse, with optional fixed HTTPS GET checks for public ledgers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deepseekoracle](https://clawhub.ai/user/deepseekoracle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to create, verify, and optionally persist local P6-style software attestation artifacts for node state, dual-ledger Merkle locks, and phase alignment. It is for software attestation only and does not claim TPM or hardware attestation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attestations may include hashes of the truth and chaos inputs supplied by the user.

Mitigation: Use non-sensitive inputs and do not paste private secrets into truth or chaos payloads.

Risk: Optional public ledger checks make fixed HTTPS GET requests.

Mitigation: Leave network access disabled unless public ledger checks are intended, and use --network only for that purpose.

Risk: Local JSON artifact writes can persist attestation data.

Mitigation: Write artifacts only with explicit --write or --write-default plus --i-consent, and review the target path before consenting.

Risk: Software attestation can be mistaken for TPM or hardware attestation.

Mitigation: Treat this skill as software attestation only and pair it with a hardware attestation path when hardware evidence is required.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/deepseekoracle/skills/lygo-geodesic-sealer)
- [Project Homepage](https://github.com/DeepSeekOracle/lygo-protocol-stack/tree/main/docs/skills/lygo-geodesic-sealer)
- [Source Repository](https://github.com/DeepSeekOracle/lygo-protocol-stack)
- [Agent Contract](references/AGENT_CONTRACT.md)
- [Security Notes](references/SECURITY.md)
- [SkillSpector Audit Response](references/SKILLSPECTOR_AUDIT.md)
- [Minimal Attestation Example](examples/minimal-attest.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON seal, lock, attestation, status, and verification outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-first by default; optional HTTPS GET checks require --network, and local JSON artifact writes require --i-consent.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
