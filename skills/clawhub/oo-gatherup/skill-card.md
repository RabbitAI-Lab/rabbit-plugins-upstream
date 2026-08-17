## Description:

GatherUp (gatherup.com). Use this skill for ANY GatherUp request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve GatherUp business locations and customers through an OOMOL-connected account. It supports schema-first execution of read-only GatherUp actions through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GatherUp customer and business data can be sensitive even when accessed through read-only actions.

Mitigation: Use the skill only with an intended OOMOL-connected GatherUp account, inspect action schemas before execution, and avoid exposing returned customer or business data unnecessarily.

Risk: First-time authentication or connection steps can authorize access to a GatherUp account.

Mitigation: Run oo CLI login or GatherUp connection steps only after an auth or connection failure and only when the user intends to use the integration.

## Reference(s):

- [GatherUp homepage](https://gatherup.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gatherup)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector commands that return JSON responses from GatherUp actions.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
