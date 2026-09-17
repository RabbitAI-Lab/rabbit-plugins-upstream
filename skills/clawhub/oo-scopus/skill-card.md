## Description:

Scopus helps agents search and read Scopus abstracts, affiliations, authors, documents, and serial sources through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run read-only Scopus searches and retrieve scholarly metadata through the OOMOL Scopus connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute directly in a shell.

Mitigation: Install the oo CLI through a trusted, version-pinned package or verified download, and avoid pipe-to-shell installers unless the publisher and local system changes are understood.

Risk: Connector calls depend on live schemas, authentication state, connected Scopus scopes, and OOMOL billing status.

Mitigation: Inspect the connector schema before building payloads, run setup only after a matching failure, and resolve auth, connection, scope, or billing errors before retrying.

## Reference(s):

- [Scopus homepage](https://www.scopus.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Scopus ClawHub release](https://clawhub.ai/oomol/skills/oo-scopus)
- [Scopus icon](https://static.oomol.com/logo/third-party/scopus.svg)

## Skill Output:

**Output Type(s):** [shell commands, json, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Scopus connector actions return JSON data with execution metadata.]

## Skill Version(s):

1.0.2 (source: artifact frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
