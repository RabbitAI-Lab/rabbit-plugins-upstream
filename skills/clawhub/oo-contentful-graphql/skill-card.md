## Description:

Provides agent access to Contentful GraphQL through OOMOL's oo CLI for searching and reading Contentful data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Contentful GraphQL connector schemas and execute Content API queries against connected Contentful spaces and environments through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance documents remote installer commands for the oo CLI.

Mitigation: Prefer a verified, pinned, or package-manager installation path instead of piping remote installer scripts directly into a shell.

Risk: Contentful GraphQL requests and data are routed through OOMOL as an intermediary.

Mitigation: Confirm acceptable data handling, scopes, and environments before use, and limit connected Contentful access to the intended spaces.

## Reference(s):

- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Contentful GraphQL](https://www.contentful.com)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON responses from the OOMOL connector, including data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
