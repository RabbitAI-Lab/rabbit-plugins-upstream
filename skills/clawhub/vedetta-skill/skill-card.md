## Description:

Buy pay-per-call market intel via x402. Dual rail: Base USDC (live) and Solana /sol/v1/* (live; paid feed settle proven; SVM client for Sol pay).

This skill is ready for commercial/non-commercial use.

## Publisher:

[lacryptorina](https://clawhub.ai/user/lacryptorina)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use Vedetta to request paid market-intelligence reads, cached signals, sentiment-versus-price divergence, predictions, and track-record data over x402. Outputs should be treated as descriptive research, not financial advice or trade instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill signs x402 micropayments using local wallet keys and can spend funded wallet balances.

Mitigation: Use only dedicated low-balance wallets, keep keys in environment variables, and check the x402 offer amount and payTo before paid calls.

Risk: Market-intelligence outputs could be mistaken for investment recommendations.

Mitigation: Present results as descriptive research only and do not convert stance, confidence, or signal fields into buy/sell instructions.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/lacryptorina/skills/vedetta-skill)
- [Vedetta upstream product](https://vedetta.dethboy.com)
- [Official live skill](https://vedetta.dethboy.com/SKILL.md)
- [Vedetta install documentation](https://vedetta.dethboy.com/install)
- [8004 specification](https://8004.qnt.sh)
- [x402 Synthex hub](https://x402synthex.xyz)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires terminal access, a dedicated low-balance wallet, and x402 offer checks before paid calls.]

## Skill Version(s):

2.12.2-v8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
