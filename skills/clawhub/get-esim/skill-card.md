## Description: <br>
Purchase travel eSIM data plans using USDC on Base Mainnet or Base Sepolia through x402, then deliver an eSIM installation page. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[inthaiguy](https://clawhub.ai/user/inthaiguy) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agent developers use this skill to search travel eSIM packages, quote a selected plan, coordinate USDC payment on Base, and return the eSIM installation link. It supports production purchases on Base Mainnet and mock testing on Base Sepolia. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Production purchases on Base Mainnet can spend real USDC and gas. <br>
Mitigation: Before approving payment, confirm mainnet versus testnet, selected package, USDC amount, token contract, recipient address from the 402 response, and gas cost. <br>
Risk: Testing against the production path can create a real eSIM purchase. <br>
Mitigation: Use Base Sepolia or a limited-balance wallet for testing and explicitly select testnet when a mock eSIM is intended. <br>
Risk: API rate limits can interrupt package search, quote, or purchase completion. <br>
Mitigation: Respect HTTP 429 responses and wait for the Retry-After interval before retrying. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/inthaiguy/skills/get-esim) <br>
- [Mainnet API Documentation](https://esimqr.link/api/agent/docs) <br>
- [Testnet API Documentation](https://esimqr.link/api/agent-testnet/docs) <br>
- [eSIM Agent Landing Page](https://esimqr.link/agents) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown instructions with JSON examples and Python helper code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes package search, quote, x402 payment, network selection, rate-limit handling, and eSIM delivery guidance.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
