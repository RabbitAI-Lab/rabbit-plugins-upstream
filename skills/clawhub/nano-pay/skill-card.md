## Description: <br>
nano-pay helps agents pay x402-priced HTTP APIs with feeless Nano (XNO) micropayments from a self-custodied local wallet and manage quote, pay, receive, send, top-up, and server-side payment commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[glennquinting](https://clawhub.ai/user/glennquinting) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and agents use nano-pay to quote and execute Nano-backed x402 payments for paid HTTP endpoints, compare payer cost across rails, and manage small self-custodied working balances. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Payment, send, and top-up execution commands can move or commit real Nano funds. <br>
Mitigation: Run quote and status commands before paying, keep only small working funds in the wallet, and rely on max-xno limits for paid requests. <br>
Risk: The local self-custodied wallet contains sensitive seed material. <br>
Mitigation: Protect ~/.nano-pay/wallet.json, do not commit or transmit it, and avoid printing or pasting the seed. <br>
Risk: Payments are irreversible and failed HTTP responses may not prove whether a payment settled. <br>
Mitigation: Use nano-pay status as the balance ground truth after attempted payments and top up only with small intended amounts. <br>


## Reference(s): <br>
- [Feeless402 homepage](https://feeless402.com) <br>
- [nano-gpt x402 API endpoint](https://nano-gpt.com/api/v1/chat/completions) <br>
- [x402nano facilitator](https://www.x402nano.org/) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON command output expectations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands are expected to print JSON; pay, send, and topup --execute can move or commit funds.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
