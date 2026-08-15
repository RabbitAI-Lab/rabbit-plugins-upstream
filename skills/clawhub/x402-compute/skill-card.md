## Description:

x402 Compute helps agents browse, provision, manage, and tear down paid Singularity Cloud Network compute, AI Machines, grid inference, Agent Pods, processors, and related wallet/API-key flows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivaavimusic](https://clawhub.ai/user/ivaavimusic)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill to manage paid GPU/VPS infrastructure, deploy private OpenAI-compatible LLM endpoints, consume or provide grid inference, operate hosted Agent Pods, and publish paid processors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend funds on paid compute, extensions, credits, grid operations, hosted agents, and processor workflows.

Mitigation: Use dedicated low-balance wallets, keep spend caps enabled, and require explicit confirmation before provisioning, extending, auto-renewing, or sending wallet payments.

Risk: The skill handles sensitive wallet keys, API keys, managed agent keys, and one-time passwords.

Mitigation: Prefer COMPUTE_API_KEY or OWS for routine management, avoid primary custody keys, keep credentials out of logs and transcripts, and revoke or rotate keys after use.

Risk: Destroy, resize, wallet-send, and background-service actions can have irreversible operational or financial effects.

Mitigation: Review target instance or pod details, confirm destructive actions explicitly, and verify irreversible disk-growth or wallet-send parameters before execution.

Risk: Some workflows reference remote installers or external command-line tools.

Mitigation: Verify remote installers and package sources before execution, and prefer pinned or locally installed wallet tooling for sensitive operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ivaavimusic/skills/x402-compute)
- [x402 Compute Documentation](https://docs.x402layer.cc/agentic-access/x402-compute)
- [Cloud Network App](https://cloud.x402compute.cc)
- [x402Compute API Reference](references/api-reference.md)
- [AI Machines](references/ai-machines.md)
- [Agent Pods](references/agent-pods.md)
- [SGL Grid Node Operator](references/node-operator.md)
- [OpenWallet / OWS](references/openwallet-ows.md)
- [SGL Processors](references/processors.md)
- [Compute API Base](https://compute.x402layer.cc)
- [Grid API Base](https://grid.x402compute.cc)
- [Staking App](https://staking.x402layer.cc)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown with inline shell commands, configuration snippets, JSON examples, and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide API calls and local script execution for paid compute, wallet signing, API-key management, and hosted agent workflows.]

## Skill Version(s):

1.17.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
