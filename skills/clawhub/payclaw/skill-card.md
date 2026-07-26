## Description: <br>
Agent-to-Agent USDC payments. Create wallets, send/receive payments, escrow between agents. Built for the USDC Hackathon on Moltbook. <br>

This skill is for demonstration purposes and not for production usage. <br>

## Publisher: <br>
[rojasjuniore](https://clawhub.ai/user/rojasjuniore) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
OpenClaw developers and agent operators use Payclaw to create testnet USDC wallets, request or send payments, and model escrow-style agent-to-agent payment workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Payment and escrow commands may affect testnet wallet balances or create misleading escrow expectations. <br>
Mitigation: Use only low-risk Circle testnet API keys, verify every recipient, amount, and release action manually, and do not treat local escrow state as real escrow. <br>
Risk: The security scan reports unsafe command execution and recommends avoiding untrusted names, addresses, amounts, memos, or API keys until validation is fixed. <br>
Mitigation: Install only in a trusted test environment and pass only trusted, reviewed values to commands. <br>


## Reference(s): <br>
- [Payclaw homepage](https://github.com/rojasjuniore/payclaw) <br>
- [Payclaw on ClawHub](https://clawhub.ai/rojasjuniore/skills/payclaw) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, code, guidance] <br>
**Output Format:** [Markdown documentation with CLI examples and TypeScript integration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Circle testnet API key and manual review of wallet, payment, and escrow actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release, SKILL.md frontmatter, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
