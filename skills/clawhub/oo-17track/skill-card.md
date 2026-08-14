## Description:

Enables an agent to operate 17TRACK through an OOMOL-connected account for shipment tracking queries and tracking-number registration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent retrieve 17TRACK quota information, shipment details, and tracking lists, and to register tracking numbers after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can register tracking numbers and change 17TRACK account state.

Mitigation: Require user confirmation of the exact registration payload and expected effect before running write actions.

Risk: The skill operates through an OOMOL-connected 17TRACK account.

Mitigation: Install and use it only when the user is comfortable allowing agent access through that connected account.

Risk: First-time setup may use a remote CLI installer.

Mitigation: Use the remote install step only when the oo CLI is missing and the user trusts the OOMOL installer source.

## Reference(s):

- [17TRACK homepage](https://www.17track.net/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance, configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect live connector schemas before running actions; write actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
