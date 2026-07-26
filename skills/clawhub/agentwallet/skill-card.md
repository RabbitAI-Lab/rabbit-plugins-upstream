## Description: <br>
The agent wallet enables EVM transactions, token swaps, smart contract interactions, balance checks, and raw message signing through the Vincent CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[glitch003](https://clawhub.ai/user/glitch003) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to let an agent create and manage a policy-constrained wallet for EVM transfers, token swaps, smart contract calls, balance checks, and raw signing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can enable real fund movement and signing before owner policies are configured. <br>
Mitigation: Claim any created wallet immediately, configure strict spending limits, address and token allowlists, and approval policies before funding it. <br>
Risk: Stored wallet credentials or re-link tokens could be misused within the permissions granted to the agent. <br>
Mitigation: Protect the configured credential directories, treat re-link tokens as secrets, and revoke or rotate credentials when access is no longer needed. <br>
Risk: The skill invokes the Vincent CLI package for wallet operations. <br>
Mitigation: Review or pin the @vincentai/cli version before use in sensitive environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/glitch003/skills/agentwallet) <br>
- [HeyVincent homepage](https://heyvincent.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with CLI command examples; CLI invocations return JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses configured agentwallet credential storage and the @vincentai/cli package for wallet operations.] <br>

## Skill Version(s): <br>
1.0.70 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
