## Description:

Operates and analyzes single Docker, Portainer, or Podman container hosts with governed reads, restart-loop and resource-pressure analysis, storage-bloat analysis, and guarded lifecycle or cleanup writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to triage single container hosts, inspect containers, images, volumes, networks, stacks, and pods, and run focused analyses for restart loops, resource pressure, and reclaimable storage. It also supports audited, guarded writes such as restart, stop, start, remove, prune, resource-limit update, and Portainer stack recreation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Container-host access can be root-equivalent, and write-enabled MCP use can stop services or delete data.

Mitigation: Install only in a controlled environment, start with read-only or narrowly scoped accounts, and prefer external authorization or separate read-only and write-capable deployments.

Risk: Plain Docker TCP or disabled TLS verification can expose host-control traffic.

Mitigation: Avoid plaintext Docker TCP and avoid disabling TLS verification for Portainer or TLS Docker endpoints outside a lab.

Risk: High-risk cleanup and lifecycle operations such as container removal, image or volume pruning, and stack recreation may be destructive or irreversible.

Mitigation: Use dry-run previews, review candidates before execution, keep backups for data-bearing volumes, and rely on narrowly scoped host or Portainer permissions for enforcement.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/container-host-aiops)
- [Project homepage](https://github.com/AIops-tools/Container-Host-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live host observations, ranked analyses, dry-run previews, and audit or undo guidance.]

## Skill Version(s):

0.11.3 (source: server release metadata and release changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
