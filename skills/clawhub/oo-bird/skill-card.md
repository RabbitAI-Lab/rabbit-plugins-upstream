## Description:

Bird connector for reading, creating, updating, and deleting Bird data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to manage Bird contacts, channels, messages, and message interactions through an OOMOL-connected Bird account. It supports read operations directly and requires confirmation for writes, message sends, batch sends, updates, and deletes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute code from an external source during setup.

Mitigation: Use the setup commands only when required by a command failure, and verify the oo CLI installer source, version, and integrity before running them.

Risk: Write, message-send, batch-send, update, and delete actions can change or remove Bird data.

Mitigation: Confirm the exact action, target, effect, and JSON payload with the user before execution; require explicit approval for destructive deletes.

## Reference(s):

- [Bird homepage](https://bird.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-bird)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses are JSON when run with --json.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
