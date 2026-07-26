## Description: <br>
Validates documentation usability by spawning context-free agents to complete tasks using only the docs, identifying gaps for improvement. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zscole](https://clawhub.ai/user/zscole) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, technical writers, and documentation maintainers use this skill to test whether documentation lets a fresh tester complete a task and to identify concrete gaps to fix. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Testing may share bundled documentation with a spawned tester session. <br>
Mitigation: Use the skill only with documentation that is appropriate to share with that session, and keep sensitive or unnecessary material out of the test bundle. <br>
Risk: Tester output is a literal gap report and may not reflect the intended product behavior. <br>
Mitigation: Review gap reports before applying changes and verify documentation fixes against the source project. <br>


## Reference(s): <br>
- [RTFM Testing on ClawHub](https://clawhub.ai/zscole/skills/rtfm-testing) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown gap reports and concise guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include tester prompts, execution logs, gap categories, and remediation suggestions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
