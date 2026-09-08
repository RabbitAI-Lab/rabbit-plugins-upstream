## Description:

Access Artsonia student art portfolios, comments, fans, teacher feedback, and downloads from a shell with curl by logging in with a username/password form POST and using the resulting session cookie to fetch server-rendered member pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers with authorized Artsonia parent access use this skill to run curl-based reads, downloads, and selected form POSTs for student portfolios, profile data, comments, fans, feedback, and awards without operating the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive student-related records, account profile data, cookie jars, downloaded HTML, and artwork images.

Mitigation: Use it only for Artsonia accounts and student records you are authorized to access; store cookies and downloaded data securely and avoid shared machines.

Risk: Artwork images, including private pieces, may be downloadable from a public CDN without an authenticated session.

Mitigation: Do not bulk-download, redistribute, or retain artwork unless you have explicit authorization and a clear retention need.

Risk: Invite, comment, feedback, and profile POST examples can cause side effects in the live Artsonia account.

Mitigation: Run POST recipes only with explicit consent, use test-safe values where possible, and re-fetch the affected page to confirm the intended change.

Risk: Credentials and session cookies can grant access to private account data.

Mitigation: Read passwords from standard input or a secret manager, keep the cookie jar private, and refresh or remove it when the session is no longer needed.

## Reference(s):

- [Artsonia endpoints - curl and parser recipes](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/artsonia-api)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands, curl examples, Node.js parser snippets, and jq projections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command recipes and safety guidance; it does not produce a running service.]

## Skill Version(s):

0.12.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
