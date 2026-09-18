## Description:

Ticketmaster lets agents search and retrieve Ticketmaster event, venue, attraction, classification, image, suggestion, section-map, and Season Ticketing command results through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Ticketmaster data and retrieve event-related details through OOMOL's Ticketmaster connector. Season Ticketing command execution should be used only after the exact command, payload, target, and expected effect are shown and approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Season Ticketing command execution may change Ticketmaster state if the command and payload are not understood.

Mitigation: Use read/search actions by default; run Season Ticketing commands only when the exact command, payload, target, and expected effect are shown and explicitly approved.

Risk: Remote installer commands can execute downloaded code in the user's shell.

Mitigation: Do not run the remote installer commands unless the OOMOL installer source is trusted and the download has been verified through a safer channel.

## Reference(s):

- [ClawHub Ticketmaster skill page](https://clawhub.ai/oomol/skills/oo-ticketmaster)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Ticketmaster homepage](https://www.ticketmaster.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON data with execution metadata when run through the oo CLI.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
