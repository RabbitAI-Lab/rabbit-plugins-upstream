## Description:

Container Host AIops helps an agent inspect and administer a single Docker, Portainer, or Podman container host with host overviews, container/image/volume/network/system reads, restart-loop and resource-pressure analysis, bloat analysis, and guarded lifecycle or prune actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to triage and manage non-orchestrator container hosts, including crash-loop investigation, resource pressure review, disk cleanup planning, and guarded container or Portainer stack actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable Docker, Podman, or Portainer access can stop services, remove containers, prune images, or delete volumes without an enforced read-only or approval boundary in the skill.

Mitigation: Use a read-only Docker socket, a restricted Portainer account, or an isolated test host for diagnostics; enable write-capable access only for sessions where destructive actions are intended.

Risk: Volume pruning and some remove or recreate actions are irreversible and may delete data or reproduce a broken stack definition.

Mitigation: Require dry-run review before high-risk actions, confirm backups for data-bearing volumes, and treat audit or undo records as operational records rather than guaranteed recovery.

Risk: The reviewed artifact does not pin the runtime package installed by the agent.

Mitigation: Verify the exact installed package version before use and align it with the reviewed release version 0.11.1.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/container-host-aiops)
- [Container Host AIops source homepage](https://github.com/AIops-tools/Container-Host-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, and structured tool-result summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include live container-host diagnostics, ranked analyses, dry-run previews, audit or undo guidance, and truncated log/event indicators.]

## Skill Version(s):

0.11.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
