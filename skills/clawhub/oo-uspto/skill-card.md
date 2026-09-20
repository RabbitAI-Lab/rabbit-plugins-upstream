## Description:

USPTO (uspto.gov). Use this skill for ANY USPTO request: searching and reading trademark data without calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve USPTO trademark last-update, case-status, and document-metadata records through OOMOL's USPTO connector without handling raw credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes shell commands that fetch and execute an installer.

Mitigation: Confirm trust in OOMOL and the oo CLI installer, and review or verify the installer before running it.

Risk: Trademark connector requests can fail when authentication, connection scopes, credentials, or billing are not ready.

Mitigation: Only run login, connection, or billing setup steps after the connector command fails with the matching error.

## Reference(s):

- [ClawHub USPTO skill page](https://clawhub.ai/oomol/skills/oo-uspto)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [USPTO homepage](https://www.uspto.gov/)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before connector calls and returns execution metadata with JSON responses.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
