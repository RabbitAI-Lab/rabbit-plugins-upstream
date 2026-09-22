## Description:

OpenClaw Gateway Manager helps an agent inspect, configure, restart, verify, create, and delete OpenClaw gateway instances across supported local and cloud-style distributions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seastaradmin](https://clawhub.ai/user/seastaradmin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage OpenClaw gateway instances, including status checks, port changes, service restarts, configuration verification, instance creation, and guarded deletion. It is most relevant when a user has multiple OpenClaw, JVS Claw, QClaw, cloud, or custom gateway installations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify OpenClaw configuration, service definitions, and gateway processes.

Mitigation: Review commands before execution, use trusted instance names and numeric ports, and manually inspect generated service files.

Risk: Deletion workflows can remove instance directories and may cause data loss.

Mitigation: Keep independent backups, confirm the target instance carefully, and rely on the documented backup behavior before deletion.

Risk: Service creation can introduce persistent execution under the user's account.

Mitigation: Install only trusted releases, inspect LaunchAgent or user-service files, and uninstall unused gateway services.

Risk: The security verdict is suspicious because unsafe script handling could enable persistent command execution or unintended data loss.

Mitigation: Prefer an audited pinned release over a default-branch clone and review this skill carefully before installing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/seastaradmin/skills/gateway-manager)
- [Publisher profile](https://clawhub.ai/user/seastaradmin)
- [Common ports reference](artifact/references/common-ports.md)
- [Security review response](artifact/SECURITY_RESPONSE.md)
- [Package-declared repository](https://github.com/seastaradmin/openclaw-gateway-manager)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and configuration details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to run bundled shell scripts that read or modify local OpenClaw configuration, service, and instance files.]

## Skill Version(s):

1.0.2 (source: server release metadata and clawhub.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
