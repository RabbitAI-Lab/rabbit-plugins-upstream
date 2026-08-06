## Description: <br>
Executes implementation plans with progress tracking, checkpoint validation, and quality gates after planning is complete and tasks are ready to implement. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill after project planning is complete to execute task lists, validate checkpoints, track progress, manage blockers, and report completion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad development triggers may activate the skill during casual coding or exploratory questions. <br>
Mitigation: Use it for planned implementation work after a concrete plan exists, and avoid invoking it for isolated or exploratory tasks. <br>
Risk: The workflow encourages local test and quality-gate commands that can be slow, fail in unprepared environments, or affect local project state. <br>
Mitigation: Review commands before execution and run them in the intended project environment with dependencies installed. <br>
Risk: The skill may guide agents to maintain project-local progress state such as `.attune/execution-state.json`. <br>
Mitigation: Confirm progress tracking files are appropriate for the repository and review them before committing or sharing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-project-execution) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline code, shell commands, JSON examples, and checklist-style reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents to update project-local progress state and run local test or quality-gate commands.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
