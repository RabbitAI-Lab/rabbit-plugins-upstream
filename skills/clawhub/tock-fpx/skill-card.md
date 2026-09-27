## Description:

Guides agents in querying Tock restaurant listings, availability, and signed-in reservations through the fpx CLI and a paired browser tab without running the Tock MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to browse Tock metros and venues, check bookable availability, and retrieve their own reservations through a paired browser session. Booking and cancellation remain on the Tock website.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pairing fpx with a signed-in Tock tab grants access to personal reservation details.

Mitigation: Pair only on a trusted device and use the signed-in session only when reservation access is needed.

Risk: Reservation and identity data may remain in terminal output or saved temporary files.

Mitigation: Avoid shared machines, limit exposure of terminal output, and delete saved response files when finished.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/tock-fpx)
- [Tock](https://www.exploretock.com)
- [Tock request recipes](references/requests.md)
- [Redux slice extraction helper](references/extract-redux-slice.mjs)

## Skill Output:

**Output Type(s):** [Shell commands, JSON data, Guidance]

**Output Format:** [Markdown instructions and CLI JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; reservation queries require a signed-in Tock browser tab.]

## Skill Version(s):

1.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
