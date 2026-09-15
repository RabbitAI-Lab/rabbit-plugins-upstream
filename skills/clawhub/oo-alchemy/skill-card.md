## Description:

Alchemy connector guidance for searching and reading Alchemy data through an OOMOL-connected account instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to query Ethereum mainnet asset transfers, NFT metadata, owner NFTs, ERC-20 balances, and token metadata through an OOMOL-connected Alchemy account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can run unverified remote installer scripts on the user's machine.

Mitigation: Review official installation instructions, use a trusted package source, and avoid pipe-to-shell installer commands unless local code execution risk is accepted.

Risk: Alchemy access is mediated through OOMOL and requires oo CLI setup and account connection.

Mitigation: Install only when the user is comfortable with OOMOL-mediated access and has confirmed the account connection and billing state.

## Reference(s):

- [ClawHub Alchemy Skill](https://clawhub.ai/oomol/skills/oo-alchemy)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Installation Guide](https://cli.oomol.com/install-guide.md)
- [Alchemy Homepage](https://www.alchemy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output should inspect the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
