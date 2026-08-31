## Description:

Query and act on Resy restaurant reservations from a shell: search venues, check slot availability, book or cancel reservations, and manage favorites and Priority Notify using curl and an optional one-time fpx token bootstrap.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to have an agent produce Resy API curl workflows for reservation search, availability checks, booking, cancellation, favorites, notify settings, and account profile inspection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ready-to-run booking, cancellation, favorite, and notify commands can change a real Resy account.

Mitigation: Require explicit approval for each write action and verify the account state with list or profile calls before and after the change.

Risk: RESY_TOKEN grants account access and may appear in shell variables or command history.

Mitigation: Treat RESY_TOKEN as a sensitive account token, avoid logging it, and remove stored shell variables or fpx profiles when no longer needed.

Risk: The curl layer has no dry-run mode for write actions.

Mitigation: Use read-only calls to inspect the target reservation, venue, favorite, or notify entry before issuing a write command.

## Reference(s):

- [Resy API ready-to-run requests](references/resy-api.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require a user-provided Resy token or credentials; write examples affect a live Resy account.]

## Skill Version(s):

0.9.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
