## Description: <br>
Software implementation planning with file-based persistence (.plan/) for code changes touching three or more files or with ambiguous scope. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to turn ambiguous or multi-file software implementation work into concrete, file-backed plans with scoped phases, verification steps, and execution handoff choices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated plans may steer later implementation work in the wrong direction if the goal, scope, or verification criteria are weak. <br>
Mitigation: Review the generated plan before execution and confirm the goal, scope boundaries, success thresholds, and handoff choice. <br>
Risk: The planning scaffold writes local .plan/ files and may update .gitignore in the active project. <br>
Mitigation: Use the skill only in projects where local planning files are expected, and inspect generated file changes before committing or handing off execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-planning) <br>
- [Execution & Decomposition Patterns](references/execution-and-methodology.md) <br>
- [Operational Patterns](references/operational-patterns.md) <br>
- [Plan Deepening](references/plan-deepening.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown plans, checklists, and inline bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create .plan/ working files and update .gitignore when the planning scaffold is used.] <br>

## Skill Version(s): <br>
4.3.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
