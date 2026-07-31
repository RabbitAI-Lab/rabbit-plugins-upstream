## Description: <br>
Generates phased, dependency-ordered implementation tasks from specifications after the specification is complete and before implementation begins. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to convert completed specifications and implementation plans into phased task lists with explicit dependencies, file coordination, parallelization markers, and completion criteria. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger terms may activate the skill in general planning or implementation discussions. <br>
Mitigation: Confirm the user is asking for implementation task planning from a completed specification before applying the generated breakdown. <br>
Risk: Generated task plans may contain incorrect sequencing, unsafe parallelization, or incomplete file coordination. <br>
Mitigation: Review dependencies, same-file edits, parallel markers, and completion criteria before executing the plan. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-spec-kit-task-planning) <br>
- [OpenClaw homepage metadata](https://github.com/athola/claude-night-market/tree/master/plugins/spec-kit) <br>
- [Task phase structure](artifact/modules/phase-structure.md) <br>
- [Task dependency patterns](artifact/modules/dependency-patterns.md) <br>
- [Technology stack patterns](artifact/modules/tech-stack-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown task plan with phased task entries, dependency fields, affected files, and verification criteria] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May mark parallelizable tasks with [P] and include concrete file paths, configuration suggestions, and verification commands.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter is 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
