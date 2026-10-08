## Description:

Helps agents provision and manage cloud compute, run grid inference and embeddings, deploy hosted agents and paid endpoints, and back up agent data through x402 Compute.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivaavimusic](https://clawhub.ai/user/ivaavimusic)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to deploy and manage GPU or VPS instances, access AI inference and embeddings, operate grid nodes, host agent pods and paid processors, and back up agents. Some operations involve payments or changes to live infrastructure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud provisioning, extensions, and inference can incur charges; resource deletion can be irreversible.

Mitigation: Review costs and approve paid or destructive commands before execution.

Risk: Wallet access or broad API credentials can expose funds and infrastructure.

Mitigation: Use a dedicated low-balance wallet and tightly scoped API keys; review credential rotation and fund transfers.

Risk: Installers, persistent services, and agent backups can change local systems or capture sensitive agent data.

Mitigation: Review installation, service startup, and backup commands and their destinations before running them.

## Reference(s):

- [x402 Compute documentation](https://docs.x402layer.cc/agentic-access/x402-compute)
- [x402 Compute Cloud Network](https://cloud.x402compute.cc)
- [API reference](artifact/references/api-reference.md)
- [Multimodal embeddings](artifact/references/multimodal-embeddings.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, JSON]

**Output Format:** [Markdown with commands and API examples; API responses may be JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide endpoints, resource details, and payment or deployment instructions.]

## Skill Version(s):

1.31.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
