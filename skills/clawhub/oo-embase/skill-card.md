## Description:

Embase helps agents search biomedical literature and retrieve article records through an OOMOL-connected Elsevier Embase account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers with an OOMOL-connected Embase account use this skill to search biomedical literature and retrieve article records from Embase.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Embase requests are brokered through OOMOL using an OOMOL-connected account.

Mitigation: Review the OOMOL CLI installation and account connection steps before first use, and connect only accounts you are comfortable using through OOMOL.

Risk: Authentication, connection, scope, or billing failures can block Embase actions.

Mitigation: Run setup, reconnection, or billing steps only after the connector command fails with the matching error.

## Reference(s):

- [ClawHub Embase Skill](https://clawhub.ai/oomol/skills/oo-embase)
- [Embase Product Page](https://www.elsevier.com/products/embase)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before each Embase action; connector responses include data and meta.executionId.]

## Skill Version(s):

1.0.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
