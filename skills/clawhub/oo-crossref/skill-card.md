## Description:

Crossref (crossref.org). Use this skill for Crossref search, metadata retrieval, DOI agency lookup, citation export, resource listing, and bibliographic reference matching through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Crossref records, retrieve DOI and collection metadata, export citations, and match bibliographic references without constructing direct Crossref API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded shell or PowerShell scripts without local verification.

Mitigation: Do not allow agents to run installer commands automatically; install the oo CLI from a verified, versioned source with checksum or signature validation.

Risk: Crossref requests are routed through OOMOL rather than direct public Crossref API access.

Mitigation: Use this skill only when the user intentionally wants requests handled through an OOMOL-connected account and server-side credential injection.

Risk: Authentication, connection, and billing setup steps can change account state or expose users to unexpected service dependencies.

Mitigation: Run login, connection, or billing steps only after a matching command failure and with explicit user intent.

## Reference(s):

- [Crossref homepage](https://www.crossref.org/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-crossref)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect live connector schemas before constructing Crossref action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
