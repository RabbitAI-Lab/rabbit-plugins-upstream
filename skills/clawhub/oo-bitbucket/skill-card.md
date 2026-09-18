## Description:

Enables agents to operate Bitbucket through the OOMOL-connected oo CLI for reading, creating, updating, and deleting Bitbucket data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to inspect and manage Bitbucket workspaces, repositories, branches, commits, pull requests, issues, pipelines, variables, runners, and members through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow can ask users to run an unverified remote installer script.

Mitigation: Review the installer before installing the oo CLI and prefer a signed, versioned, or checksum-verified installation source.

Risk: The skill can perform write and destructive Bitbucket actions, including deleting branches, pipeline variables, or repositories.

Mitigation: Confirm the exact repository, payload, and effect before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub Bitbucket skill page](https://clawhub.ai/oomol/skills/oo-bitbucket)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Bitbucket](https://bitbucket.org)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May issue live oo CLI commands that return JSON when the user has authenticated and connected Bitbucket.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
