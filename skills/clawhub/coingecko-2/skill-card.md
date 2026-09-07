## Description:

Live Bitcoin & crypto price data via CoinGecko API. Fetch BTC/USD, ETH/USD, multi-asset quotes. Supports both Demo (free) and Pro API keys. No credentials in prompts—only .env isolation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bronoman](https://clawhub.ai/user/bronoman)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Hermes users use this skill to fetch read-only cryptocurrency price data, health-check API connectivity, and format current Bitcoin or multi-asset quotes for dashboards, alerts, or agent workflows. It is data-only and should not be treated as trading or financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags broad API-key handling.

Mitigation: Use only CG_API_KEY from a skill-owned environment file, remove the generic API_KEY fallback, and avoid printing credentials while troubleshooting.

Risk: The security evidence flags credential-like documentation examples.

Mitigation: Replace concrete-looking keys with placeholders before publication and rotate any real key that may have been copied into documentation.

Risk: The skill makes HTTPS calls to CoinGecko and Kraken, including a fallback path.

Mitigation: Install only in environments that permit those egress destinations, and disable or remove the Kraken fallback where strict egress control is required.

Risk: The skill provides market data that may be delayed, unavailable, or unsuitable for trading decisions.

Mitigation: Use the output as informational context only, verify important prices independently, and do not treat the skill as financial advice.

## Reference(s):

- [Server-resolved source repository](https://github.com/bronoman/hermes/tree/main/skills/coingecko)
- [ClawHub skill page](https://clawhub.ai/bronoman/skills/coingecko-2)
- [Publisher profile](https://clawhub.ai/user/bronoman)
- [Technical reference](artifact/references/DESCRIPTION.md)
- [CoinGecko API documentation](https://www.coingecko.com/en/api/documentation)
- [CoinGecko API pricing](https://www.coingecko.com/en/api/pricing)
- [Kraken public ticker API](https://api.kraken.com/0/public/Ticker)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-shaped script outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only HTTPS price lookups; CoinGecko access can use CG_API_KEY, and Kraken fallback is controlled by CG_FALLBACK_KRAKEN.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
