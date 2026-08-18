## Description:

Generates a non-advisory directional research brief for a US stock or index proxy by purchasing and synthesizing nine quoted market, technical, news, social, earnings, and macro data reads through a MetaMask Agent Wallet.

This skill is for research and development only.

## Publisher:

[selat-dev](https://clawhub.ai/user/selat-dev)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to buy quoted data reads for a US equity ticker or index proxy and synthesize a plain-language directional research brief with confidence, catalysts, risks, and invalidation points. The output is research only and does not provide financial advice or execute orders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend the user's USDC for paid data reads.

Mitigation: Run the quoted dry run first, show the live total cost, require user approval before wallet setup or execution, and keep wallet funding limited to the intended spend.

Risk: The research brief could be mistaken for financial advice or an instruction to trade.

Mitigation: Present outputs as non-advisory research only and decline requests to place orders or trade based on the result.

Risk: Wallet misuse or credential exposure could put funds at risk.

Mitigation: Use the MetaMask Agent Wallet CLI for signatures and never ask for, paste, store, or handle private keys.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/selat-dev/skills/stock-signal)
- [SELAT MetaMask skill source](https://github.com/SELAT-AI/selat-metamask-skills/tree/main/skills/stock-direction-signals)
- [SELAT MetaMask skills repository](https://github.com/SELAT-AI/selat-metamask-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown research brief with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes paid-read cost reporting, confidence, catalysts, social and macro context, and invalidation risks.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
