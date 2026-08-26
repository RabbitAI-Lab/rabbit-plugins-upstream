## Description:

Formaloo lets agents read, create, update, and delete Formaloo data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected Formaloo account from an agent, including form discovery, form inspection, submitted-row retrieval, row creation, row updates, and row deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, and delete data in a connected Formaloo account.

Mitigation: Review the exact payload and effect before write actions, and require explicit approval before deleting rows.

Risk: Incorrect payloads or stale assumptions about an action schema could cause failed or unintended Formaloo operations.

Mitigation: Fetch the live connector schema with oo connector schema before building each action payload.

Risk: The skill depends on an installed oo CLI, an authenticated OOMOL account, and an active Formaloo connection.

Mitigation: Run first-time setup steps only when commands fail with installation, authentication, connection, scope, credential, app, or billing errors.

## Reference(s):

- [ClawHub Formaloo skill page](https://clawhub.ai/oomol/skills/oo-formaloo)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Formaloo homepage](https://www.formaloo.com/)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing JSON payloads; write and destructive actions require confirmation.]

## Skill Version(s):

1.0.1 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
