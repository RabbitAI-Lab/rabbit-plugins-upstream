## Description: <br>
Track action items and coordination signals for the community, including quick task creation, status checks, and handoff notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[crimsondevil333333](https://clawhub.ai/user/crimsondevil333333) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to track community action items, inspect task status, and record handoff notes in a local JSON task file. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill creates or updates a local JSON task file, so an incorrect custom data path could modify an unintended workspace file. <br>
Mitigation: Confirm the data path before running the helper and use a dedicated task file for shared collaboration state. <br>


## Reference(s): <br>
- [Collaboration Helper reference](references/collaboration-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/crimsondevil333333/skills/collaboration-helper) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON task records] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can create or update a local tasks.json file when the helper is executed.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
