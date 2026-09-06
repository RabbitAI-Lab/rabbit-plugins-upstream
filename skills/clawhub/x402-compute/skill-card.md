## Description:

x402 Compute helps agents browse, provision, manage, and pay for GPU/VPS compute, private LLM endpoints, confidential grid inference, hosted agent pods, paid processors, datasets, and encrypted agent backups on Singularity Cloud Network.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivaavimusic](https://clawhub.ai/user/ivaavimusic)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent operators use this skill to manage Singularity Cloud Network resources: browse plans, provision and resize instances, run or consume grid inference, deploy agent pods or processors, buy datasets, and manage encrypted agent backups with wallet or API-key authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through wallet-backed payments and paid compute provisioning.

Mitigation: Use a dedicated low-balance wallet or bounded API key, review costs before execution, and avoid unattended approvals unless the task budget is explicit.

Risk: The skill can create, resize, extend, or destroy compute instances and persistent hosted agents.

Mitigation: Confirm target instance or pod identifiers before destructive or long-running actions, and revoke API or pod integration keys when they are no longer needed.

Risk: Backup workflows can include local agent state.

Mitigation: Prefer specific backup paths over broad backup commands, protect passphrases, and verify restore targets before migrating agent state.

Risk: Some workflows may rely on remote installers or global npm tools.

Mitigation: Review third-party tools before installation and pin or inspect packages in controlled environments.

## Reference(s):

- [x402 Compute documentation](https://docs.x402layer.cc/agentic-access/x402-compute)
- [Cloud Network app](https://cloud.x402compute.cc)
- [ClawHub skill page](https://clawhub.ai/ivaavimusic/skills/x402-compute)
- [x402Compute API Reference](artifact/references/api-reference.md)
- [AI Machines](artifact/references/ai-machines.md)
- [Agent Pods](artifact/references/agent-pods.md)
- [SGL Processors](artifact/references/processors.md)
- [Datasets](artifact/references/datasets.md)
- [SGL Grid - Provide Compute](artifact/references/node-operator.md)
- [Agent Vault](artifact/references/agent-vault.md)
- [OpenWallet / OWS](artifact/references/openwallet-ows.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, code snippets, configuration values, and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can guide actions that spend wallet funds, create or destroy paid compute resources, deploy persistent hosted agents, or back up local agent state.]

## Skill Version(s):

1.24.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
