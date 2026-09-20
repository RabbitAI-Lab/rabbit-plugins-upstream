## Description:

Operate Asana through an OOMOL-connected account to read, create, update, and delete Asana data using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to operate Asana workspaces, projects, tasks, teams, users, tags, stories, attachments, and custom fields through an OOMOL-connected Asana account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read, create, update, and delete Asana resources, including destructive actions.

Mitigation: Require user confirmation for actions tagged [write] or [destructive], and verify the target and payload before execution.

Risk: The skill documentation includes remote installer commands for the oo CLI.

Mitigation: Do not run installer commands automatically; install the CLI only from a trusted source after verifying the installer or using safer platform package steps.

## Reference(s):

- [Asana homepage](https://asana.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector runs return JSON responses with data and meta.executionId.]

## Skill Version(s):

1.0.5 (source: server evidence release.version and skill metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
