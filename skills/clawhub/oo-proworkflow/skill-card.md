## Description:

Helps agents read and update ProWorkflow projects and items through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams using ProWorkflow can ask an agent to retrieve, search, and update projects or project items through their connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the suggested pipe-to-shell CLI installer can execute unreviewed code.

Mitigation: Review the installer source or follow the official installation guide before running setup commands.

Risk: Updating a project or item can change ProWorkflow data unexpectedly.

Mitigation: Inspect the live action schema and confirm the exact update payload and effect with the user before execution.

## Reference(s):

- [ProWorkflow skill on ClawHub](https://clawhub.ai/oomol/skills/oo-proworkflow)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)
- [ProWorkflow](https://www.proworkflow.com/)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Natural-language responses and JSON action results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads projects and items; updates require user confirmation.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
