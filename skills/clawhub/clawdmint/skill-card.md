## Description: <br>
Deploy NFT collections on Base. AI agents can deploy via API key or x402 USDC payment. Humans mint. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nrlartt](https://clawhub.ai/user/nrlartt) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and agent operators use Clawdmint to register agents, verify human ownership, and deploy ERC-721 NFT collections on Base through API-key or x402 USDC payment flows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: NFT deployments and x402 requests can create real financial obligations or public blockchain transactions. <br>
Mitigation: Require explicit approval before deployments or paid requests, and use a dedicated low-balance wallet for x402 activity. <br>
Risk: Leaked Clawdmint API keys could allow unauthorized actions against the account. <br>
Mitigation: Keep CLAWDMINT_API_KEY private, send it only to https://clawdmint.xyz, and regenerate the key if it is compromised. <br>
Risk: Incorrect payout addresses, mint prices, or webhook destinations can route funds or notifications incorrectly. <br>
Mitigation: Verify payout addresses, mint prices, and webhook HTTPS endpoints before allowing an agent to submit requests. <br>


## Reference(s): <br>
- [Clawdmint skill page](https://clawhub.ai/nrlartt/skills/clawdmint) <br>
- [Clawdmint website](https://clawdmint.xyz) <br>
- [Clawdmint API base](https://clawdmint.xyz/api/v1) <br>
- [x402 pricing](https://clawdmint.xyz/api/x402/pricing) <br>
- [Published skill document](https://clawdmint.xyz/skill.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with curl commands, JSON examples, TypeScript snippets, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides registration, verification, collection deployment, webhook setup, and x402 payment requests for Base NFT collections.] <br>

## Skill Version(s): <br>
1.2.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
