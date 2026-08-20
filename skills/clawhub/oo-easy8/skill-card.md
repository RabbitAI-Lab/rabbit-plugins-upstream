## Description:

Easy8 lets an agent read, create, update, and delete Easy8 projects and tasks through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers with an OOMOL-connected Easy8 account use this skill to inspect Easy8 connector schemas and operate supported project and task actions from an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify Easy8 data through write actions.

Mitigation: Confirm the exact payload and expected effect with the user before running create or update actions.

Risk: The skill can permanently delete Easy8 tasks through a destructive action.

Mitigation: Require explicit user approval for the target task before running delete actions.

Risk: The skill depends on an authenticated oo CLI and an OOMOL-connected Easy8 account.

Mitigation: Install and authenticate the oo CLI only from trusted sources, and use setup or connection flows only when an action fails for that reason.

## Reference(s):

- [ClawHub Easy8 Skill](https://clawhub.ai/oomol/skills/oo-easy8)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Easy8 Homepage](https://www.easy8.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include Easy8 connector action results with data and execution metadata.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
