## Description: <br>
Decomposes complex user requests into executable subtasks, identifies required capabilities, searches for existing skills at skills.sh, and creates new skills when no solution exists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[10e9928a](https://clawhub.ai/user/10e9928a) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to break complex workflow requests into executable subtasks, map each task to required capabilities, search for existing skills, and draft new skills when a gap remains. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can steer an agent toward global, noninteractive skill installation or new skill creation. <br>
Mitigation: Require explicit user review before installation or creation, inspect proposed skill source, and avoid noninteractive global `-g -y` installs unless the user accepts that scope. <br>
Risk: Execution plans and generated skill drafts may contain incorrect or misleading guidance. <br>
Mitigation: Review the proposed plan, dependencies, commands, and generated skill content before using them in a workflow. <br>
Risk: Workflow plans may involve credentials, scheduled jobs, or external service changes. <br>
Mitigation: Confirm credentials, scheduling behavior, and rollback or removal steps before enabling the workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/10e9928a/skills/task-decomposer) <br>
- [skills.sh](https://skills.sh/) <br>
- [Universal Capability Types Reference](references/capability_types.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with structured task lists, capability mappings, shell commands, and skill templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include proposed installations, new skill drafts, execution plans, and verification steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
