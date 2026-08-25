## Description:

PlanetScale (planetscale.com). Use this skill for ANY PlanetScale request: reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage PlanetScale organizations, databases, and branches through an OOMOL-connected account. It supports listing and retrieving resources, creating databases and branches, and deleting databases or branches after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can create PlanetScale databases or branches with user-provided payloads.

Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged as write.

Risk: Destructive actions can delete PlanetScale databases or branches.

Mitigation: Require explicit approval for the specific deletion target before running destructive actions.

Risk: The connected OOMOL service token may grant access beyond the intended PlanetScale resources.

Mitigation: Use only the scopes needed for the intended workflow and review scope or connection errors before retrying.

## Reference(s):

- [PlanetScale homepage](https://planetscale.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-planetscale)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; action responses are JSON when run with --json.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
