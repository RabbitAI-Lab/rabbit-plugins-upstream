## Description: <br>
Safe Skills helps agents create and manage EVM wallets, check balances, transfer tokens, and submit transactions while keeping raw secret values server-side. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[glitch003](https://clawhub.ai/user/glitch003) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use Safe Skills to provision EVM wallets and perform wallet operations through API calls without exposing private keys to the agent. The skill is suited to workflows that need balances, transfers, or smart-contract transactions mediated by a server-side secret manager. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet transfers and arbitrary smart-contract transactions can move funds or create irreversible blockchain effects. <br>
Mitigation: Use testnet or very small amounts first, and require explicit user confirmation for every transfer or transaction after checking recipient, amount, token, calldata, and value. <br>
Risk: The API key authorizes future wallet operations and may be exposed through chat history, logs, or insecure storage. <br>
Mitigation: Keep the API key out of chat and logs, store it securely, and replace the wallet credential if exposure is suspected. <br>
Risk: Users rely on the SafeSkills provider and claim URL controls to enforce wallet policies and monitor activity. <br>
Mitigation: Verify the provider and claim URL before funding a wallet, and review policy controls before approving funded transactions. <br>


## Reference(s): <br>
- [Safe Skills on ClawHub](https://clawhub.ai/glitch003/skills/safe-skills) <br>
- [SafeSkills Service Endpoint](https://safeskill-production.up.railway.app) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration] <br>
**Output Format:** [Markdown guidance with curl commands and JSON request bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a bearer API key returned by the SafeSkills service; wallet actions can move funds or submit smart-contract transactions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
