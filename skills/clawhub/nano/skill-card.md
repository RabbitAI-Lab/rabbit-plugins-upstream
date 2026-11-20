## Description:

Provides Nano (XNO) wallet operations, transaction analysis, and explorer lookups, including sending and receiving, balance checks, address validation, unit conversion, and Nano protocol guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[casualsecurityinc](https://clawhub.ai/user/casualsecurityinc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Nano accounts and transactions, manage wallet operations when requested, and provide address, payment, and explorer guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanner reports possible recipient substitution during transfers.

Mitigation: Verify the full destination address and amount through a trusted channel before any transfer.

Risk: Scanner reports unpinned package launches.

Mitigation: Review package launch behavior before installation and use the documented pinned xno-skills version.

Risk: Wallet queries may expose account activity to third-party RPC providers.

Mitigation: Review the configured RPC provider and avoid querying wallet information through providers whose privacy practices you do not accept.

## Reference(s):

- [Nano.org](https://nano.org)
- [Blocklattice explorer](https://blocklattice.io)
- [Nano block-lattice reference](artifact/references/blocklattice.md)
- [Nano wallet send and receive guidance](artifact/references/send.md)
- [Nano wallet receive guidance](artifact/references/receive.md)
- [NOMS signing support status](https://github.com/open-wallet-standard/core/pull/217)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and structured tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Wallet operations require user intent; wallet secrets are not exposed.]

## Skill Version(s):

5.1.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
