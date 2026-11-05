## Description:

Access Artsonia (artsonia.com) student-art portfolios, comments, fans, teacher feedback, and downloads from a shell with curl instead of running the artsonia-mcp server — log in with a username/password form POST to get a session cookie, then curl the server-rendered member pages. Use when you want Artsonia data without the MCP, in a script, or on a machine where the MCP isn't installed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and developers can use this skill to read Artsonia student portfolios, artwork details, comments, fans, feedback, awards, and profile information with curl. It also provides examples for account actions such as posting comments, inviting fans, and changing feedback or notification state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local page captures can contain children’s private information, and a reusable login cookie could be exposed to other local users.

Mitigation: Use a private temporary directory, set umask 077 and cookie file permissions to 600, then remove sensitive pages and cookies when finished.

Risk: Examples can change account data or send an invitation, comment, or other action when executed.

Mitigation: Limit use to reads unless the user explicitly requests the specific write; verify changes by fetching the affected page again.

## Reference(s):

- [Artsonia API endpoints and curl recipes](artifact/references/endpoints.md)
- [Artsonia member login](https://www.artsonia.com/members/login.asp)
- [Artsonia skill release](https://clawhub.ai/chrischall/skills/artsonia-api)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Files]

**Output Format:** [Markdown instructions with curl examples; fetched server-rendered HTML and artwork image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use authenticated session cookies for member data; artwork image downloads are available without authentication.]

## Skill Version(s):

1.4.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
