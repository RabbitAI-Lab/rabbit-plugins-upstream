## Description:

Teamtailor (teamtailor.com). Use this skill for ANY Teamtailor request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and read Teamtailor data through an OOMOL-connected account. It supports listing departments, jobs, and locations, and retrieving individual jobs with optional included relationships.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts.

Mitigation: Review the OOMOL CLI installation source before use, and prefer a pinned, signed, or package-manager installation method when available.

Risk: Use outside the listed read-only Teamtailor actions could exceed the documented release behavior.

Mitigation: Use only the documented read-only actions unless a future version clearly documents and scopes write operations.

## Reference(s):

- [ClawHub Teamtailor skill page](https://clawhub.ai/oomol/skills/oo-teamtailor)
- [Teamtailor homepage](https://www.teamtailor.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON data with execution metadata when run through the oo CLI.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
