## Description: <br>
Initialize a memory bank for a new or existing project following the v6.12 protocol. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[space-cadet](https://clawhub.ai/user/space-cadet) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and project maintainers use this skill to initialize project-local memory-bank documentation, task tracking files, and optional first-task scaffolding for new or existing projects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill creates memory-bank files in the selected project. <br>
Mitigation: Confirm the target project root before use and review the generated files before committing them. <br>
Risk: The skill can propose an optional git commit after initialization. <br>
Mitigation: Review the staged changes and commit message before allowing the commit. <br>
Risk: Referenced follow-on workflow files are not bundled in this artifact. <br>
Mitigation: Review any separately installed follow-on workflow skills before using them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/space-cadet/skills/mb-init) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown instructions with inline shell commands and file templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates project-local memory-bank documentation templates and may propose an optional git commit.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
