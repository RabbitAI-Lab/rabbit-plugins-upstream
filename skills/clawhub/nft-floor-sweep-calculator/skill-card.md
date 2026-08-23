## Description:

Calculates the total cost of sweeping N items off an NFT collection's floor by fetching live floor prices from Magic Eden for Solana collections or CoinGecko's free NFT API for EVM collections, then applying configurable marketplace-fee and slippage assumptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ssidharhubble](https://clawhub.ai/user/ssidharhubble)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to estimate the likely cost of sweeping a specified number of NFTs from a collection floor before checking the live marketplace. It is for planning and comparison only, not for executing trades or managing wallets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Collection slugs or NFT IDs are sent to Magic Eden or CoinGecko to fetch live pricing.

Mitigation: Use only if sharing those collection identifiers with the public pricing APIs is acceptable.

Risk: Sweep totals are rough estimates because the skill uses public floor-price APIs and a configurable slippage curve instead of full live order-book depth.

Mitigation: Verify the active marketplace order book, fees, and royalties before making any purchase decision.

Risk: The output may be mistaken for an executable trade quote or financial advice.

Mitigation: Treat the result as planning guidance only; the skill does not trade, access wallets, or place orders.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ssidharhubble/skills/nft-floor-sweep-calculator)
- [CoinGecko NFT list endpoint](https://api.coingecko.com/api/v3/nfts/list)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Plain text report or JSON from a Python CLI command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports floor price, item price estimates, subtotal, marketplace fee, total cost, and average price per item.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
