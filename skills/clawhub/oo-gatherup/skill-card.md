## Description:

GatherUp (gatherup.com). Use this skill for searching and reading GatherUp business and customer data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve GatherUp business locations and customers from an OOMOL-connected GatherUp account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes unverified remote installer commands for the oo CLI.

Mitigation: Review the installer before execution, install the oo CLI through a verified method, and avoid elevated shells unless required.

Risk: The security verdict recommends review before installing this connector skill.

Mitigation: Use the skill only for the listed read operations unless the publisher documents additional actions.

## Reference(s):

- [GatherUp skill page](https://clawhub.ai/oomol/skills/oo-gatherup)
- [GatherUp homepage](https://gatherup.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running GatherUp actions; responses include data and an execution id.]

## Skill Version(s):

1.0.2 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
