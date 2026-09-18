## Description:

x402 Compute helps agents manage Singularity Cloud Network compute workflows, including GPU/VPS provisioning, private or grid LLM endpoints, agent pods, processors, datasets, and encrypted agent backup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivaavimusic](https://clawhub.ai/user/ivaavimusic)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and engineers use this skill to provision and manage paid compute, deploy OpenAI-compatible LLM endpoints and hosted agents, run grid inference, publish paid processors, and create datasets or agent backups through the Singularity Cloud Network.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents through paid cloud resource provisioning and lifecycle changes.

Mitigation: Use explicit user approval, low prepaid balances or spend limits, and review commands before executing paid provisioning, extension, resize, pod, processor, or dataset actions.

Risk: Wallet private keys and compute API keys can authorize payments or management actions.

Mitigation: Use dedicated low-balance wallets, protect API keys as secrets, avoid passing secrets as CLI arguments, and revoke or rotate keys after use.

Risk: Password fallback, plain HTTP endpoints, remote installers, persistent services, auto-renewing pods, and broad backups increase operational exposure.

Mitigation: Prefer SSH keys, require HTTPS/TLS for private endpoints, verify remote installers before running them, review persistent service and auto-renew settings, and scope Agent Vault backups narrowly.

## Reference(s):

- [x402 Compute Documentation](https://docs.x402layer.cc/agentic-access/x402-compute)
- [x402 Compute Cloud App](https://cloud.x402compute.cc)
- [API Reference](references/api-reference.md)
- [AI Machines](references/ai-machines.md)
- [Agent Pods](references/agent-pods.md)
- [Agent Pods API](references/agent-pods-api.md)
- [SGL Processors](references/processors.md)
- [Node Operator](references/node-operator.md)
- [Agent Vault](references/agent-vault.md)
- [Datasets](references/datasets.md)
- [OpenWallet OWS](references/openwallet-ows.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples, code snippets, API calls, and JSON payloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include concrete commands that create paid infrastructure or interact with wallet, API-key, pod, processor, dataset, and backup services.]

## Skill Version(s):

1.29.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
