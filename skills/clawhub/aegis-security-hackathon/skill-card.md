## Description: <br>
Blockchain security scanner for AI agents on testnet that uses Base Sepolia USDC payments via the x402 protocol. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[swiftadviser](https://clawhub.ai/user/swiftadviser) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External developers and AI-agent builders use this skill to check token, address, and transaction risk through the Aegis402 testnet API before swaps or transaction signing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using the skill sends token, wallet address, or transaction details to the Aegis402 external service. <br>
Mitigation: Submit only data appropriate for that provider and review its privacy and retention practices before using sensitive or production trading workflows. <br>
Risk: Paid endpoints can consume Base Sepolia testnet USDC through the x402 payment flow. <br>
Mitigation: Use a dedicated low-value testnet wallet and confirm payment behavior before integrating the endpoints into automated agents. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/swiftadviser/skills/aegis-security-hackathon) <br>
- [Hackathon API](https://hackathon.aegis402.xyz/v1) <br>
- [Skill metadata](https://hackathon.aegis402.xyz/skill.json) <br>
- [x402 Protocol](https://docs.x402.org) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown instructions with bash and TypeScript examples; paid API responses are JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Paid x402 endpoints require Base Sepolia testnet USDC and return token, address, or transaction risk fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, package.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
