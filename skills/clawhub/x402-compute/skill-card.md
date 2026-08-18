## Description:

x402 Compute helps agents provision and manage paid GPU/VPS instances, OpenAI-compatible inference endpoints, grid nodes, hosted agent pods, processors, and encrypted agent backups across Singularity Cloud Network.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivaavimusic](https://clawhub.ai/user/ivaavimusic)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent browse compute plans, provision and manage paid cloud instances and LLM endpoints, operate grid/provider workflows, deploy hosted agent pods and processors, and manage encrypted agent backup or restore.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can manage paid compute resources and hosted agents.

Mitigation: Use a dedicated low-balance wallet, set a strict spend cap, and require explicit confirmation before provision, extend, resize, auto-renew, or wallet-send actions.

Risk: The skill can perform destructive or state-changing actions such as delete, revoke, restore, destroy, and resize.

Mitigation: Confirm the target resource, cost, and recovery plan before each destructive or irreversible action.

Risk: The skill depends on wallet keys, signing keys, and API keys for management and payment flows.

Mitigation: Keep primary custody wallets out of the environment, prefer scoped or revocable credentials, and avoid exposing sensitive values in logs or prompts.

Risk: Some workflows use external installers or package downloads.

Mitigation: Pin or lock dependencies before use and inspect remote installers before running them.

## Reference(s):

- [x402 Compute documentation](https://docs.x402layer.cc/agentic-access/x402-compute)
- [x402 Compute ClawHub page](https://clawhub.ai/ivaavimusic/skills/x402-compute)
- [Cloud Network app](https://cloud.x402compute.cc)
- [API Reference](references/api-reference.md)
- [AI Machines](references/ai-machines.md)
- [Agent Pods](references/agent-pods.md)
- [Agent Vault](references/agent-vault.md)
- [Processors](references/processors.md)
- [Node Operator](references/node-operator.md)
- [OpenWallet OWS](references/openwallet-ows.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration values, API examples, and script invocation instructions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents through paid compute, wallet signing, API-key management, hosted agent, processor, and backup/restore workflows.]

## Skill Version(s):

1.18.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
