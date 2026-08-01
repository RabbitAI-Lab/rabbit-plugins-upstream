## Description: <br>
Orchestrates Spec Driven Development by coordinating spec, plan, and task skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to coordinate speckit-style specification, planning, task generation, implementation, and verification workflows across spec.md, plan.md, and tasks.md artifacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad triggers may activate the skill during ordinary planning discussions. <br>
Mitigation: Invoke it explicitly for speckit work and confirm the intended workflow phase before applying generated guidance or artifact changes. <br>
Risk: Incorrectly coordinated spec, plan, task, or checklist artifacts can mislead later implementation work. <br>
Mitigation: Review generated artifacts for consistency with the repository constitution and verify cross-artifact alignment before implementation. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/athola/skills/nm-spec-kit-speckit-orchestrator) <br>
- [Spec-kit plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/spec-kit) <br>
- [Artifact structure](modules/artifact-structure.md) <br>
- [Command-skill matrix](modules/command-skill-matrix.md) <br>
- [Progress tracking](modules/progress-tracking.md) <br>
- [Writing-plans extensions](modules/writing-plans-extensions.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with checklists, command mappings, progress items, and inline command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Coordinates spec.md, plan.md, tasks.md, checklists, and related spec-kit artifacts.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
