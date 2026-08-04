## Description: <br>
Buy pay-per-call market intel via x402 using dual rails: Base USDC and Solana /sol/v1/*. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lacryptorina](https://clawhub.ai/user/lacryptorina) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to request live or cached market-intelligence reads on crypto, US stocks, and macro assets through paid x402 API calls. It supports descriptive research workflows such as sentiment, narrative, divergence, prediction, event, and track-record checks, and it should not be used for trade execution, custody, or financial advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet keys may be exposed or used for unintended live micropayments if a main wallet or poorly protected shell environment is used. <br>
Mitigation: Use only dedicated low-balance Base or Solana wallets, keep keys in local environment variables, avoid terminal history or logs, and verify the 402 amount and payTo before paid calls. <br>
Risk: Market-intelligence responses could be mistaken for investment recommendations. <br>
Mitigation: Present outputs only as descriptive research and do not use them for trade execution, custody decisions, or buy/sell advice. <br>


## Reference(s): <br>
- [Vedetta upstream product](https://vedetta.dethboy.com) <br>
- [Official live skill](https://vedetta.dethboy.com/SKILL.md) <br>
- [ClawHub listing](https://clawhub.ai/lacryptorina/skills/vedetta-skill) <br>
- [Vedetta 8004 metadata](https://vedetta.dethboy.com/.well-known/8004-vedetta.json) <br>
- [x402 Synthex hub](https://x402synthex.xyz) <br>
- [8004 specification](https://8004.qnt.sh) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API response handling] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May initiate paid x402 API calls when configured with dedicated low-balance wallet keys; market output is descriptive research, not financial advice.] <br>

## Skill Version(s): <br>
2.12.1-v8 (source: SKILL.md frontmatter and server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
