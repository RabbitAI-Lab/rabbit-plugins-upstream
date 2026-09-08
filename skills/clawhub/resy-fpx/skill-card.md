## Description:

Query and act on Resy restaurant reservations from a shell with curl against api.resy.com, using @fetchproxy/cli only for one-time token bootstrap when Resy credentials are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to search venues, check availability, book or cancel reservations, manage favorites, and manage Priority Notify from shell workflows without running the Resy MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to install an unpinned global browser bridge and pair it with an authenticated Resy browser session.

Mitigation: Prefer the credential-based curl path when appropriate; otherwise pin and verify @fetchproxy/cli, use a restricted environment, limit pairing to resy.com, and remove the pairing or global install after use.

Risk: Generated commands can perform real reservation, cancellation, favorite, and Priority Notify actions on a Resy account.

Mitigation: Confirm all book, cancel, favorite, and notify commands before running them, and verify state with list or profile calls before and after writes.

## Reference(s):

- [Resy API ready-to-run requests](references/resy-api.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Markdown, Guidance]

**Output Format:** [Markdown with inline shell commands and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes commands that can perform real Resy account actions when executed with valid credentials or an authenticated browser session.]

## Skill Version(s):

0.13.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
