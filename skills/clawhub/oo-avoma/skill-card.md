## Description:

Avoma (avoma.com). Use this skill for ANY Avoma request - searching and reading data. Whenever a task involves Avoma, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and read Avoma meetings, recordings, transcriptions, meeting insights, and visible users through an OOMOL-connected Avoma account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that could execute changing code on the user's machine.

Mitigation: Do not let an agent run installer one-liners automatically; install the oo CLI through a reviewed, version-pinned, verified method.

Risk: The skill mediates access to Avoma data through OOMOL-connected credentials.

Mitigation: Connect Avoma deliberately with an account limited to the data the agent is intended to read.

## Reference(s):

- [ClawHub Avoma Skill](https://clawhub.ai/oomol/skills/oo-avoma)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Avoma Homepage](https://www.avoma.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Avoma connector workflows; live action schemas are inspected before payloads are built.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
