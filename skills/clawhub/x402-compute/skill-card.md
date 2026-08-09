## Description:

x402 Compute helps agents manage Singularity Cloud Network compute, including GPU/VPS provisioning, private OpenAI-compatible LLM endpoints, SGL Grid inference, grid node operation, hosted Agent Pods, and paid Processor endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivaavimusic](https://clawhub.ai/user/ivaavimusic)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and compute operators use this skill to provision and manage paid cloud compute, deploy private or grid-connected LLM endpoints, consume confidential grid inference, run provider nodes, and create hosted agents or paid processor endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can manage paid compute, hosted agents, wallets, and API keys, so mistaken or over-broad agent execution can create charges, expose access, or destroy resources.

Mitigation: Install only when this authority is intended, prefer revocable API keys, and require explicit confirmation for provisioning, resizing, deletion, wallet sends, API-key changes, and pod lifecycle actions.

Risk: Wallet-backed flows use sensitive EVM or Solana signing credentials.

Mitigation: Use dedicated low-balance wallets and avoid primary custody wallets for signing credentials.

Risk: OpenWallet / OWS and node-operator flows can involve local executables or remote installers.

Mitigation: Avoid raw OWS passthrough unless needed, use a locally installed OWS binary when possible, and verify any remote installer before running it.

Risk: Agent Pods are persistent hosted agents with wallet and integration-key capabilities.

Mitigation: Review pod configuration, limit delegated spend, protect integration keys, and confirm lifecycle actions before execution.

## Reference(s):

- [x402 Compute documentation](https://docs.x402layer.cc/agentic-access/x402-compute)
- [Cloud Network app](https://cloud.x402compute.cc)
- [ClawHub skill page](https://clawhub.ai/ivaavimusic/skills/x402-compute)
- [API reference](references/api-reference.md)
- [AI Machines](references/ai-machines.md)
- [Agent Pods](references/agent-pods.md)
- [SGL Grid node operator](references/node-operator.md)
- [OpenWallet / OWS](references/openwallet-ows.md)
- [SGL Processors](references/processors.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, Python script invocations, HTTP API examples, and JSON snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide paid compute, wallet-signing, API-key, hosted-agent, and resource lifecycle actions when used by an agent.]

## Skill Version(s):

1.13.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
