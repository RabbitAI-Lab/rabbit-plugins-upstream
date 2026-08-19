## Description:

x402 Compute helps agents provision and manage Singularity Cloud Network compute, deploy private or grid LLM endpoints, use grid inference, manage hosted Agent Pods, publish paid processors, and back up or restore agent state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivaavimusic](https://clawhub.ai/user/ivaavimusic)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent browse compute plans, provision or manage paid GPU and VPS instances, deploy OpenAI-compatible inference endpoints, operate grid nodes, manage hosted agent pods, publish paid processor endpoints, and perform encrypted agent backup or restore.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend funds through x402, credits, MPP, provisioning, extension, grid usage, processors, or hosted agent pods.

Mitigation: Use dedicated low-balance wallets, review every network, target, price, duration, and cost before payment, and avoid using primary custody wallets.

Risk: The skill can manage or delete servers and hosted agents.

Mitigation: Review instance and pod identifiers before resize, restore, extension, lifecycle actions, or deletion; prefer SSH keys over root-password fallback.

Risk: The skill can create persistent API keys, hosted agents, pod wallets, and encrypted backups of private agent state.

Mitigation: Store one-time keys and backup passphrases securely, revoke API keys when finished, and disable pod wallet sending when it is not needed.

Risk: The skill includes flows that can run a remote installer for grid node software.

Mitigation: Avoid curl-pipe-shell installation unless the source and command are trusted and verified.

## Reference(s):

- [x402 Compute ClawHub Page](https://clawhub.ai/ivaavimusic/skills/x402-compute)
- [x402 Compute Documentation](https://docs.x402layer.cc/agentic-access/x402-compute)
- [Cloud Network App](https://cloud.x402compute.cc)
- [x402Compute API Reference](references/api-reference.md)
- [AI Machines](references/ai-machines.md)
- [Agent Pods](references/agent-pods.md)
- [SGL Grid Node Operator](references/node-operator.md)
- [SGL Processors](references/processors.md)
- [Agent Vault](references/agent-vault.md)
- [OpenWallet / OWS](references/openwallet-ows.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, Python command examples, API request examples, and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce commands or API calls that use wallet keys, API keys, paid compute resources, hosted agents, backups, or node services.]

## Skill Version(s):

1.19.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
