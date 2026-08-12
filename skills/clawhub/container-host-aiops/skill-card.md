## Description:

Container Host AIops helps agents inspect, analyze, and perform guarded operations on a single Docker, Portainer, or Podman container host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Developers and operations engineers use this skill to triage container host health, diagnose restart loops and resource pressure, review image or volume bloat, and perform dry-run-capable lifecycle or cleanup operations on non-orchestrator container hosts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control a container host through Docker or Podman socket access or a Portainer token, which can be root-equivalent on the host.

Mitigation: Install only for trusted container-host administration and restrict socket or token access to trusted administrators; prefer read-only sockets or non-write Portainer accounts for observation workflows.

Risk: Destructive writes such as remove, prune, and recreate operations can be irreversible and the skill does not provide a built-in approval or read-only gate.

Mitigation: Require review of dry-run output before writes, use account-level permissions to block writes when appropriate, and keep backups for data-bearing volumes before pruning or removal.

Risk: Local audit, undo, configuration, and encrypted secret files may contain sensitive operational history or credentials metadata.

Mitigation: Protect the ~/.container-host-aiops directory with appropriate file permissions and periodically clean up retained audit, undo, config, and encrypted secret files according to local policy.

## Reference(s):

- [Container Host AIops ClawHub Skill](https://clawhub.ai/zw008/skills/container-host-aiops)
- [Project homepage](https://github.com/AIops-tools/Container-Host-AIops)
- [Capabilities reference](artifact/references/capabilities.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Setup and security guide](artifact/references/setup-guide.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text, markdown]

**Output Format:** [Markdown guidance with inline shell commands and structured operational recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose MCP or CLI actions for reads, analyses, dry-run previews, and guarded writes against configured Docker, Portainer, or Podman targets.]

## Skill Version(s):

0.10.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
