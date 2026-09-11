## Description:

Query Bitcoin L1 blockchain data with USD pricing, including address balances, transaction details, UTXO analysis, fee estimates, mempool statistics, recent blocks, network status, and BTC price lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bronoman](https://clawhub.ai/user/bronoman)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch live, read-only Bitcoin blockchain and market context for dashboards, monitoring, transaction inspection, fee review, and operational research. It is for data retrieval and analysis, not trading advice, transaction execution, wallet access, or fee guarantees.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Address and transaction lookups are sent to Mempool.space, which can reveal lookup interest in public Bitcoin addresses or transactions.

Mitigation: Use a self-hosted Mempool endpoint through BITCOIN_API_URL when lookup privacy matters.

Risk: A COINGECKO_API_KEY found in a local .env file may be included in a CoinGecko request URL.

Mitigation: Run the skill from a clean directory and avoid storing unrelated secrets near the skill execution path.

Risk: Fee and price outputs are point-in-time data and may be stale, rate-limited, or unavailable.

Mitigation: Verify important financial or operational decisions against independent data sources before acting.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/bronoman/hermes/tree/main/skills/bitcoin)
- [ClawHub skill page](https://clawhub.ai/bronoman/skills/bitcoin-2)
- [Mempool.space REST API documentation](https://mempool.space/docs/api/rest)
- [CoinGecko simple price endpoint](https://api.coingecko.com/api/v3/simple/price)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and terminal-style text output from the helper CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live network and price responses depend on Mempool.space and CoinGecko availability, rate limits, and point-in-time data freshness.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
