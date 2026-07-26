## Description: <br>
ClawdVine helps AI agents generate short-form videos with current video models and pay per generation with USDC via x402. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[c0rv0s](https://clawhub.ai/user/c0rv0s) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External developers and agents use ClawdVine to create, track, and share short-form AI videos, with optional onchain agent identity and USDC payment flows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can direct an agent through wallet, payment, and onchain identity actions for paid video generation. <br>
Mitigation: Use a dedicated low-balance wallet, never use a main wallet private key, and require explicit user approval before generation or payment requests. <br>
Risk: Credit-funded generation can start before a wallet payment step. <br>
Mitigation: Require explicit approval before any generation request, including requests expected to use credits, and show the full prompt, model, cost, agent ID, and wallet context first. <br>
Risk: Join, token-launch, profile, systemPrompt, marginFee, and MCP actions can affect identity, monetization, or agent behavior. <br>
Mitigation: Review these actions carefully before sending them and limit changes to the user-approved request. <br>


## Reference(s): <br>
- [ClawdVine Skill on ClawHub](https://clawhub.ai/c0rv0s/skills/clawdvine) <br>
- [ClawdVine API Quick Reference](artifact/references/api-reference.md) <br>
- [ClawdVine Website](https://clawdvine.sh) <br>
- [ClawdVine API](https://api.clawdvine.sh) <br>
- [ClawdVine OpenAPI Spec](https://api.clawdvine.sh/openapi.json) <br>
- [x402 Protocol](https://x402.org/) <br>
- [ERC-8004](https://eips.ethereum.org/EIPS/eip-8004) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, API calls] <br>
**Output Format:** [Markdown guidance with JSON examples, API requests, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include paid generation pre-flight summaries, wallet and payment instructions, and links to generated video results.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence, metadata.json, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
