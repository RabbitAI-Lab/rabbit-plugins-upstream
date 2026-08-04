## Description: <br>
Container-host AIops helps agents inspect, analyze, and perform guarded operations on a single Docker, Portainer, or Podman container host. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations engineers use this skill to triage a non-orchestrated container host, inspect containers, images, volumes, networks, and system state, run restart-loop/resource-pressure/bloat analyses, and prepare guarded lifecycle or cleanup actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can operate Docker, Portainer, or Podman with destructive host-level permissions and does not enforce an MCP approval gate or read-only mode. <br>
Mitigation: Install it only where an administrator intentionally wants agent-assisted container-host operations, use read-only Docker socket mounts or limited Portainer accounts for observation, and require explicit human approval outside the skill for writes. <br>
Risk: Docker socket access and unauthenticated Docker TCP access can be equivalent to host-root control. <br>
Mitigation: Protect socket permissions, avoid unauthenticated Docker TCP, enable TLS for TCP Docker daemons, and prefer least-privilege accounts or read-only mounts where possible. <br>
Risk: Local configuration, audit, undo, and encrypted secret material under ~/.container-host-aiops can expose operational context or credentials if mishandled. <br>
Mitigation: Protect ~/.container-host-aiops, keep Portainer tokens encrypted, avoid logging secrets, and control access to the host account running the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/container-host-aiops) <br>
- [Project homepage](https://github.com/AIops-tools/Container-Host-AIops) <br>
- [Capabilities reference](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup and security guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured host-operation results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include read results, analysis summaries, dry-run previews, risk labels, audit/undo references, and recommended next actions.] <br>

## Skill Version(s): <br>
0.8.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
