## Description:

x402 Compute helps agents provision and manage GPU/VPS instances, AI Machines, SGL Grid inference, Agent Pods, Processors, Datasets, and Agent Vault workflows for Singularity Cloud Network.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivaavimusic](https://clawhub.ai/user/ivaavimusic)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to browse compute plans, provision or manage paid GPU/VPS instances, deploy private OpenAI-compatible endpoints or hosted agent pods, operate grid nodes, and invoke related x402 payment-backed services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger paid compute actions and long-running infrastructure changes.

Mitigation: Review proposed provision, extend, resize, and top-up commands before execution; set explicit spend bounds and avoid non-interactive --yes flows unless the budget and target are tightly scoped.

Risk: The skill handles wallet keys, API keys, and bearer tokens for payment and management flows.

Mitigation: Use dedicated low-balance wallets, protect COMPUTE_API_KEY and signing keys as secrets, and avoid sending bearer tokens to plaintext HTTP endpoints.

Risk: Destructive actions can delete compute instances, processors, keys, pods, or broad backup/restore targets.

Mitigation: Confirm exact resource IDs, backup paths, restore destinations, and daemon/service changes before running deletion, restore, install, or migration steps.

Risk: Dependency and external CLI flows can introduce supply-chain risk.

Mitigation: Pin Python dependencies for deployment, verify remote installers or CLIs before use, and prefer explicitly installed wallet tooling over runtime downloads.

Risk: Password fallback and private endpoint credentials can expose server access.

Mitigation: Prefer SSH public keys, treat one-time passwords and generated endpoint API keys as sensitive, and store or transmit them only through trusted channels.

## Reference(s):

- [x402 Compute documentation](https://docs.x402layer.cc/agentic-access/x402-compute)
- [x402 Compute ClawHub listing](https://clawhub.ai/ivaavimusic/skills/x402-compute)
- [Cloud Network app](https://cloud.x402compute.cc)
- [API reference](references/api-reference.md)
- [AI Machines](references/ai-machines.md)
- [Agent Pods](references/agent-pods.md)
- [Processors](references/processors.md)
- [Agent Vault](references/agent-vault.md)
- [Datasets](references/datasets.md)
- [Node operator](references/node-operator.md)
- [OpenWallet OWS](references/openwallet-ows.md)
- [SGL staking](https://staking.x402layer.cc)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, configuration values, and JSON/API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include payment, wallet, server, and API-key handling steps that require user review before execution.]

## Skill Version(s):

1.25.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
