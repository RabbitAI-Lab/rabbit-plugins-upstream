## Description:

Access Artsonia student-art portfolios, comments, fans, teacher feedback, profile data, and artwork downloads from a shell with curl commands against Artsonia's server-rendered member pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized Artsonia account holders use this skill to retrieve Artsonia member pages, parse student-art data, download artwork images, and perform documented account actions from shell workflows without running the Artsonia MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose Artsonia session cookies, profile data, comments, fan invites, and full-resolution student artwork.

Mitigation: Use it only with explicit authorization for the account and student artwork involved, store cookie jars and downloaded files as sensitive data, and remove local copies when finished.

Risk: The skill documents live write operations, including comments, fan invitations, feedback state changes, and profile notification settings.

Mitigation: Run write commands only when the account holder explicitly requested the action, then re-read the affected page to confirm the actual result.

Risk: Full-resolution artwork downloads may be available from public CDN paths even for private pieces.

Mitigation: Avoid bulk downloads unless they are specifically authorized, and limit local retention and sharing of downloaded images.

## Reference(s):

- [Artsonia endpoint curl recipes](artifact/references/endpoints.md)
- [Artsonia member login](https://www.artsonia.com/members/login.asp)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/artsonia-api)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JavaScript parsing snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include curl commands, cookie-jar setup guidance, endpoint paths, jq projections, and verification steps for reads and writes.]

## Skill Version(s):

0.9.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
