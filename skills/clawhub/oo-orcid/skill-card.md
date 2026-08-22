## Description:

ORCID lookup helper for searching public ORCID records and reading public researcher records and works through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to perform ORCID-related lookup tasks through an OOMOL-connected account, including retrieving public researcher records, retrieving works summaries, and searching public ORCID records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the OOMOL oo CLI and an OOMOL-connected ORCID account, so commands can fail when the CLI is missing, authentication is absent, the ORCID connection is expired, or billing is stopped.

Mitigation: Use the artifact's first-time setup guidance only after a matching command failure and resolve the specific CLI, authentication, connection, or billing issue before retrying.

Risk: Future ORCID connector schemas could expose write or destructive actions even though the current artifact-backed actions are public lookups.

Mitigation: Inspect the live connector schema before building payloads and require explicit user confirmation before running any write or destructive action.

## Reference(s):

- [ORCID homepage](https://orcid.org/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-orcid)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
