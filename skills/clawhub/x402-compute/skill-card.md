## Description:

x402 Compute helps agents manage Singularity Cloud Network compute, including GPU/VPS provisioning, AI machines, confidential grid inference, grid node operation, hosted agent pods, and paid processor endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivaavimusic](https://clawhub.ai/user/ivaavimusic)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to browse, provision, manage, resize, extend, and destroy compute resources; run OpenAI-compatible inference; deploy hosted agent pods; and publish paid processor endpoints. It is intended for workflows where an agent may need wallet-backed payment, compute API-key management, or shell/API guidance for Singularity Cloud Network services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use wallet credentials and compute API keys to spend funds.

Mitigation: Use dedicated low-balance wallets and scoped API keys, avoid primary custody wallets, and review every paid action before execution.

Risk: The skill can delete, resize, or otherwise change compute resources.

Mitigation: Confirm resource identifiers, backups, and intended lifecycle changes before running destructive or irreversible commands.

Risk: Processor payments are final and failed paid runs may not be refundable.

Mitigation: Read processor reliability signals before paying and retry failed paid runs by re-sending the same X-Payment header when supported.

Risk: The node-operator workflow can install long-running node software through a curl-to-shell installer.

Mitigation: Independently verify the installer source and service trust before running it, and use an isolated machine for node operation.

Risk: Unpinned or drifting dependencies can change wallet, payment, or provisioning behavior.

Mitigation: Pin or lock dependencies before use and review dependency changes before running payment or management workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ivaavimusic/skills/x402-compute)
- [x402 Compute documentation](https://docs.x402layer.cc/agentic-access/x402-compute)
- [x402 Compute cloud app](https://cloud.x402compute.cc)
- [API reference](references/api-reference.md)
- [AI Machines](references/ai-machines.md)
- [Agent Pods](references/agent-pods.md)
- [Node Operator](references/node-operator.md)
- [OpenWallet / OWS](references/openwallet-ows.md)
- [Processors](references/processors.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON request examples, and Python script invocations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include payment, wallet credential, compute lifecycle, and API-key handling steps.]

## Skill Version(s):

1.16.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
