## Description:

LogSnag connects an agent to LogSnag through the OOMOL oo CLI for reading, creating, and updating LogSnag data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to publish LogSnag events, update user profile properties, and publish or mutate numeric insights from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path asks users to run remote installer scripts for the oo CLI.

Mitigation: Install the oo CLI through a verifiable package manager when possible, or inspect and verify the installer script before running it.

Risk: Write actions can change LogSnag events, user properties, or numeric insights.

Mitigation: Fetch the live action schema and confirm the exact payload and effect with the user before running write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-logsnag)
- [LogSnag homepage](https://logsnag.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector actions; write actions require payload confirmation.]

## Skill Version(s):

1.0.4 (source: evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
