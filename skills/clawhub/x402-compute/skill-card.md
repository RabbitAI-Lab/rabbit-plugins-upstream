## Description:

Helps agents manage paid cloud compute, deploy hosted AI services and agents, use grid inference, and publish paid endpoints through Singularity Cloud Network.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivaavimusic](https://clawhub.ai/user/ivaavimusic)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and platform operators use this skill to provision and manage GPU or VPS instances, deploy LLM endpoints and hosted agents, access inference, and operate paid processors or agent backups. These workflows can involve wallet payments, API credentials, and persistent infrastructure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet-signed payments and paid compute can spend funds.

Mitigation: Use a dedicated low-balance wallet and confirm spend and renewal actions before proceeding.

Risk: API keys and hosted-agent wallet or control scopes grant high-impact access.

Mitigation: Use least-privilege, revocable keys and grant processor or pod scopes only when needed.

Risk: Remote installers and destructive infrastructure actions can affect running services.

Mitigation: Inspect installers before execution and confirm exact resource IDs before delete, revoke, resize, or renew actions.

## Reference(s):

- [x402 Compute on ClawHub](https://clawhub.ai/ivaavimusic/skills/x402-compute)
- [x402 Compute documentation](https://docs.x402layer.cc/agentic-access/x402-compute)
- [x402 Compute cloud](https://cloud.x402compute.cc)
- [API reference](artifact/references/api-reference.md)
- [Agent Pods API](artifact/references/agent-pods-api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide paid resource management and credential-backed operations.]

## Skill Version(s):

1.30.1 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
