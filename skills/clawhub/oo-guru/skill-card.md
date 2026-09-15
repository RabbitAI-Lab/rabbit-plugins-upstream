## Description:

Guru (getguru.com) helps agents search and read Guru data through the OOMOL oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to search and read Guru knowledge through an OOMOL-connected account. It supports read-only Guru workflows such as retrieving cards, searching cards, listing collections, checking identity, and viewing team statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes one-line shell and PowerShell installer commands fetched from remote URLs.

Mitigation: Install only from a trusted OOMOL CLI distribution path, prefer an official versioned installer, and verify its signature or checksum before execution.

## Reference(s):

- [Guru homepage](https://www.getguru.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-guru)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guru connector responses are returned as JSON when run with the documented --json flag.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
