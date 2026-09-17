## Description:

Buildium helps agents inspect live OOMOL connector schemas and retrieve Buildium rental owners, properties, units, and property notes through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to look up Buildium rental owners, properties, units, and property notes through the OOMOL Buildium connector. It is suited for read-oriented property management data retrieval after the oo CLI is installed, signed in, and connected to Buildium.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Buildium request details and returned records are routed through OOMOL.

Mitigation: Install only when that routing is acceptable for the data involved, and limit connected Buildium scopes to the intended read actions.

Risk: The artifact documents remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Prefer a signed or checksum-verified installation path before installing the oo CLI.

## Reference(s):

- [ClawHub Buildium skill page](https://clawhub.ai/oomol/skills/oo-buildium)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Buildium homepage](https://www.buildium.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed oo CLI, OOMOL sign-in, and a connected Buildium account; listed actions are read-only get and list operations.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
