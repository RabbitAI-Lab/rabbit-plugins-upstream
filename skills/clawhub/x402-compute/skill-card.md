## Description:

x402 Compute helps agents provision and manage Singularity Cloud Network compute, deploy OpenAI-compatible LLM endpoints and hosted agents, run grid inference, operate nodes, publish paid processors, buy datasets, and manage encrypted agent backups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivaavimusic](https://clawhub.ai/user/ivaavimusic)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and external agent builders use this skill to compare GPU and VPS plans, provision or manage compute instances, deploy private or grid LLM endpoints, run confidential grid inference, operate compute nodes, deploy hosted agents, publish paid processors, purchase JSONL datasets, and back up or migrate agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend funds through x402 payments and wallet-backed workflows.

Mitigation: Use dedicated low-balance wallets, set tight spend caps, and review payment details before approving transactions.

Risk: The skill can create, resize, extend, or destroy cloud compute resources and hosted agents.

Mitigation: Review lifecycle commands before execution, avoid non-interactive approval flags until tested, and verify the target instance or pod id before destructive actions.

Risk: The skill can create reusable compute API keys and pod integration keys.

Mitigation: Store keys securely, scope them to the intended workflow, and revoke keys that are no longer needed.

Risk: Private AI Machine endpoints may expose prompts or API keys over an unprotected endpoint if TLS is not configured.

Mitigation: Add TLS before sending sensitive prompts or credentials to private AI Machine endpoints.

Risk: Node-operation setup can run remote installers and persistent services.

Mitigation: Inspect remote installers before running them and review service configuration before enabling long-running node workflows.

## Reference(s):

- [x402 Compute ClawHub listing](https://clawhub.ai/ivaavimusic/skills/x402-compute)
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

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, Python script invocations, API request examples, and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce cloud, wallet, payment, API-key, and lifecycle-management actions that should be reviewed before execution.]

## Skill Version(s):

1.22.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
