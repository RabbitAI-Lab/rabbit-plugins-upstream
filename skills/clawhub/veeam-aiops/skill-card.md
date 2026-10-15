## Description:

Helps agents inspect and manage Veeam Backup & Replication jobs, repositories, restore points, and sessions through CLI or MCP tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Backup administrators and operations teams use this skill to assess Veeam Backup & Replication health, troubleshoot failed jobs or low repository capacity, manage backup jobs, and initiate VM restores with appropriate authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent access can start or stop backup jobs and initiate a VM restore without an enforced MCP approval or read-only control.

Mitigation: Use a dedicated least-privilege Veeam account, begin with read-only or restricted access, and require human approval before restore or stop actions.

Risk: Untrusted prompts or unattended automation could trigger high-impact operations; an audit log records actions but does not prevent them.

Mitigation: Keep the agent away from untrusted prompts and unattended write workflows; review proposed actions before execution.

Risk: Local credentials or legacy plaintext secrets could be exposed.

Mitigation: Protect the local Veeam configuration and encrypted secret store, and migrate away from legacy plaintext .env credentials.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/veeam-aiops)
- [Project homepage (skill metadata)](https://github.com/AIops-tools/Veeam-AIops)
- [Agent guardrails](artifact/references/agent-guardrails.md)
- [Capabilities](artifact/references/capabilities.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Setup guide](artifact/references/setup-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Text or Markdown with CLI commands and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the configured Veeam server and the connected account's permissions.]

## Skill Version(s):

0.18.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
