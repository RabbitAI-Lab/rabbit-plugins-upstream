## Description:

OpenPageRank lets an agent look up OpenPageRank scores for one or more domains through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect the OpenPageRank connector schema and run read-only PageRank lookups for domains through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup commands execute remote installer scripts downloaded at runtime.

Mitigation: Prefer a verified, pinned, or package-manager installation of the oo CLI and avoid running installer scripts from an elevated shell.

Risk: Authentication, connection, or billing failures can interrupt OpenPageRank lookups.

Mitigation: Run setup only after a matching command failure and follow the documented recovery path for sign-in, OpenPageRank connection, or billing.

## Reference(s):

- [OpenPageRank homepage](https://openpagerank.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OpenPageRank skill on ClawHub](https://clawhub.ai/oomol/skills/oo-openpagerank)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts the agent to inspect the live action schema before submitting an OpenPageRank lookup payload.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
