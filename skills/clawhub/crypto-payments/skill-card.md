## Description: <br>
Creates Shieldz crypto payment links or reusable tip jars for user-provided wallets, and checks payment status after explicit user confirmation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shieldz](https://clawhub.ai/user/shieldz) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to create non-custodial Shieldz payment links or tip jars for a wallet they provide, then check received payment status. It is intended only for explicit payment-link or tip-jar requests where the wallet, chain, asset, amount, memo, and email choice are confirmed before any external call. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends wallet addresses, chains, assets, amounts, memos or titles, optional email addresses, and manage tokens to Shieldz. <br>
Mitigation: Disclose the data transfer before use and proceed only after the user confirms the exact wallet, chain, asset, amount, memo or title, and email choice. <br>
Risk: Manage URLs and manage tokens can expose account totals and settings if shared. <br>
Mitigation: Treat manage URLs and manage tokens like passwords; do not post them publicly, paste them into shared contexts, or write them to logs. <br>
Risk: A mistaken wallet, chain, asset, amount, or memo could create an incorrect payment link or tip jar. <br>
Mitigation: Never create links from vague intent, never batch-create autonomously, and require an explicit yes after restating all payment details. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shieldz/skills/crypto-payments) <br>
- [Shieldz REST payment link endpoint](https://shieldz.cash/api/v1/links) <br>
- [Shieldz REST tip jar endpoint](https://shieldz.cash/api/v1/tip-jars) <br>
- [Shieldz MCP server](https://shieldz.cash/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, API Calls] <br>
**Output Format:** [Markdown with inline bash commands and payment-status summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include public payment URLs; manage URLs and manage tokens are private credentials and should not be logged or shared.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
