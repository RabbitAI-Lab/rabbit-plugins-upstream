## Description:

Writer (writer.com) enables agents to read, create, and update Writer data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate Writer through the OOMOL-connected oo CLI, including chat completion generation and model discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chat completion requests may send conversation text to Writer and consume account credits.

Mitigation: Review payloads before approving chat completion requests and retry billing-related failures only after confirming account credit status.

Risk: Setup commands can change local authentication or service connection state if run unnecessarily.

Mitigation: Run setup steps only after the oo CLI reports an installation, authentication, connection, or billing error.

Risk: Write-tagged actions may change Writer state.

Mitigation: Confirm the exact payload and expected effect with the user before running write-tagged actions.

## Reference(s):

- [Writer homepage](https://writer.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Writer skill page](https://clawhub.ai/oomol/skills/oo-writer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions; write actions require user confirmation.]

## Skill Version(s):

1.0.1 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
