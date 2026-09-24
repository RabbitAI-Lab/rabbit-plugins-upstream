## Description:

x402 Compute helps agents and developers provision and manage Singularity Cloud Network compute, GPU/VPS instances, private OpenAI-compatible LLM endpoints, decentralized inference, agent pods, processors, datasets, and encrypted agent backups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivaavimusic](https://clawhub.ai/user/ivaavimusic)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents use this skill to browse plans, provision or manage paid compute, deploy private LLM endpoints or hosted agent pods, run grid inference, publish paid processors, buy datasets, and back up or migrate agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide wallet-backed payments and paid compute provisioning.

Mitigation: Use dedicated low-balance wallets, scoped revocable API keys, and review payment amounts before allowing an agent to proceed.

Risk: The skill can guide cloud infrastructure changes, including resize, extension, and destruction of instances.

Mitigation: Review commands before execution, avoid automatic confirmation flags for destructive actions, and confirm target instance IDs.

Risk: The skill references remote installers, persistent services, and agent backup flows.

Mitigation: Review remote installation commands before running them and enable background services or backup daemons only after confirming what they will execute or upload.

## Reference(s):

- [x402 Compute Skill](https://clawhub.ai/ivaavimusic/skills/x402-compute)
- [x402 Compute Documentation](https://docs.x402layer.cc/agentic-access/x402-compute)
- [Cloud Network App](https://cloud.x402compute.cc)
- [x402Compute API Reference](references/api-reference.md)
- [AI Machines](references/ai-machines.md)
- [Agent Pods](references/agent-pods.md)
- [Agent Pods API](references/agent-pods-api.md)
- [SGL Processors](references/processors.md)
- [SGL Grid - Provide Compute](references/node-operator.md)
- [SGL Grid - Laya / System One](references/systemone-laya.md)
- [Datasets](references/datasets.md)
- [Agent Vault](references/agent-vault.md)
- [OpenWallet / OWS](references/openwallet-ows.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown with inline shell commands, Python script invocations, API examples, and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents through paid compute actions, wallet-backed payments, hosted services, and backup operations that require user review before execution.]

## Skill Version(s):

1.30.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
