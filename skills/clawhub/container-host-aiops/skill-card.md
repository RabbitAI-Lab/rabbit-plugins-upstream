## Description:

Governed Docker, Portainer, and Podman container-host operations for host overview, read diagnostics, restart-loop RCA, resource-pressure analysis, disk-bloat analysis, and guarded maintenance writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to inspect and triage a single Docker, Portainer, or Podman container host, analyze restart loops, resource pressure, and image or volume bloat, and prepare guarded maintenance actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes highly privileged Docker, Podman, and Portainer administration operations without a tool-enforced approval or read-only boundary.

Mitigation: Install only where an agent is intended to have container-host administration power; prefer read-only Docker sockets or read-only Portainer accounts for observation and use narrowly scoped maintenance credentials.

Risk: Writable production sockets and management APIs can allow destructive host changes.

Mitigation: Use external approval controls before writable production use and pin or verify the exact package or plugin release before deployment.

Risk: Container removal, image pruning, volume pruning, and stack recreation can be destructive, and some actions do not have an undo path.

Mitigation: Review dry-run previews, confirm the target and scope outside the agent, and maintain backups for data-bearing volumes before destructive maintenance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/container-host-aiops)
- [Container Host AIops homepage](https://github.com/AIops-tools/Container-Host-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include host-health summaries, RCA findings, dry-run maintenance steps, and risk-aware recommendations.]

## Skill Version(s):

0.11.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
