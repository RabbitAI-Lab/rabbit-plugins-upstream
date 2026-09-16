## Description:

Unpaywall helps an agent search and retrieve open-access article metadata through the OOMOL Unpaywall connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they want an agent to retrieve Unpaywall open-access metadata for a DOI or search articles by title through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes unverified remote installer commands.

Mitigation: Install the oo CLI through a verified package or pinned release, and verify checksums or signatures before running installer commands.

Risk: Using the connector routes Unpaywall lookups through OOMOL with connected credentials.

Mitigation: Connect OOMOL and Unpaywall only after confirming that this routing and credential handling model is acceptable for the intended use.

## Reference(s):

- [Unpaywall homepage](https://unpaywall.org/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-unpaywall)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON when actions are run with --json.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
