## Description: <br>
Openclaw Wallet provides multi-chain wallet, trading, market data, token launch, fee management, and RPC tools for AI agents on Solana and EVM chains. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[loomlay](https://clawhub.ai/user/loomlay) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external agent operators use this skill when an agent needs wallet setup, balance checks, swaps, transfers, bridges, DEX market research, token launch workflows, fee claims, or raw RPC calls across supported Solana and EVM chains. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent broad authority over crypto wallet operations, including swaps, transfers, bridges, token launches, fee claims, and raw RPC calls. <br>
Mitigation: Install it only for agents that intentionally need wallet authority, use a dedicated low-value wallet, and require explicit user approval before every financial or raw RPC action. <br>
Risk: The skill handles seed phrases, private-key export, API registration, and persistent credentials. <br>
Mitigation: Never log seed phrases or keys, require approval before wallet creation or key export, pin and review the npm package before use, and periodically remove or rotate credentials stored in ~/.loomlay/credentials.json. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/loomlay/skills/openclaw-wallet) <br>
- [Skill homepage listed in metadata](https://github.com/loomlay/openclaw-wallet) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with inline bash and JavaScript code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LOOMLAY_API_KEY; may also use LOOMLAY_BASE_URL.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
