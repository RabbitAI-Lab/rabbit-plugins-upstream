## Description:

Provides an agent workflow for reading Supervisely user, team, workspace, project, and dataset data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Supervisely connector schemas and run read actions against connected Supervisely accounts for user, team, workspace, project, and dataset information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes running an internet installer directly in a shell.

Mitigation: Install the oo CLI only from verified, versioned OOMOL release instructions and review the installer before execution.

Risk: Connector access depends on the Supervisely account linked through OOMOL.

Mitigation: Confirm which Supervisely account is connected before running connector actions.

## Reference(s):

- [Supervisely homepage](https://supervisely.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-supervisely)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
