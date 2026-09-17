## Description:

Enables agents to operate Oracle Cloud Infrastructure resources through OOMOL-connected oo CLI actions for reading, creating, updating, deleting, and monitoring cloud resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inspect, provision, update, and delete OCI network, compute, monitoring, tenancy, and compartment resources through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate OCI resources and includes write, delete, instance action, and remote command capabilities.

Mitigation: Require explicit approval for every write, delete, instance action, and remote command, including confirmation of the target resource and payload.

Risk: Remote Oracle Cloud Agent commands may execute scripts on cloud instances with the agent service account's privileges.

Mitigation: Review the exact script, target instance, compartment, and expected effect before execution, and prefer least-privilege OCI permissions.

Risk: The artifact recommends installer commands that pipe remote scripts directly to a shell.

Mitigation: Install the oo CLI through a verified, signed, or checksum-checked method instead of piping remote installer scripts directly to a shell.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-oracle-cloud)
- [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live action schema inspection before execution and explicit user confirmation for state-changing actions.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
