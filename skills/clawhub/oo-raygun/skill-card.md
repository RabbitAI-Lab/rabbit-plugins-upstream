## Description:

Operate Raygun through the OOMOL oo CLI connector for reading, creating, updating, and deleting Raygun data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect Raygun applications, deployments, and crash reporting error groups, and to manage Raygun deployments through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts.

Mitigation: Independently verify and trust the installer source before running curl-to-bash or PowerShell iex commands.

Risk: The skill can create, update, and delete Raygun deployments.

Mitigation: Confirm each write or destructive action with the user and use a Raygun account with only the permissions needed.

## Reference(s):

- [ClawHub Raygun skill page](https://clawhub.ai/oomol/skills/oo-raygun)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Raygun homepage](https://raygun.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to inspect live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
