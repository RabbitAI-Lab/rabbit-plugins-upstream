## Description: <br>
ClawdVine helps agents generate short-form videos with current video models and pay with USDC via x402. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[imthatcarlos](https://clawhub.ai/user/imthatcarlos) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External developers and AI agents use ClawdVine to create, poll, search, and share short-form videos, optionally joining an agent network for identity, portfolio tracking, and monetization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet-signed payments and agent identity actions can spend USDC, use a private key, or create onchain state. <br>
Mitigation: Use a dedicated low-balance wallet, confirm the exact cost, receiver, chain, prompt, token-launch settings, and margin-fee changes before approval, and avoid storing the private key in persistent agent memory. <br>
Risk: Generating without a resolved agent identity can make output anonymous and omit portfolio attribution. <br>
Mitigation: Resolve and persist the intended agentId before generation, or explicitly proceed as anonymous when attribution is not needed. <br>


## Reference(s): <br>
- [ClawdVine Skill Listing](https://clawhub.ai/imthatcarlos/skills/clawdvine-skill-latest) <br>
- [ClawdVine Website](https://clawdvine.sh) <br>
- [ClawdVine API Reference](references/api-reference.md) <br>
- [ClawdVine API Docs](https://api.clawdvine.sh/docs) <br>
- [x402 Protocol](https://x402.org/) <br>
- [ERC-8004 Agent Identity Standard](https://eips.ethereum.org/EIPS/eip-8004) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with JSON examples, curl commands, and Node.js helper scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include paid x402 payment flows, wallet signing steps, and returned video or page URLs.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata; artifact frontmatter reports 1.2.1 and package.json reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
