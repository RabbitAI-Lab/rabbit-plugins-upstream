## Description:

Leiga (leiga.com). Use this skill for ANY Leiga request: searching and reading data through the OOMOL-connected Leiga connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to search and read Leiga projects, issues, issue schemas, and project lists from an OOMOL-connected Leiga account. It guides the agent to inspect live action schemas before running Leiga connector commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include installer commands fetched from the internet for the oo CLI.

Mitigation: Prefer official installation documentation, signed or versioned packages, checksum or signature verification, and non-administrator execution before use.

Risk: The skill depends on OOMOL account, connection, and billing flows to access Leiga.

Mitigation: Connect only the intended OOMOL and Leiga accounts, review requested scopes, and stop on billing or connection errors until the user confirms the account state.

## Reference(s):

- [Leiga homepage](https://www.leiga.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OOMOL server-side credential handling and returns connector responses as JSON when commands are run with --json.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
