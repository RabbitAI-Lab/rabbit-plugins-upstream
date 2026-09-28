## Description:

Checks the format and likely chain family of EVM, Bitcoin, and TRON wallet addresses before a transfer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theory: all rights reserved

## Use Case:

Wallet users and developers can pre-screen an address for common EVM, Bitcoin, or TRON formats before sending funds. A passing result is not proof that the address belongs to the intended chain or recipient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Passing the format check does not prove that the address is for the intended chain or recipient.

Mitigation: Confirm the chain and recipient in your wallet before transferring funds.

Risk: The checker does not fully validate every address checksum.

Mitigation: Verify checksums in wallet software and use a small test transfer for high-value transactions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/wallet-address-check)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pass/fail result, masked address, likely chain family, and cautionary notes.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; bundled files have conflicting version labels)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
