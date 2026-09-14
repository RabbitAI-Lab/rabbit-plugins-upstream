## Description:

Container Host AIops helps agents inspect and manage single Docker, Portainer, or Podman hosts, including host health, container diagnostics, resource and bloat analyses, and guarded lifecycle or cleanup actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to triage non-orchestrated container hosts, inspect runtime state, analyze restart, resource, and disk issues, and perform audited lifecycle or cleanup actions when authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change or delete Docker, Podman, or Portainer resources.

Mitigation: Install only in trusted administrator environments, use least-privileged accounts or read-only access where possible, and require explicit operator authorization before write actions.

Risk: Unrestricted Docker or Podman socket access can be equivalent to host administrator access.

Mitigation: Avoid exposing unrestricted sockets to agents; prefer least-privileged Portainer credentials or a Docker authorization proxy when write access is not required.

Risk: The executable package may be installed without a pinned version.

Mitigation: Pin and verify the container-host-aiops package before granting access to container-host resources.

Risk: Prune, remove, and redeploy operations can disrupt services or cause data loss.

Mitigation: Use dry-run previews, review candidates carefully, keep backups for data-bearing volumes, and rely on audit and undo records only for reversible operations.

## Reference(s):

- [Container Host AIops project homepage](https://github.com/AIops-tools/Container-Host-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or structured text with CLI commands, configuration guidance, and host-operation results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include live Docker, Portainer, or Podman state; log and event outputs can be bounded or truncated and should be treated as operational evidence.]

## Skill Version(s):

0.11.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
