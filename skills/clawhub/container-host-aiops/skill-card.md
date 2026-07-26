## Description: <br>
Container Host Aiops helps agents inspect, analyze, and operate single Docker, Portainer, or Podman container hosts, including host health, logs, restart-loop RCA, resource pressure, disk bloat, and guarded lifecycle or prune actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operations engineers use this skill to triage and manage non-orchestrator container hosts through Docker Engine, Portainer, or Podman. It supports host overview, container/image/volume/network/system reads, focused RCA analyses, and guarded write workflows with dry-run and audit support. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform destructive Docker, Portainer, or Podman actions with root-equivalent access and no built-in read-only or approval gate. <br>
Mitigation: Install only where agent-level container-host administration is intended; prefer read-only Docker socket mounts or Portainer accounts without write scope for monitoring-only use. <br>
Risk: Write operations such as container removal, image pruning, volume pruning, and stack recreation can remove services or data. <br>
Mitigation: Use dry-run previews before writes, require operator review for destructive actions, and rely on backups for irreversible prune or removal outcomes. <br>
Risk: Unauthenticated Docker TCP, disabled TLS, or exposed management endpoints can expand access beyond the intended host. <br>
Mitigation: Avoid unauthenticated Docker TCP and disabled TLS outside lab environments, and keep Portainer or Docker API access scoped to trusted networks and accounts. <br>
Risk: The local state directory contains audit history, undo state, configuration, and encrypted Portainer tokens. <br>
Mitigation: Protect ~/.container-host-aiops/ and any relocated CONTAINER_HOST_AIOPS_HOME path with appropriate filesystem permissions and operational handling. <br>


## Reference(s): <br>
- [Container Host AIops homepage](https://github.com/AIops-tools/Container-Host-AIops) <br>
- [Capabilities reference](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup and security guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include dry-run previews, host-operation recommendations, and audit-oriented follow-up steps.] <br>

## Skill Version(s): <br>
0.6.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
