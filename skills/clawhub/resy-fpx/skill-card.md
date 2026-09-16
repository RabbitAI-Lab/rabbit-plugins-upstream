## Description:

Query and act on Resy restaurant reservations from a shell with curl, using fpx only for one-time token bootstrap when direct Resy credentials are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users use this skill to search venues, check availability, manage favorites and Priority Notify, and book or cancel reservations through Resy account-authenticated shell commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles live Resy credentials, browser-session tokens, profile data, and payment method identifiers.

Mitigation: Use secrets or environment variables, avoid logging or sharing tokens and account output, and prefer the direct credential path when possible.

Risk: Booking, cancellation, favorite, and Priority Notify commands can mutate real reservations and account state.

Mitigation: Require explicit confirmation before write actions and read back reservations, favorites, or notify settings before and after changes.

Risk: The optional fpx browser bridge can access an authenticated Resy browser workflow during token bootstrap.

Mitigation: Use the bridge only for one-time token bootstrap when needed, verify the active browser profile and pairing state, and stop using it after the token is obtained.

## Reference(s):

- [Resy API - ready-to-run requests](artifact/references/resy-api.md)
- [Resy](https://resy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell command examples and API request snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes credential setup guidance and authenticated Resy API request examples.]

## Skill Version(s):

0.14.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
