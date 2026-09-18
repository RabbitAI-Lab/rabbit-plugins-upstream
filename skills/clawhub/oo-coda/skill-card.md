## Description:

Coda (coda.io). Use this skill for Coda requests that read, create, or update data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect live Coda action schemas and run Coda operations for docs, pages, tables, columns, rows, users, and mutation status. Write actions require reviewing the exact payload and expected effect before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes unverified remote installer commands.

Mitigation: Prefer a verified package, pinned release, or manual inspection path before installing the CLI.

Risk: Coda requests and responses are processed through OOMOL as an intermediary service.

Mitigation: Use this skill only when the user trusts OOMOL to process the relevant Coda data, and connect only the minimum documents and permissions needed.

Risk: Write actions can create pages or insert and update rows in Coda.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect before running write actions.

## Reference(s):

- [Coda homepage](https://coda.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-coda)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: skill frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
