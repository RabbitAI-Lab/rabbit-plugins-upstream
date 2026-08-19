## Description:

Generates tokenomics due-diligence reports for crypto tokens, including unlock pressure, rug-pull risk, holder concentration, and peer comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heroinyan-stack](https://clawhub.ai/user/heroinyan-stack)

### License/Terms of Use:

MIT-0

## Use Case:

External crypto researchers, traders, and developers use this skill to turn a contract address and chain ID into a structured tokenomics research report. It is intended for due-diligence support, not personalized investment, legal, or regulatory advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can produce direct-sounding crypto action guidance despite educational-only limits.

Mitigation: Treat outputs as unverified research notes, not investment advice; verify on-chain data independently and avoid personalized buy, sell, hold, or day-trade recommendations.

Risk: Server security evidence marks the release as suspicious even though it does not appear to trade, steal data, persist state, or run code.

Mitigation: Review carefully before installing and do not provide API keys unless they are needed for rate limits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heroinyan-stack/skills/tokenomics-decoder)
- [Etherscan](https://etherscan.io)
- [Solscan](https://solscan.io)
- [Basescan](https://basescan.org)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown report with tables, risk scores, source links, and a disclaimer footer]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a contract address and chain ID; critical data points should link to block explorers; no wallet connectivity or trade execution.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
