## Description:

Query and act on Resy restaurant reservations from a shell without running the resy-mcp server: search venues, check slot availability, book or cancel reservations, and manage favorites or Priority Notify using curl and optional one-time fpx token bootstrap.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation-oriented Resy users use this skill to query reservation data and perform account actions from a shell or script when the Resy MCP server is not installed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Resy account credentials and browser-session tokens.

Mitigation: Use a disposable or tightly controlled shell, avoid terminal logging on shared machines, and unset credentials and tokens after use.

Risk: Booking, cancellation, favorites, and Priority Notify examples can make live account changes.

Mitigation: Verify venue, date, party size, party details, and payment details before write calls; read back reservation or notification state before and after changes.

Risk: The optional browser-token path depends on fpx and a signed-in browser session.

Mitigation: Prefer a pinned or isolated fpx setup for token bootstrap, and do not reuse session-derived tokens outside the intended controlled shell.

Risk: Unattended scripts could execute booking, cancellation, favorites, or notify actions without adequate confirmation.

Mitigation: Add explicit confirmations and validation before automating any write operation.

## Reference(s):

- [Resy API ready-to-run requests](references/resy-api.md)
- [Resy website](https://resy.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown with inline shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes live API examples that require user-provided Resy credentials or a session-derived token; some examples mutate reservations, favorites, and notifications.]

## Skill Version(s):

0.14.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
