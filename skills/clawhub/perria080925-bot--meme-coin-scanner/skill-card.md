## Description:

Guides a two-step, pay-per-request pre-buy scan of meme coins on BSC, Base, or Ethereum for rug-risk indicators and exit liquidity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[perria080925-bot](https://clawhub.ai/user/perria080925-bot)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and agents use this skill to screen meme-token addresses before buying, checking rug-risk signals and whether available liquidity may support an exit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanning sends token addresses to an external service.

Mitigation: Confirm that sharing each token address with the disclosed service is acceptable before making a request.

Risk: Each scan incurs USDC payments through x402.

Mitigation: Use a trusted x402 client and verify the recipient and payment amount before authorizing; never provide seed phrases or private keys.

Risk: Heuristic safety and liquidity metrics may not predict a rug or a viable exit.

Mitigation: Treat scan results as screening signals, not guarantees or financial advice.

## Reference(s):

- [Meme Coin Scanner on ClawHub](https://clawhub.ai/perria080925-bot/skills/meme-coin-scanner)
- [Paid scanning API endpoint](https://x402.bankr.bot/0xf436ca41bd0a236338bef57adeb4976677513010)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with HTTP request examples and guidance for interpreting JSON scan results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Two paid API requests per full scan; heuristic metrics are not financial advice.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
