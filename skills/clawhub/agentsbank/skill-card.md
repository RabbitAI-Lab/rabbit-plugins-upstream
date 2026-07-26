## Description: <br>
AgentsBank provides a TypeScript/JavaScript SDK for AI agents to authenticate with AgentsBank, inspect multi-chain crypto wallets, estimate fees, sign messages, and submit wallet transactions through the AgentsBank API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cryruz](https://clawhub.ai/user/cryruz) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent builders use this skill to integrate AI agents with AgentsBank wallet APIs for balance checks, transaction history, fee estimation, message signing, wallet creation, and user-approved crypto transfers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The SDK exposes direct fund-transfer and batch-transfer APIs, and the security verdict flags the release as suspicious because no enforceable user approval gate is present in the scanned implementation. <br>
Mitigation: Review carefully before connecting funded wallets, start with testnet or low-limit credentials, and require a separate human approval step before send, sendSafe, signMessage, or sendMultiple calls. <br>
Risk: Gas and fee controls may be misunderstood because the security guidance says maxGasUSD is not an enforced fee cap in this version. <br>
Mitigation: Treat fee estimates as advisory, independently confirm final costs before transaction approval, and avoid relying on maxGasUSD as a hard spending limit. <br>
Risk: The release evidence and artifact files disagree on version numbers. <br>
Mitigation: Use the server-resolved release version for this card and confirm package provenance and version alignment before promoting the skill. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/cryruz/skills/agentsbank) <br>
- [AgentsBank SDK Documentation](https://docs.agentsbank.online/sdk) <br>
- [AgentsBank API Reference](https://api.agentsbank.online/docs) <br>
- [AgentsBank Security Guide](https://docs.agentsbank.online/security) <br>
- [npm Package](https://www.npmjs.com/package/@agentsbankai/sdk) <br>


## Skill Output: <br>
**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and TypeScript/JavaScript code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AgentsBank API credentials and environment configuration before wallet operations can run.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact package.json and changelog report 1.0.7, and src/index.ts exports 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
