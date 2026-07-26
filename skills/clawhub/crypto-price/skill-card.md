## Description: <br>
Get cryptocurrency token price and generate candlestick charts via CoinGecko API or Hyperliquid API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[evgyur](https://clawhub.ai/user/evgyur) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to answer cryptocurrency price and market-data requests by fetching public price data and returning a price summary with a generated candlestick chart when available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes outbound requests to CoinGecko and Hyperliquid for public market data, so API availability, rate limits, or third-party data quality can affect answers. <br>
Mitigation: Document the required egress endpoints in stricter environments and treat returned prices as informational market data rather than financial advice. <br>
Risk: The script writes temporary cache and chart files under /tmp. <br>
Mitigation: Run it with expected /tmp write permissions and use routine cleanup for generated crypto_price and crypto_chart files. <br>
Risk: The skill depends on matplotlib for chart rendering. <br>
Mitigation: Pin and scan matplotlib in managed deployments before release. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/evgyur/skills/crypto-price) <br>
- [CoinGecko API](https://api.coingecko.com/api/v3/) <br>
- [Hyperliquid API](https://api.hyperliquid.xyz/info) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, files] <br>
**Output Format:** [JSON from the local script, plus a plain-text price summary and MEDIA line for the generated PNG chart when available.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, matplotlib, outbound API access to CoinGecko or Hyperliquid, and /tmp write access for cache and chart files.] <br>

## Skill Version(s): <br>
0.2.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
