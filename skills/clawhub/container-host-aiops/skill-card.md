## Description:

Helps administrators inspect and troubleshoot Docker, Portainer, and Podman container hosts and perform guarded maintenance actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Container-host administrators and engineers use this skill to review host health, investigate restart loops, resource pressure, and disk bloat, and perform container or stack maintenance when authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Container-host access can grant root-equivalent control, and the skill has no internal read-only or approval gate.

Mitigation: Restrict this skill to trusted administrators and use read-only Docker access or a Portainer account without write scope for observation; keep it away from untrusted prompts.

Risk: Pruning, removal, or stack redeployment can cause data loss or downtime.

Mitigation: Review a dry-run preview, confirm authorization, and back up important data before destructive actions.

Risk: Disabling TLS verification weakens protection for remote host connections.

Mitigation: Keep TLS verification enabled outside isolated labs.

## Reference(s):

- [ClawHub release](https://clawhub.ai/zw008/skills/container-host-aiops)
- [Project homepage (listed in release metadata)](https://github.com/AIops-tools/Container-Host-AIops)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command examples and host-analysis summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Host findings and maintenance previews depend on the configured target and its permissions.]

## Skill Version(s):

0.13.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
