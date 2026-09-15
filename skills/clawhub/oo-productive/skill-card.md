## Description:

Productive (productive.io). Use this skill for Productive requests such as reading, creating, updating, and deleting tasks and time entries through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Productive tasks and time entries from an agent session through the OOMOL-connected oo CLI. It supports read, create, update, and delete workflows while requiring live schema inspection before payload construction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands, creating a supply-chain risk if the installer delivery chain is not trusted.

Mitigation: Review the installer path before installing and do not run the remote installer commands unless OOMOL's installer delivery chain is trusted and independently verifiable.

Risk: The skill can create, update, and delete Productive records.

Mitigation: Confirm the exact payload and expected effect before write actions, and get explicit approval before destructive deletions.

## Reference(s):

- [ClawHub Productive skill page](https://clawhub.ai/oomol/skills/oo-productive)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Productive homepage](https://productive.io)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live connector schemas before constructing action payloads and to confirm write or destructive operations with the user.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
