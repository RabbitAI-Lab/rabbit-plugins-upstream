## Description: <br>
Use the Warden App through browser automation to inspect portfolios and positions, prepare crypto actions, and execute swaps, bridges, deposits, withdrawals, and perps only after explicit user approval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deiu](https://clawhub.ai/user/deiu) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to operate Warden App browser workflows for wallet review, balances, positions, swaps, bridge actions, deposits, withdrawals, and perp trading with explicit confirmation gates before transactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: High-impact crypto wallet automation can initiate transactions with financial loss if chain, token, amount, slippage, fees, or leverage are wrong. <br>
Mitigation: Verify those transaction details before execution and approve only when the user explicitly intends the transaction. <br>
Risk: Wallet credentials or seed phrases could be exposed if requested or stored during automation. <br>
Mitigation: Never request seed phrases or private keys, and keep wallet connection limited to the user's browser session. <br>
Risk: Users may mistake prepared actions or UI navigation for authorized execution. <br>
Mitigation: Default to read-only actions and require an explicit execution approval before clicking final confirmation controls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deiu/skills/warden-app) <br>
- [Warden App](https://app.wardenprotocol.org/) <br>
- [Warden UI notes](references/warden-ui-notes.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands] <br>
**Output Format:** [Markdown guidance with browser-automation checklists and confirmation steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided app access and explicit approval before final transaction execution.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
