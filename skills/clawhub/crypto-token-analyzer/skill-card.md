## Description:

Analyze a cryptocurrency token by contract address and chain. Fetch price, volume, liquidity, price changes, tags, security risks, and trend signals from DexScreener plus block explorers and GoPlus. Give subjective bullish/bearish/uncertain view and position strategy (clear/add/hold if holding; buy/watch if empty). Trigger on contract address+chain, token analysis, 看涨看跌, K线, 策略建议, honeypot check, or similar crypto token queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sqxy090123](https://clawhub.ai/user/sqxy090123)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze crypto tokens from a contract address and chain, combining live market data, token-security checks, and trend signals. It supports research-oriented bullish, bearish, or uncertain views with holder and watcher strategy commentary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake subjective buy, watch, hold, add, or clear-position commentary for financial advice.

Mitigation: Treat outputs as research support only, verify high-risk tokens independently, and control position sizing before trading.

Risk: Public token, market, and explorer data can be sparse, delayed, or unavailable, especially for new tokens and Solana assets.

Mitigation: Surface data gaps clearly, default uncertain cases to watch-and-verify guidance, and recommend manual checks on explorers and DexScreener.

## Reference(s):

- [Data Sources & Endpoints](references/data-sources.md)
- [Security Checklist](references/security-checklist.md)
- [DexScreener API](https://api.dexscreener.com)
- [GoPlus Token Security API](https://api.gopluslabs.io/api/v1/token_security/{chain_id}?contract_addresses={address})
- [DexScreener Token Page](https://dexscreener.com/{chain}/{tokenAddress})
- [GeckoTerminal Token Page](https://www.geckoterminal.com/{chain}/tokens/{tokenAddress})

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Shell commands, Guidance]

**Output Format:** [Markdown or natural-language text with optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Matches the current conversation language and includes a concise risk note.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
