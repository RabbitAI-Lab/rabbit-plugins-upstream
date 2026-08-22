## Description:

Scans spot and perpetual futures prices across Binance, Bybit, OKX, and Deribit public REST APIs to report basis percentage, approximate annualized basis, and current 8-hour funding rate for requested symbols.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ssidharhubble](https://clawhub.ai/user/ssidharhubble)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, AI agent operators, and crypto researchers use this skill to run one-shot or watched cross-exchange basis scans before evaluating cash-and-carry or funding-rate arbitrage opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts Binance, Bybit, OKX, and Deribit public APIs for the symbols being scanned.

Mitigation: Use it only in environments where outbound HTTPS to those exchange APIs is allowed and where querying those symbols is acceptable.

Risk: The annualized basis value is a rough approximation and not a funding-payment forecast or trading recommendation.

Mitigation: Treat the output as research context and independently verify live prices, funding, fees, and position assumptions before acting.

Risk: The scanner does not use order-book depth, so it does not account for slippage or executable size.

Mitigation: Check live order books and venue liquidity separately before sizing any spot-perp trade.

Risk: Exchange rate limits, unavailable instruments, or blocked requests can produce error rows or missing data.

Mitigation: Review error rows before relying on a scan, narrow exchanges with the exchange selector when needed, and re-run scans when data is incomplete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ssidharhubble/skills/perp-basis-scanner)
- [README](artifact/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown guidance with shell command examples; scanner output is table text or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only market-data scanner; no API keys, account access, or trade execution.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
