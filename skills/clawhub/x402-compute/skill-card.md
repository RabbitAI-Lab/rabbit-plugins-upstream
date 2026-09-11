## Description:

x402 Compute helps agents manage Singularity Cloud Network compute, including GPU/VPS provisioning, OpenAI-compatible inference, hosted agent pods, paid processors, synthetic datasets, and encrypted agent backups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivaavimusic](https://clawhub.ai/user/ivaavimusic)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, infrastructure operators, and agent builders use this skill to let agents browse pricing, provision and manage paid compute, deploy private or grid-connected LLM endpoints, operate hosted agents, publish paid processors, buy JSONL training datasets, and back up or restore agent state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents can operate funded wallets and paid compute workflows, which may spend funds or create infrastructure.

Mitigation: Use dedicated low-balance wallets, keep spend limits in place, and require explicit approval before provisioning, extending, staking, or topping up credits.

Risk: The skill handles sensitive API keys, wallet keys, one-time passwords, integration keys, and backup passphrases.

Mitigation: Prefer scoped and revocable API keys, export secrets only in the active process environment, avoid command-line secret arguments, store one-time credentials securely, and never log backup passphrases.

Risk: Destroy, restore, delete, credential-rotation, daemon, and service-install actions can be destructive or persistent.

Mitigation: Require human confirmation for destructive and persistent-service actions, review target identifiers before execution, and keep recoverable backups before restore or delete operations.

Risk: External installers and dependencies can introduce supply-chain risk.

Mitigation: Inspect or replace curl-to-shell installers, pin dependencies where possible, install OWS explicitly, and use an absolute trusted OWS_BIN path for wallet operations.

Risk: Processor write credentials can control processor code, secrets, token rotation, listings, and deletion.

Mitigation: Mint read-only keys unless write access is required, revoke unused keys, keep processor write keys narrowly distributed, and pause processors instead of deleting them when possible.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ivaavimusic/skills/x402-compute)
- [x402 Compute Documentation](https://docs.x402layer.cc/agentic-access/x402-compute)
- [x402 Compute Cloud App](https://cloud.x402compute.cc)
- [Singularity Compute](https://x402compute.cc)
- [Staking](https://staking.x402layer.cc)
- [API Reference](references/api-reference.md)
- [AI Machines](references/ai-machines.md)
- [Agent Pods](references/agent-pods.md)
- [Processors](references/processors.md)
- [Agent Vault](references/agent-vault.md)
- [Datasets](references/datasets.md)
- [Node Operator](references/node-operator.md)
- [OpenWallet / OWS](references/openwallet-ows.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python commands, shell commands, curl examples, JSON request and response patterns, and environment variable setup.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May print instance metadata, payment prompts, API keys or one-time credentials returned by services, endpoint URLs, transaction hashes, and operational error messages.]

## Skill Version(s):

1.26.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
