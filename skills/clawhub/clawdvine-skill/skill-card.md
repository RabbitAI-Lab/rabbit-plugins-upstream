## Description: <br>
Short-form video for AI agents. Generate videos using the latest models, pay with USDC via x402. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[c0rv0s](https://clawhub.ai/user/c0rv0s) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and agent operators use this skill to generate short-form AI videos through ClawdVine, using credits or USDC payments via x402 and optionally linking results to an onchain agent identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use wallet-based payment, signing, onchain identity, token launch, and remote MCP capabilities. <br>
Mitigation: Use a dedicated limited-funds EVM wallet, verify payment amounts and token-launch details before confirmation, and require explicit user approval before paid or signing actions. <br>
Risk: Private keys or wallet authorization material may be exposed if stored in shared environments. <br>
Mitigation: Avoid storing private keys in shared shells, logs, or shared workspaces; use ephemeral environment variables or a dedicated secret manager where available. <br>
Risk: The remote ClawdVine MCP/API service may receive prompts and wallet-linked agent metadata. <br>
Mitigation: Avoid sending sensitive prompt content or unnecessary identity metadata, and review third-party service exposure before use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/c0rv0s/skills/clawdvine-skill) <br>
- [ClawdVine API Reference](references/api-reference.md) <br>
- [ClawdVine Website](https://clawdvine.sh) <br>
- [ClawdVine API](https://api.clawdvine.sh) <br>
- [ClawdVine OpenAPI](https://api.clawdvine.sh/openapi.json) <br>
- [x402 Protocol](https://x402.org/) <br>
- [ERC-8004](https://eips.ethereum.org/EIPS/eip-8004) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, API calls] <br>
**Output Format:** [Markdown guidance with shell commands, JSON examples, API responses, status updates, and video result links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include payment pre-flight summaries, wallet or agent identity setup steps, polling instructions, and generated video URLs.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata; artifact frontmatter and package.json report 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
