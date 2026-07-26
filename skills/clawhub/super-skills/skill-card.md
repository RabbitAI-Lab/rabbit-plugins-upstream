## Description: <br>
Decomposes complex user requests into executable subtasks, identifies required capabilities, searches for existing skills at skills.sh, and creates new skills when no solution exists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[10e9928a](https://clawhub.ai/user/10e9928a) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to break complex workflow requests into actionable subtasks, map each subtask to required capabilities, find suitable skills, and plan any new skill creation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can recommend installing or creating third-party skills that change agent behavior. <br>
Mitigation: Review each recommended skill source and SKILL.md before approving installation or creation. <br>
Risk: Task decomposition or execution plans may be incomplete, incorrect, or misleading for the user's workflow. <br>
Mitigation: Validate subtasks, dependencies, commands, and generated skill files before relying on the plan. <br>
Risk: Searching or using third-party services may expose private information if sensitive inputs are included. <br>
Mitigation: Avoid sending private documents or secrets to third-party services unless their data handling is understood. <br>


## Reference(s): <br>
- [Universal Capability Types Reference](references/capability_types.md) <br>
- [skills.sh](https://skills.sh/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with structured task lists, YAML-style execution plans, shell commands, and skill file templates.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May recommend skills to install or create; skill creation requires user confirmation before proceeding.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
