## Description:

BTCPay Server helps agents read, create, and update BTCPay Server stores and invoices through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, merchants, and operators use this skill to inspect BTCPay Server stores and invoices, create invoices, update invoice metadata, and mark invoice status through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run an unverified internet installer directly in a shell.

Mitigation: Review the install step before use and prefer verified official releases or package-manager instructions with checksums or signatures.

Risk: BTCPay write actions can create invoices, update invoice metadata, or manually mark invoices as settled or invalid.

Mitigation: Fetch the live action schema and confirm the exact payload and expected effect with the user before running any write action.

## Reference(s):

- [BTCPay Server homepage](https://btcpayserver.org)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-btcpay-server)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live connector schemas before constructing action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
