## Description:

Freshteam lets an agent inspect live action schemas and read Freshteam employees, job postings, fields, candidate sources, and related recruiting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, HR operators, recruiting teams, and developers use this skill to retrieve Freshteam employee and recruiting records through connected OOMOL and Freshteam accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts for the oo CLI.

Mitigation: Review installer contents and install the oo CLI through a trusted, versioned, verifiable method before use.

Risk: The skill can query Freshteam HR and recruiting data through a connected account.

Mitigation: Connect only a Freshteam account with the minimum access needed for the HR or recruiting data being queried.

## Reference(s):

- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Freshteam homepage](https://www.freshworks.com/freshteam/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands run through the oo CLI against live Freshteam connector schemas.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
