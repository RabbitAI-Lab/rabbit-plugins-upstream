## Description:

GitHub (github.com) support for reading, creating, updating, and deleting GitHub data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect and manage GitHub repositories, issues, pull requests, releases, Actions workflows, branches, commits, labels, milestones, and files through OOMOL's GitHub connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run unverified remote installer scripts.

Mitigation: Review the setup path before installing and prefer a verified, version-pinned oo CLI source.

Risk: The skill can perform write or destructive GitHub actions when the connected account has permission.

Mitigation: Allow GitHub write or destructive actions only after checking the exact repository, target, action, and JSON payload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-github)
- [GitHub](https://github.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON; write and destructive actions require confirmation of the repository, target, action, and payload before execution.]

## Skill Version(s):

1.0.9 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
