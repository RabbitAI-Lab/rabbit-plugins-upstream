## Description:

Operate CrateDB Cloud through an OOMOL-connected account for reading users, organizations, projects, clusters, products, and regions via the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect CrateDB Cloud account resources through an OOMOL-connected account without handling raw credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may encourage running unverified remote installer scripts directly in a shell.

Mitigation: Review the installer path before installing and prefer a trusted, versioned oo CLI source with checksum or signature verification.

Risk: The connected CrateDB Cloud account can expose readable account resources through OOMOL's connector.

Mitigation: Connect only a CrateDB Cloud account whose read access is appropriate for the intended users and workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cratedb-cloud)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [CrateDB Cloud](https://cratedb.com/database/cloud)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration guidance, Text]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
