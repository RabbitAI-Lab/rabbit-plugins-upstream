## Description:

Guides shell-based access to Artsonia student portfolios, feedback, comments, and artwork using curl without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized parents, guardians, and developers use this skill to retrieve student artwork and account information or manage Artsonia interactions from shell scripts without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent session cookies and downloaded pages can expose account credentials or student information.

Mitigation: Use only authorized accounts, keep cookie jars and downloaded data out of shared or synced locations, and restrict or delete them after use.

Risk: Private artwork images may be downloadable without an authenticated session.

Mitigation: Access or share private artwork only with explicit permission from the account holder.

Risk: Write actions can change account state or send real invitation emails.

Mitigation: Obtain explicit permission before writes, confirm recipients, and recheck the affected page to verify changes.

## Reference(s):

- [Artsonia endpoint recipes](references/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/artsonia-api)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can retrieve student data and perform account changes when run with authorized credentials.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
