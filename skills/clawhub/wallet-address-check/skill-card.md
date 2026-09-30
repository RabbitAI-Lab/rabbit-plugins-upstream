## Description:

Checks EVM, Bitcoin-family, and TRON wallet-address formats before a transfer and flags suspicious formats for review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theory: All rights reserved

## Use Case:

Agents and their users can pre-screen a wallet address for recognizable EVM, Bitcoin-family, or TRON formatting before a transfer. A passing result is not confirmation that the address, network, or transfer is safe.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A format pass does not fully verify address checksums or guarantee that the recipient or transfer is safe.

Mitigation: Confirm the full address and intended network in a trusted wallet before transferring; consider a small test transfer.

Risk: The skill requests broader agent tools than its local format checker needs.

Mitigation: Review and restrict tool access to the minimum needed for local checking before installation.

## Reference(s):

- [Wallet Address Check on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/wallet-address-check)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain text or JSON with a pass/fail result, masked address, possible address family, and notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exit code 0 for pass, 1 for fail, and 2 for usage errors; passing is format screening only.]

## Skill Version(s):

1.0.3 (source: ClawHub server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
