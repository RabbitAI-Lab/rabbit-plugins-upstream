## Description:

Query and update setlist.fm from a shell without running the setlist-mcp server, using curl for the public REST API and an fpx-captured website session cookie for attendance toggles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and shell users use this skill to read setlist.fm artists, setlists, venues, cities, and users through curl commands, and to mark or unmark personal attendance on a setlist after capturing their own authenticated setlist.fm session cookie.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fpx/Transporter setup can access a signed-in setlist.fm browser session, and the captured COOKIE value acts as sensitive account access.

Mitigation: Use the skill only when comfortable granting that access, do not paste or log the COOKIE value, and clear it after use.

Risk: The attendance write path toggles account state on setlist.fm and can produce the wrong state if executed blindly.

Mitigation: Dry-run first, compare the current state to the desired state, require deliberate confirmation, and re-fetch the page after toggling to verify the result.

Risk: setlist.fm API use has attribution, caching, rate-limit, and free-key non-commercial constraints.

Mitigation: Surface followable setlist.fm links with returned data, avoid persistent caching, respect rate limits, and review setlist.fm terms for the intended use.

## Reference(s):

- [setlist-fpx Skill Page](https://clawhub.ai/chrischall/skills/setlist-fpx)
- [setlist.fm REST API read endpoints](references/rest-api.md)
- [Attendance write walkthrough](references/attendance-write.md)
- [setlist.fm API settings](https://www.setlist.fm/settings/api)
- [setlist.fm REST API base](https://api.setlist.fm/rest)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes REST read examples, cookie-capture setup guidance, attendance-toggle workflow steps, and verification guidance.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
