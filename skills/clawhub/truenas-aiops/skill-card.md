## Description:

Helps agents inspect and manage TrueNAS SCALE storage through health diagnostics, ZFS operations, snapshots, services, and replication status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Storage administrators and engineers use this skill to diagnose TrueNAS SCALE appliance health, inspect pools and datasets, and perform selected storage and service operations through an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable tools can alter storage or services without a built-in MCP approval or read-only gate.

Mitigation: Use a least-privilege TrueNAS API key, preferably read-only for diagnostic work; restrict write tools to supervised, authorized agents.

Risk: Deleting a snapshot permanently removes it and cannot be undone.

Mitigation: Review the target and use a dry run before explicitly approving deletion.

Risk: Long-lived API keys or master passwords exposed in shell environments may be disclosed.

Mitigation: Avoid plaintext shell secrets where possible and protect the credential store and execution environment.

## Reference(s):

- [TrueNAS AIops project homepage](https://github.com/AIops-tools/TrueNAS-AIops)
- [Capabilities](references/capabilities.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline commands and diagnostic summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries can reflect live appliance state; selected tools can change storage or services.]

## Skill Version(s):

0.13.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
