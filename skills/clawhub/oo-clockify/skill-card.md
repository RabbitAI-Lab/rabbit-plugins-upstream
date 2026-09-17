## Description:

Clockify (clockify.me). Use this skill for ANY Clockify request: reading, creating, updating, and deleting data through the OOMOL oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Clockify through an OOMOL-connected account, including listing workspaces, projects, tasks, and time entries, and creating, updating, or deleting supported Clockify records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts directly.

Mitigation: Prefer official oo CLI installation documentation, a pinned installer, and checksum or signature verification before installation.

Risk: Clockify write and destructive actions can create, update, or delete workspace data.

Mitigation: Review the live action schema and confirm the exact payload and target before approving any write or delete action.

Risk: Clockify operations depend on OOMOL as an intermediary for server-managed credentials.

Mitigation: Install and use the skill only when the user trusts OOMOL for Clockify operations.

## Reference(s):

- [Clockify homepage](https://clockify.me)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-clockify)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run oo CLI actions that return JSON responses from Clockify.]

## Skill Version(s):

1.0.3 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
