## Description: <br>
Executes USDC payroll runs for employees and contractors on Base through the Spraay Protocol gateway, with roster validation, cost estimation, explicit user confirmation, and payment proof links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[plagtech](https://clawhub.ai/user/plagtech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Finance operators, founders, and payroll administrators use this skill to validate a roster, estimate fees, and execute a stablecoin payroll run in USDC on Base. It is for settlement execution, not employment compliance, tax withholding, KYC, W-2/1099 generation, or worker classification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Payroll execution can move funds and on-chain transfers are final. <br>
Mitigation: Validate the roster in the same session, show headcount, total amount, fees, and gas, and require explicit user confirmation before execution. <br>
Risk: Incorrect or malicious wallet changes can divert payroll. <br>
Mitigation: Review every recipient wallet and amount, confirm wallet changes with the user, and flag anomalies before including them in a run. <br>
Risk: Duplicate or abnormal roster entries can create incorrect payments. <br>
Mitigation: Use the validation endpoint, surface duplicate wallets and unusual amounts, and compare the total against the source payroll record. <br>
Risk: Treasury signing authority could be exposed if private keys or seed phrases are mishandled. <br>
Mitigation: Keep signing under the user's direct wallet control and never collect, store, or process private keys or seed phrases. <br>


## Reference(s): <br>
- [Spraay Protocol](https://spraay.app) <br>
- [Spraay Documentation](https://docs.spraay.app) <br>
- [Spraay Gateway](https://gateway.spraay.app) <br>
- [x402 Discovery](https://gateway.spraay.app/.well-known/x402.json) <br>
- [Spraay x402 MCP Server](https://smithery.ai/servers/Plagtech/Spraay-x402-mcp) <br>
- [ClawHub Skill Page](https://clawhub.ai/plagtech/skills/crypto-payroll) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, json, api calls] <br>
**Output Format:** [Markdown with endpoint references, JSON request bodies, validation summaries, confirmation prompts, and transaction links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit user confirmation before execution; successful execution returns a transaction hash that can be linked as payment proof.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
