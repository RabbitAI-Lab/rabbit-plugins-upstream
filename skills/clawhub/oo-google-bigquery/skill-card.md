## Description:

Enables an agent to operate Google BigQuery through OOMOL's oo CLI for reading, creating, updating, deleting data, running queries, and managing BigQuery resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and data teams use this skill to let an agent inspect BigQuery metadata, run SQL queries, manage datasets, tables, routines, models, and start import or export jobs through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes an external installer script for the oo CLI that could run code on the host.

Mitigation: Review and install the oo CLI manually from a trusted source; do not allow an agent to run the installer automatically.

Risk: BigQuery write, update, delete, export, and load actions can change data, remove resources, or move data to Cloud Storage.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before running any write or destructive action.

Risk: The skill routes BigQuery access through OOMOL-connected credentials.

Mitigation: Use the skill only when OOMOL is an acceptable BigQuery access path and the connected account has appropriate scopes for the requested task.

## Reference(s):

- [ClawHub Google BigQuery skill](https://clawhub.ai/oomol/skills/oo-google-bigquery)
- [Google BigQuery homepage](https://cloud.google.com/bigquery)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads; connector responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI and an OOMOL-connected Google BigQuery account; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.4 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
