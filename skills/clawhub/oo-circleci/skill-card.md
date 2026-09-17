## Description:

CircleCI (circleci.com). Use this skill for ANY CircleCI request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect CircleCI projects, pipelines, workflows, jobs, artifacts, user data, environment variables, and Insights metrics through an OOMOL-connected account. It also supports triggering CircleCI project pipelines after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes a fallback installer path that can execute an unverified remote installer.

Mitigation: Review the skill before installing, and install the oo CLI only through a verified, user-approved process instead of allowing an agent to run installer commands automatically.

Risk: The trigger_pipeline action can change CircleCI state.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub CircleCI Skill](https://clawhub.ai/oomol/skills/oo-circleci)
- [CircleCI](https://circleci.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include CircleCI connector response data and execution metadata returned by the oo CLI.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
