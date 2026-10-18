## Description:

Helps agents provision and manage paid cloud compute, hosted agents, and endpoints, and use decentralized inference and encrypted agent backups through Singularity Cloud Network.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivaavimusic](https://clawhub.ai/user/ivaavimusic)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to discover, provision, and manage GPU or VPS instances, hosted agents, paid endpoints, inference, and agent backups, including wallet-signed payments and service credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet-signed payments and paid cloud resources can incur unintended charges.

Mitigation: Use dedicated low-balance wallets and confirm payments and auto-renewal before execution.

Risk: Instance deletion, credential rotation, and hosted-agent wallet sends can cause irreversible changes or loss of access.

Mitigation: Require manual confirmation for deletes, credential rotation, and wallet sends; use narrowly scoped API keys.

Risk: Background services and remote installation commands can change the local or hosted environment.

Mitigation: Review background-service setup and any curl-to-sh installer before running it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ivaavimusic/skills/x402-compute)
- [x402 Compute documentation](https://docs.x402layer.cc/agentic-access/x402-compute)
- [Singularity Cloud Network app](https://cloud.x402compute.cc)
- [Compute and Grid API reference](artifact/references/api-reference.md)
- [Agent Pods API reference](artifact/references/agent-pods-api.md)
- [Agent Vault guide](artifact/references/agent-vault.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with inline commands and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide paid API calls and changes to cloud or hosted-agent resources; actions require operator review.]

## Skill Version(s):

1.32.0 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
