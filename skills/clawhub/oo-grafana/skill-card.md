## Description:

Enables agents to read, create, update, and delete Grafana resources through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Grafana dashboards, folders, data sources, alerting resources, and searches through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include remote installer commands that can run unverified scripts in a shell.

Mitigation: Review before installing, use safer official installation methods for the oo CLI where possible, and do not let an agent run the remote installer automatically.

Risk: Grafana write and destructive actions can create, update, delete, or overwrite dashboards, folders, and data sources.

Mitigation: Confirm the exact action, target, payload, and effect with the user before writes, and require explicit approval before delete operations.

## Reference(s):

- [Grafana homepage](https://grafana.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-grafana)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON responses containing connector data and an execution id.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
