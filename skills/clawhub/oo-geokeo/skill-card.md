## Description:

Geokeo (geokeo.com) lets an agent read, create, and update Geokeo data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run Geokeo forward and reverse geocoding actions through an OOMOL-connected account. The skill guides agents to inspect the live action schema before constructing payloads and to handle setup only when an auth, connection, or billing failure occurs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup guidance includes pipe-to-shell installer commands for the OOMOL oo CLI.

Mitigation: Review the installer source before use and prefer a package manager, signed installer, pinned release, or checksum-verified download.

Risk: The forward geocoding action is tagged as a write action.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [Geokeo homepage](https://geokeo.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector executions return JSON responses with data and meta.executionId when commands are run.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
