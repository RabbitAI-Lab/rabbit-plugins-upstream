## Description:

resy-fpx helps agents query and manage Resy reservations from a shell with curl, using fpx only for one-time token bootstrap when Resy credentials are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users use this skill to generate shell-based Resy workflows for venue search, slot lookup, booking, cancellation, favorites, Priority Notify, and profile/payment lookup without running a Resy MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write commands can book, cancel, favorite, unfavorite, add Priority Notify, or remove Priority Notify entries on the user's Resy account.

Mitigation: Verify reservation, venue, date, party size, and notify details before running any write or DELETE command; list resources before and after changes.

Risk: The skill requires access to Resy credentials or a Resy auth token.

Mitigation: Keep credentials and tokens out of logs and shared transcripts, and re-mint the token if authenticated calls fail.

## Reference(s):

- [Resy API ready-to-run requests](references/resy-api.md)
- [Resy](https://resy.com)
- [resy-fpx ClawHub release page](https://clawhub.ai/chrischall/skills/resy-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require Resy credentials or a Resy auth token and can mutate the user's Resy account.]

## Skill Version(s):

0.7.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
