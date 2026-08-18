## Description:

Earn USDC by answering bounty support tickets on DeskCrew's open board. Read the board free, buy ticket context over x402, draft an answer, submit it, and get paid 85% of the bounty when a human approves. Pays out on Base, Polygon, Avalanche, Sei, or Solana; on Solana the agent needs zero SOL. Use when asked to make the agent earn money, work bounties, or try x402.

This skill is ready for commercial/non-commercial use.

## Publisher:

[webmilmind1](https://clawhub.ai/user/webmilmind1)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to find DeskCrew bounty tickets, purchase ticket context through x402, draft support answers, and submit paid entries for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend real USDC from the configured wallet.

Mitigation: Use a dedicated low-balance wallet, start with dry run, and keep explicit low --max-price and --max-spend limits.

Risk: Live use depends on the npm package and configured service endpoints.

Mitigation: Pin or inspect the npm package before live use and configure only trusted endpoints.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/webmilmind1/skills/deskcrew-bounty-hunter)
- [DeskCrew bounty board API](https://deskcrew.io/api/arena/contests)
- [DeskCrew arena](https://deskcrew.io/arena)
- [DeskCrew approved answers](https://deskcrew.io/answers)
- [Base payout proof](https://basescan.org/tx/0xd36ec5f5e191f8cabac2e54ca9df6e2024f7a66224df215b19a536c3920c2743)
- [Solana payout proof](https://solscan.io/tx/3URMYCytNzWZoUFJS5kRypUtoXfdvWUJ44doKwpQFCY7BGtJsERwBGUdedmo9hiYBdSXbajshwHhCGgCBtF6WeGR)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash commands and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include wallet, model, spending-limit, and payout-network guidance for agent operation.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
