## Description:

x402 Compute helps agents provision and manage Singularity Cloud Network compute, GPU and AI machines, grid inference, node operation, Agent Pods, processors, datasets, and encrypted agent backups using x402 payments, credits, or API keys.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivaavimusic](https://clawhub.ai/user/ivaavimusic)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agent builders use this skill to browse pricing and capacity, provision and manage paid compute resources, deploy OpenAI-compatible LLM endpoints, run or consume decentralized inference, and manage hosted agents or paid processors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend wallet funds for compute, inference, datasets, processors, and related services.

Mitigation: Use a dedicated low-balance wallet, set tight spend limits, and review any non-interactive payment flow before enabling it.

Risk: The skill can destroy compute resources or alter running instances and hosted agents.

Mitigation: Confirm target instance or pod IDs before lifecycle actions, and avoid confirmation-skipping flags unless deliberate automation is required.

Risk: The skill may install remote node software for grid operation.

Mitigation: Verify the installer and pin dependencies in the execution environment before running node setup.

Risk: The skill handles API keys, wallet signing keys, pod integration keys, chat tokens, backup passphrases, and one-time passwords.

Mitigation: Treat all generated credentials and secrets as sensitive, store them securely, rotate or revoke them when no longer needed, and avoid exposing them in logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ivaavimusic/skills/x402-compute)
- [x402 Compute documentation](https://docs.x402layer.cc/agentic-access/x402-compute)
- [Cloud Network app](https://cloud.x402compute.cc)
- [x402Compute API Reference](references/api-reference.md)
- [AI Machines](references/ai-machines.md)
- [Agent Pods](references/agent-pods.md)
- [SGL Grid Node Operator](references/node-operator.md)
- [SGL Processors](references/processors.md)
- [Datasets](references/datasets.md)
- [Agent Vault](references/agent-vault.md)
- [OpenWallet / OWS](references/openwallet-ows.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline Python, shell commands, JSON examples, and API request snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API calls, environment variables, and generated credentials that should be handled as secrets.]

## Skill Version(s):

1.23.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
