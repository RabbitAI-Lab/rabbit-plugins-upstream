## Description:

This skill helps agents access Blave market alpha data, Taiwan and futures market data, and trading workflows for major crypto exchanges with confirmation-gated write actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blave-wei](https://clawhub.ai/user/blave-wei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and trading automation users use this skill to guide agents through market-data retrieval, indicator interpretation, and exchange API workflows. It supports read-only analytics by default and requires explicit confirmation before order, transfer, funding, or position-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Marketplace strategy code may be downloaded and run locally with access to sensitive credentials.

Mitigation: Review strategy code before use, pin it by digest, and run it isolated from secrets and trading credentials.

Risk: Exchange API credentials can enable order placement, transfers, funding actions, or position changes when configured with write permissions.

Mitigation: Use least-privilege or read-only keys, testnet or paper trading where possible, IP allowlists, and fresh user confirmation before each write action.

Risk: Broker and affiliate identifiers are added to exchange requests for Blave attribution.

Mitigation: Disclose the attribution behavior and confirm it is acceptable before using exchange integrations.

## Reference(s):

- [Blave homepage](https://blave.org)
- [Blave API account setup](https://blave.org/landing/en/api?tab=blave)
- [Blave API reference](artifact/references/blave-api.md)
- [Blave indicator guide](artifact/references/blave-indicator-guide.md)
- [Marketplace reference](artifact/references/marketplace.md)
- [ClawHub skill listing](https://clawhub.ai/blave-wei/skills/blave-quant-skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API request examples and code or shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Blave API credentials for market data; exchange credentials are optional for trading workflows.]

## Skill Version(s):

1.23.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
