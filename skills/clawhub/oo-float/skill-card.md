## Description:

Provides read-only Float workspace access through the OOMOL oo CLI connector for listing accounts, allocations, clients, people, and projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to answer Float workspace questions by listing schedule, people, client, project, allocation, and account data through an OOMOL-connected Float account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute changing code on the user's machine.

Mitigation: Review the setup path before installing and prefer an official, versioned, inspectable, or checksum-verified oo CLI installation method.

Risk: The skill accesses live Float workspace data through OOMOL-managed credentials.

Mitigation: Use the documented read-only actions for normal Float queries, fetch the live connector schema before each action, and only perform authentication or connection setup after a command fails for that reason.

## Reference(s):

- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Float homepage](https://www.float.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before each Float connector action and returns read-oriented workspace data through the oo CLI.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
