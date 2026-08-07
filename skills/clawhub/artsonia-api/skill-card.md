## Description:

Access Artsonia student-art portfolios, comments, fans, teacher feedback, and downloads from a shell with curl by logging in with a username/password form POST and using the resulting session cookie to fetch server-rendered member pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically proficient users use this skill to script authorized Artsonia account reads and selected account-changing actions without running the Artsonia MCP server. It is most useful for retrieving student portfolios, artwork metadata, comments, fans, teacher feedback, and related images from an authenticated parent account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documents live POST actions that can change Artsonia account state, including comments, fan invitations, feedback status, and profile settings.

Mitigation: Require explicit user confirmation before any POST action and re-read the affected page afterward to verify the intended change persisted.

Risk: Cookie jars, downloaded pages, profile fields, and retrieved images may contain sensitive account or student artwork data.

Mitigation: Store artifacts only in user-controlled locations, avoid sharing them, and delete temporary files when they are no longer needed.

Risk: The documented unauthenticated image URL pattern can retrieve full-resolution artwork images, including private student artwork.

Mitigation: Use image downloads only for content the user is authorized to access and do not use the URL pattern to bypass privacy expectations.

## Reference(s):

- [Artsonia endpoint curl and parser recipes](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/artsonia-api)
- [Artsonia member site](https://www.artsonia.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Code, Markdown, Guidance]

**Output Format:** [Markdown with inline shell commands and parser examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may create cookie jars, downloaded HTML pages, JSON parser output, and image files containing sensitive Artsonia account or student artwork data.]

## Skill Version(s):

0.8.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
