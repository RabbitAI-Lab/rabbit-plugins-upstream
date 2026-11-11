## Description:

Adds an experience-inheritance workflow for coding agents: recall validated fixes, record when they help, and save new fixes after non-obvious failures, with optional experiments to measure the effect.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using coding agents use Pi EvoX Loop to retrieve reusable fixes across tasks and save newly learned fixes for later runs. They can also run controlled experiments to measure the effect of recalled fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stored fixes and approval or sharing settings can affect later agent runs and data handling.

Mitigation: Review approval and sharing behavior, and avoid relying on automatically approved stored fixes.

Risk: The security scan could not fully inspect some content, so unreported behavior remains uncertain.

Mitigation: Inspect the relevant files before installing and enabling the skill.

Risk: An optional integration was flagged in the dependency scan.

Mitigation: Check whether the optional integration is needed and review it before enabling it.

## Reference(s):

- [Pi EvoX Loop on ClawHub](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Pi coding agent](https://github.com/earendil-works/pi)
- [EvoMap Evolver](https://github.com/EvoMap/evolver)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Code, JSON]

**Output Format:** [Markdown guidance and shell commands, with optional code fixes and structured gene records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can inject reviewed fixes into agent context and save gene records and experiment outputs locally.]

## Skill Version(s):

0.40.0 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
