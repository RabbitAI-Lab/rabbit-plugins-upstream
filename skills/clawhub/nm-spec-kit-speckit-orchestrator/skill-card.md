## Description:

Orchestrates Spec Driven Development by coordinating spec, plan, and task skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to coordinate Spec Driven Development sessions across specification, planning, task generation, implementation, and verification. It helps load the appropriate companion skills, track progress, and keep spec.md, plan.md, tasks.md, and related .specify artifacts aligned.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on generic planning or specification language.

Mitigation: Use it in Speckit-enabled repositories where reading and updating spec.md, plan.md, tasks.md, and .specify memory files is intended.

Risk: Workflow guidance can affect core planning artifacts such as spec.md, plan.md, tasks.md, and .specify memory files.

Mitigation: Review proposed artifact changes and keep progress tracking aligned with the active Speckit command before continuing to implementation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-spec-kit-speckit-orchestrator)
- [ClawHub publisher profile](https://clawhub.ai/user/athola)
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/spec-kit)
- [Artifact structure](artifact/modules/artifact-structure.md)
- [Command-skill matrix](artifact/modules/command-skill-matrix.md)
- [Progress tracking](artifact/modules/progress-tracking.md)
- [Writing-plans extensions](artifact/modules/writing-plans-extensions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with command examples and structured artifact templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Coordinates workflow state and artifact expectations; does not define external API calls or credential handling.]

## Skill Version(s):

1.9.19 (source: release evidence; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
