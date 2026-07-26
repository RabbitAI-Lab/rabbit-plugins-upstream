## Description: <br>
Manage Sequence smart wallets, projects, API keys, ERC20 transfers, and query blockchain data using the Sequence Builder CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jameslawton](https://clawhub.ai/user/jameslawton) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to manage Sequence smart wallets, projects, API keys, ERC20 token transfers, and EVM blockchain queries from an agent-assisted command-line workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to create or use wallet private keys and send ERC20 transfers. <br>
Mitigation: Use test wallets and minimal funds first, avoid sharing private keys in chat or command lines where possible, and require human confirmation before any transfer. <br>
Risk: Encrypted local wallet configuration may expose funds if the passphrase or ~/.sequence-builder/config.json is mishandled. <br>
Mitigation: Protect the passphrase and local Sequence Builder configuration file, and install only when wallet or project management authority is intended. <br>


## Reference(s): <br>
- [Sequence Builder CLI repository](https://github.com/0xsequence/builder-cli) <br>
- [Sequence network status and supported chains](https://status.sequence.info/) <br>
- [ClawHub skill page](https://clawhub.ai/jameslawton/skills/sequence-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands generally request machine-readable JSON output with --json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
