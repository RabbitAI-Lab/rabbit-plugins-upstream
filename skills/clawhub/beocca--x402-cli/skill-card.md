## Description: <br>
A simple CLI that helps AI agents discover x402 services, make paywalled requests, and manage local EVM wallets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[beocca](https://clawhub.ai/user/beocca) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to list and search x402 services, create local EVM wallets, and make paywalled HTTP requests through an agent-accessible CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can use a spend-capable EVM wallet to authorize paid x402 requests. <br>
Mitigation: Use a dedicated low-balance or ephemeral wallet, avoid primary wallet keys, and apply external spending limits where available. <br>
Risk: The request command performs paid requests immediately without a built-in confirmation prompt or spending cap. <br>
Mitigation: Review the destination URL, headers, payload, and expected payment before execution, and route commands through a human or policy approval layer when needed. <br>
Risk: Wallet creation writes a plaintext private key file to disk. <br>
Mitigation: Keep wallet files out of version control and shared storage, preserve owner-only permissions, and fund wallets only with the minimum operational balance. <br>


## Reference(s): <br>
- [x402 homepage](https://www.x402.org) <br>
- [ClawHub skill page](https://clawhub.ai/beocca/skills/x402-cli) <br>
- [AgNet OpenAPI](https://api.agnet.world/openapi.json) <br>
- [AgMsg OpenAPI](https://api.agmsg.world/openapi.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [CLI text and JSON responses, with Markdown usage guidance and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Discovery commands can optionally save JSON files; wallet creation can write a plaintext wallet JSON file with owner-only permissions.] <br>

## Skill Version(s): <br>
1.0.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
