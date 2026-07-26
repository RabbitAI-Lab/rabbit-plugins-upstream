## Description: <br>
Send and receive Bitcoin over Arkade (offchain), onchain (via onboard/offboard), and Lightning. Swap USDC/USDT stablecoins. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tiero](https://clawhub.ai/user/tiero) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to let agents work with Arkade Bitcoin wallets, Lightning invoices, onchain onboarding/offboarding, and BTC-to-USDC/USDT swaps through CLI commands or TypeScript SDK calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent direct authority over wallet sends, Lightning payments, offboards, and swaps. <br>
Mitigation: Treat it as a hot-wallet integration, keep only small balances available, and require explicit human approval for every value-moving action. <br>
Risk: Payment destinations, invoices, amounts, tokens, or networks may be wrong and crypto transfers can be difficult or impossible to reverse. <br>
Mitigation: Verify the address, invoice, amount, token, chain, network, fees, and limits out of band before execution. <br>
Risk: Wallet secrets may be exposed if live private keys are pasted into prompts or command lines. <br>
Mitigation: Use local wallet configuration and do not paste live private keys into prompts, chat history, scripts, or shell commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tiero/skills/arkade-wallet) <br>
- [Arkade documentation](https://docs.arkadeos.com) <br>
- [Arkade default server](https://arkade.computer) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and TypeScript code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include wallet addresses, balances, transaction status, swap quotes, and payment guidance when used by an agent.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
