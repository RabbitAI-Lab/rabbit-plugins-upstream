## Description:

x402 Compute helps agents browse, provision, manage, and retire Singularity Cloud Network compute resources, AI machines, grid inference, hosted agent pods, processors, datasets, and encrypted agent backups using x402 or API-key based workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivaavimusic](https://clawhub.ai/user/ivaavimusic)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill to manage GPU or VPS instances, deploy private OpenAI-compatible endpoints or hosted agents, run grid inference, publish paid processors, buy datasets, and back up or migrate agents. The skill is intended for workflows where an agent may propose or execute commands that affect cloud resources, wallet-backed payments, reusable management keys, hosted agents, and backups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can affect cloud resources, wallet-backed payments, reusable management keys, hosted agent deployment, and agent backups.

Mitigation: Review every provisioning, deletion, backup, restore, pod action, service-install command, and payment-bearing request before execution.

Risk: The skill uses sensitive wallet keys and management credentials for signing and API access.

Mitigation: Use a dedicated low-balance wallet, protect COMPUTE_API_KEY and signing keys, and avoid passing secrets on command lines.

Risk: The security evidence flags unsafe install and credential-handling patterns.

Mitigation: Prefer SSH keys over password fallback, avoid pipe-to-shell installation without independent verification, and pin dependencies in a controlled environment.

## Reference(s):

- [x402 Compute documentation](https://docs.x402layer.cc/agentic-access/x402-compute)
- [x402 Compute cloud app](https://cloud.x402compute.cc)
- [ClawHub skill listing](https://clawhub.ai/ivaavimusic/skills/x402-compute)
- [x402Compute API Reference](references/api-reference.md)
- [AI Machines - One-Click GPU Running an LLM](references/ai-machines.md)
- [Agent Pods - deploy and drive an always-on hosted agent](references/agent-pods.md)
- [SGL Grid - Provide Compute](references/node-operator.md)
- [SGL Processors](references/processors.md)
- [Datasets - buy fine-tuning data with a wallet](references/datasets.md)
- [Agent Vault - encrypted agent backup and migration](references/agent-vault.md)
- [OpenWallet / OWS for x402-compute](references/openwallet-ows.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, Python, curl, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands that call external compute, wallet, payment, processor, dataset, and backup services; review before execution.]

## Skill Version(s):

1.26.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
