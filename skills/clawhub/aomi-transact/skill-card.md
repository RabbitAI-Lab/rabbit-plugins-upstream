## Description: <br>
Transact helps agents use the Aomi CLI to turn natural-language crypto and DeFi requests into reviewed, simulated, wallet-signed transactions across supported EVM and Solana flows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ceciliaz030](https://clawhub.ai/user/ceciliaz030) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agent users use this skill to inspect balances and quotes, build wallet requests, simulate transaction batches, and sign approved crypto or DeFi transactions through the Aomi CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can prepare and sign high-impact crypto transactions. <br>
Mitigation: Use a test wallet first, inspect every queued transaction, simulate multi-step batches, and sign only transactions the user explicitly approved. <br>
Risk: Private keys, seed phrases, RPC URLs, backend URLs, or account bearer tokens may expose funds or accounts if mishandled. <br>
Mitigation: Do not paste production seed phrases, do not echo credential values, and only approve custom RPC or backend URLs that the operator trusts. <br>
Risk: The on-demand npm path can run the latest Aomi CLI version and may change behavior over time. <br>
Mitigation: For stricter environments, install or pin a reviewed CLI version and restrict npx, backend, and RPC network access externally. <br>


## Reference(s): <br>
- [Source repository](https://github.com/aomi-labs/skills/tree/main/aomi-transact) <br>
- [Aomi CLI npm package](https://www.npmjs.com/package/@aomi-labs/client) <br>
- [Command Reference](references/commands.md) <br>
- [Workflows](references/workflows.md) <br>
- [Gotchas, Hard Rules, and Security Model](references/gotchas.md) <br>
- [Account Abstraction Reference](references/account-abstraction.md) <br>
- [Apps Reference](references/apps.md) <br>
- [Flow Examples](references/examples.md) <br>
- [Thread Reference](references/thread.md) <br>
- [Drain Vectors](references/drain-vectors.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash commands and command-output interpretation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May stage transaction instructions for explicit user review, simulation, and signing through the Aomi CLI; does not require the agent to echo private keys or seed phrases.] <br>

## Skill Version(s): <br>
0.10.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
