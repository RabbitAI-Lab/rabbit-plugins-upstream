## Description:

OpenAlex (openalex.org). Use this skill for OpenAlex search and data retrieval requests through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use this skill to query OpenAlex for autocomplete suggestions, works, entities, filtered lists, pagination, and grouping through the oo CLI. It is intended for read-oriented scholarly metadata retrieval after the user has connected OpenAlex in OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Install the oo CLI through a verified package manager or use a downloaded, inspected, checksum-verified installer before running OpenAlex queries.

Risk: Connector calls depend on user account authentication, OpenAlex connection state, and available OOMOL billing credit.

Mitigation: Run setup or billing actions only after a relevant command fails and the user confirms the needed account or connection step.

## Reference(s):

- [OpenAlex](https://openalex.org/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [OpenAlex skill page](https://clawhub.ai/oomol/skills/oo-openalex)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
