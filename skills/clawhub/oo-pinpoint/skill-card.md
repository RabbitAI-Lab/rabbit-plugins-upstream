## Description:

Pinpoint lets agents search and read Pinpoint applications, candidates, and jobs through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, recruiters, hiring teams, and developers use this skill to retrieve Pinpoint jobs, candidates, and applications through a connected OOMOL account without handling raw tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup suggests running a remote installer directly in a shell.

Mitigation: Review the skill before installation and prefer an official, versioned, verifiable oo CLI installation method.

Risk: Connector use depends on the Pinpoint account and scopes connected through OOMOL.

Mitigation: Connect only the Pinpoint account and scopes intended for the task, and use setup steps only after authentication or connection errors.

## Reference(s):

- [ClawHub Pinpoint skill page](https://clawhub.ai/oomol/skills/oo-pinpoint)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Pinpoint homepage](https://www.pinpointhq.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to fetch live connector schemas before running read-only Pinpoint actions.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
