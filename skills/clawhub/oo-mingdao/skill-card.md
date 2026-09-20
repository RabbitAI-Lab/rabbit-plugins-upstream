## Description:

Operate Mingdao through an OOMOL-connected account for reading, creating, updating, and deleting Mingdao data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to work with Mingdao application data and configuration through an OOMOL-connected account. It supports Mingdao tasks such as reading app metadata, querying records, managing worksheets, roles, views, workflows, approvals, knowledge content, and performing confirmed write or destructive operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include executing remote installer scripts directly in a shell.

Mitigation: Review the oo CLI installation method first and prefer official package-manager or signed installer instructions where available.

Risk: Write and destructive Mingdao actions can create, overwrite, delete, or revoke access to business data.

Mitigation: Check the exact target and payload, fetch the live action schema, and require explicit user approval before running write or destructive actions.

## Reference(s):

- [ClawHub Mingdao Skill](https://clawhub.ai/oomol/skills/oo-mingdao)
- [Mingdao Homepage](https://www.mingdao.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects returned from the user's connected Mingdao account.]

## Skill Version(s):

1.0.1 (source: server evidence release.version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
