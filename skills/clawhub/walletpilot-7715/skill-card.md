## Description: <br>
Execute on-chain transactions with user-granted permissions. Built on MetaMask ERC-7715. No private keys, full guardrails. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[andreolf](https://clawhub.ai/user/andreolf) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to help agents request scoped wallet permissions and prepare WalletPilot SDK-based flows for transactions, balance checks, swaps, token transfers, and transaction history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents may perform real crypto transactions within permissions granted by the user. <br>
Mitigation: Use small spend limits, short expirations, strict chain and contract allowlists, and revoke permissions when finished. <br>
Risk: Incorrect recipients, calldata, dependencies, or API key handling can cause financial loss or account exposure. <br>
Mitigation: Verify recipients and calldata before execution, protect the WalletPilot API key, and pin and review the SDK dependency. <br>


## Reference(s): <br>
- [WalletPilot Documentation](https://docs.walletpilot.xyz) <br>
- [WalletPilot API Reference](https://api.walletpilot.xyz) <br>
- [WalletPilot Website](https://walletpilot.xyz) <br>
- [ClawHub Skill Page](https://clawhub.ai/andreolf/skills/walletpilot-7715) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with TypeScript code blocks and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance can include wallet permission scopes, SDK setup, API calls, and transaction-preparation examples.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
