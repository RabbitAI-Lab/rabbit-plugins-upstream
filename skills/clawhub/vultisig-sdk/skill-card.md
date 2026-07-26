## Description: <br>
Helps agents use the Vultisig SDK to create self-custodial MPC vaults, check balances, send transactions, and perform token swaps across supported blockchains. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[realpaaao](https://clawhub.ai/user/realpaaao) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and agent operators use this skill to integrate Vultisig SDK workflows for wallet creation, balance checks, token sends, swaps, and vault backup or import operations across supported chains. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents can move real cryptocurrency without mandatory human approval. <br>
Mitigation: Start with a new low-value vault and require Secure Vault or explicit per-transaction approval for sends, swaps, approvals, exports, seed imports, and vault deletion. <br>
Risk: Vault backups, passwords, imported seedphrases, and package supply chain changes can expose funds. <br>
Mitigation: Avoid importing existing seedphrases, protect vault backups and passwords, and verify or pin the SDK package before using it with real funds. <br>
Risk: Unbounded transfers or swaps can create financial loss through wrong recipients, approvals, slippage, or decimal mistakes. <br>
Mitigation: Use spend limits and recipient allowlists where possible, verify addresses and quote warnings, and check token decimals before broadcasting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/realpaaao/skills/vultisig-sdk) <br>
- [Vultisig SDK repository](https://github.com/vultisig/vultisig-sdk) <br>
- [SDK Users Guide](https://github.com/vultisig/vultisig-sdk/blob/main/docs/SDK-USERS-GUIDE.md) <br>
- [Vultisig Security & Technology](https://docs.vultisig.com/security-and-technology/security-technology) <br>
- [Fast Vault documentation](https://docs.vultisig.com/infrastructure/what-is-vultisigner/how-does-vultisigner-work) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with TypeScript and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes wallet and transaction examples that can affect real cryptocurrency when executed.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
