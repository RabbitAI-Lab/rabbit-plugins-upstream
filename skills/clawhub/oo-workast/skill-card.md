## Description:

Operate Workast through an OOMOL-connected account to read, create, update, and complete tasks via the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to manage Workast spaces and tasks through an OOMOL-connected account. It supports reading user, space, and task details as well as creating, completing, and updating tasks after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, or complete Workast tasks through the connected OOMOL account.

Mitigation: Confirm the exact payload and expected effect with the user before running any write action.

Risk: First-time install, login, connection, or billing steps may be unnecessary during normal use.

Mitigation: Run setup or account-management steps only after a command fails with the matching CLI, authentication, connection, scope, credential, app, or billing error.

## Reference(s):

- [ClawHub Workast skill page](https://clawhub.ai/oomol/skills/oo-workast)
- [Workast homepage](https://www.workast.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action results are JSON; write actions require explicit user confirmation before execution.]

## Skill Version(s):

1.0.0 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
