## Description: <br>
Fetch a paywalled (HTTP 402) URL and pay for it automatically from the agent wallet's Kamino vault yield, without spending the principal. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yukikm](https://clawhub.ai/user/yukikm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to access Subly or x402 paywalled resources, settle eligible Solana USDC payment challenges from spendable vault yield, and guide the human owner through vault deposits, withdrawals, setup, and approval flows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can initiate real payments or vault movements when pointed at a configured wallet. <br>
Mitigation: Keep the configured per-payment cap in place, require user confirmation before raising caps or retrying uncertain payments, and use owner approval flows for higher-impact actions. <br>
Risk: The agent wallet keypair path grants access to sensitive signing material if mishandled. <br>
Mitigation: Never read, print, paste, or transmit the keypair file contents; only use the path for local commands and share public receipts. <br>
Risk: Deposited principal is exposed to DeFi vault risk even though payments are intended to spend only accrued yield. <br>
Mitigation: Explain deposit and withdrawal effects to the user, require the human owner's approval for deposits, and avoid making deposits without explicit consent. <br>


## Reference(s): <br>
- [Subly payment protocol](https://github.com/SublyFi/subly-payment-protocol) <br>
- [ClawHub skill page](https://clawhub.ai/yukikm/skills/subly-pay) <br>
- [Publisher profile](https://clawhub.ai/user/yukikm) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON result interpretation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include setup or approval URLs, retry commands, payment receipt details, and guidance for handling refused payments.] <br>

## Skill Version(s): <br>
0.2.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
