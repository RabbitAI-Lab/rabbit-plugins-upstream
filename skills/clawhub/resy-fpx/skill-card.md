## Description:

Query and act on Resy reservations from a shell using curl for venue search, slot availability, booking, cancellation, favorites, Priority Notify, and optional fpx token bootstrap when credentials are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation-oriented users use this skill to prepare curl-based Resy workflows for account profile lookup, venue discovery, slot checks, booking, cancellation, favorites, and Priority Notify management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires access to Resy credentials, a Resy auth token, or a signed-in browser session.

Mitigation: Use protected environment variables, avoid logging tokens or command output that contains tokens, and re-mint tokens only when needed.

Risk: Booking, cancellation, favorite, and Priority Notify commands can change the user's real Resy account state.

Mitigation: Review each command before execution and use list/read calls before and after write actions to confirm the intended target and result.

Risk: The optional fpx bootstrap path installs an unpinned global browser-bridge package.

Mitigation: Pin or review the package before installation, use it only for token bootstrap, and remove the global install or profile after use.

## Reference(s):

- [Resy API request examples](references/resy-api.md)
- [Resy](https://resy.com)
- [Resy API base URL](https://api.resy.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands target live Resy endpoints and may mutate reservations, favorites, and notifications when executed.]

## Skill Version(s):

0.14.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
