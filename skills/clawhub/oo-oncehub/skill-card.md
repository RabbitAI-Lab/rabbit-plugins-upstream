## Description:

OnceHub supports agent-led searching and reading of OnceHub booking pages, bookings, and event types through the OOMOL oncehub connector instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent inspect OnceHub connector schemas and run read-only OnceHub workflows for booking pages, bookings, and event types through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions may run remote oo CLI installer scripts directly in a shell.

Mitigation: Install the oo CLI through a verified package when available, or download, inspect, and verify the installer before running it.

Risk: The skill can read OnceHub booking-related data through the connected OOMOL account.

Mitigation: Use an account with appropriate OnceHub access, inspect the live connector schema before each action, and limit use to the documented read-only actions unless a future release adds write actions with explicit review.

## Reference(s):

- [ClawHub OnceHub skill page](https://clawhub.ai/oomol/skills/oo-oncehub)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OnceHub homepage](https://www.oncehub.com/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Text, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are based on live OnceHub connector schemas and read-only connector responses.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
