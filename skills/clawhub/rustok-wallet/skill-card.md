## Description: <br>
Self-custody Ethereum agent wallet that runs locally as a Docker or Podman image, keeps private keys on the user's machine, reads wallet context, balances and DeFi positions, previews and executes sends, and signs plain messages and EIP-712 typed data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[temrjan](https://clawhub.ai/user/temrjan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect an agent to a local self-custody Ethereum wallet for balance checks, DeFi position review, transaction previews, sends, and message or typed-data signing. It is intended for users who intentionally place funds under the wallet's control and accept the operational risk of autonomous signing and transaction execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill controls a self-custody Ethereum wallet and can affect funds intentionally placed in that wallet. <br>
Mitigation: Install only when comfortable giving the agent wallet authority over those funds, keep only intentional balances in the wallet, and review previews before execution. <br>
Risk: Typed-data signing can authorize approvals, permits, or off-chain orders that move funds. <br>
Mitigation: Treat EIP-712 typed-data signing with the same scrutiny as transaction execution and avoid signing payloads that are not fully understood. <br>
Risk: The HTTP gateway can be exposed beyond loopback if the operator opts into network exposure. <br>
Mitigation: Keep the gateway loopback-only unless network exposure is required, and use an API key and trusted callers when exposing it. <br>
Risk: RUSTOK_MCP_CAPABILITIES alone does not fully enforce reduced-capability deployments because typed-data signing is outside the advertised MCP capability limits. <br>
Mitigation: Do not rely on that environment variable as the only control for read-only or reduced-capability deployments; restrict gateway access and caller trust separately. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/temrjan/skills/rustok-wallet) <br>
- [Rustok project homepage](https://github.com/rustok-org/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, API Calls] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON configuration examples, wallet data, transaction previews, transaction hashes, and signatures] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Docker or Podman, a local wallet volume, an Ethereum RPC URL, and careful handling of wallet password and recovery phrase.] <br>

## Skill Version(s): <br>
0.4.8 (source: frontmatter, claw.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
