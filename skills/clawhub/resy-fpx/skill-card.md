## Description:

Query and act on Resy restaurant reservations from a shell with curl, using fpx only for one-time token bootstrap when Resy email and password credentials are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users use this skill to search Resy venues, check reservation slots, and manage account actions such as bookings, cancellations, favorites, and Priority Notify from shell workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires sensitive Resy account or session access, including password or token handling.

Mitigation: Protect RESY_PASSWORD and RESY_TOKEN, prefer reviewed credential handling, and avoid exposing tokens in shell history, logs, or shared terminals.

Risk: The optional fpx bootstrap path uses an unpinned global browser-bridge install.

Mitigation: Use a reviewed, pinned, isolated fpx setup when possible, and remove or disconnect the browser bridge after token bootstrap.

Risk: Write operations can create, cancel, favorite, or subscribe to real Resy account records.

Mitigation: Confirm every booking, cancellation, favorite, and Priority Notify command before execution, and read back account state before and after write actions.

## Reference(s):

- [Resy API ready-to-run requests](references/resy-api.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy-fpx)
- [Resy](https://resy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces commands that may make authenticated Resy account changes when executed by the user.]

## Skill Version(s):

0.14.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
