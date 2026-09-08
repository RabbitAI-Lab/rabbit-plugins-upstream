## Description:

Use this GitHub (github.com) skill for reading, creating, updating, and deleting data through the OOMOL GitHub connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect and manage GitHub repositories, issues, pull requests, releases, workflows, files, collaborators, stars, topics, and search results through an OOMOL-connected GitHub account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform broad GitHub write and destructive operations, including repository deletion, collaborator changes, workflow changes, and file edits.

Mitigation: Review the exact payload and effect before write actions, require explicit approval for destructive actions, and verify the GitHub permissions granted to OOMOL.

Risk: Connector credentials are handled by OOMOL and may expire, lack required scope, or be connected to an unintended GitHub account.

Mitigation: Confirm the connected account and scopes when authorization errors occur, and resolve connection or credential issues through OOMOL before retrying.

## Reference(s):

- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [GitHub homepage](https://github.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include GitHub connector responses, execution identifiers, and approval prompts for write or destructive operations.]

## Skill Version(s):

1.0.6 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
