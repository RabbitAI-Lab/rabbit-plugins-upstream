## Description:

Beam helps agents coordinate verified object transfers across supported storage providers and exchange messages, streams, and files in Rooms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beam-network](https://clawhub.ai/user/beam-network)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to estimate, run, monitor, and cancel transfers between S3, R2, S3-compatible storage, Hippius, and Hugging Face, or to coordinate agents through Beam Rooms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Transfers can spend organization credits and overwrite destination objects without an enforced confirmation gate.

Mitigation: Estimate first; verify the source, every destination, and expected cost with the user before running.

Risk: The agent may receive a Beam API key and storage credentials.

Mitigation: Provide only necessary, scoped or temporary credentials and avoid exposing credential values in chat or command arguments.

## Reference(s):

- [Beam documentation](https://docs.b1m.ai)
- [Beam on ClawHub](https://clawhub.ai/beam-network/skills/beam)
- [Choosing a Beam primitive](references/choosing.md)
- [Beam transfers reference](references/transfers.md)
- [Beam Rooms reference](references/rooms.md)
- [Beam Studio reference](references/studio.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, JSON status summaries]

**Output Format:** [Markdown with shell commands and transfer status details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transfer estimates and progress may include sizes, costs, and transfer IDs.]

## Skill Version(s):

0.2.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
