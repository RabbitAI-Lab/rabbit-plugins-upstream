## Description:

Helps agents move objects between supported storage services, monitor transfers, and use Beam Rooms for live exchanges between machines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beam-network](https://clawhub.ai/user/beam-network)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to estimate and run object transfers or fan-out across supported storage services, check transfer progress, and coordinate live messages, streams, media, and files in Beam Rooms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live transfers can consume credits and overwrite existing destination objects without a confirmation check enforced by the transfer helper.

Mitigation: Estimate or dry-run first, show the user the sources, destinations, size, and expected cost, and require explicit approval before every live transfer.

Risk: Room creation consumes credits, and broad credentials or grants can expose data or allow unintended actions.

Mitigation: Require explicit approval before creating a Room; use narrowly scoped Beam and storage credentials and least-privilege channel grants.

Risk: Independent transfer workers can read unencrypted data in transit.

Mitigation: Encrypt confidential data before transferring it, or use an agent-only Room object publication.

Risk: A curl-to-shell CLI installer runs remotely supplied code.

Mitigation: Avoid that installer unless the Beam distribution path is trusted.

## Reference(s):

- [Beam skill release](https://clawhub.ai/beam-network/skills/beam)
- [Beam documentation](https://docs.b1m.ai)
- [Transfer reference](references/transfers.md)
- [Rooms reference](references/rooms.md)
- [Choosing a Beam primitive](references/choosing.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance and commands with JSON transfer or Room results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include cost estimates, transfer IDs, progress, and Room status.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
