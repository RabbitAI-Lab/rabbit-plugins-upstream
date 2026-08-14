## Description:

Provides Scopus search and lookup workflows through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Scopus records and retrieve abstracts, authors, affiliations, documents, and source metadata from an OOMOL-connected Scopus account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and returned Scopus data pass through the OOMOL connector.

Mitigation: Install and use the skill only when the user intends to use an OOMOL-connected Scopus account for searches and lookups.

Risk: Unnecessary authentication, connection, or billing setup could affect the user's OOMOL or Scopus account state.

Mitigation: Run setup and login commands only after an auth, connection, scope, credential, app, or billing error indicates they are needed.

Risk: Incorrect action payloads could cause failed connector calls or misleading retrieval results.

Mitigation: Inspect the live connector schema before constructing each action payload.

## Reference(s):

- [Scopus homepage](https://www.scopus.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Scopus skill page](https://clawhub.ai/oomol/skills/oo-scopus)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON response references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building action payloads; Scopus connector responses include data and metadata.]

## Skill Version(s):

1.0.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
