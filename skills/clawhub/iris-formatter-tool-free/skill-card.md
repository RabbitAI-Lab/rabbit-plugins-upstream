## Description: <br>
Provides InterSystems IRIS/ObjectScript code formatting, style review, and basic standards checks for naming, locks, transactions, formatting, and comments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers working with InterSystems IRIS or Cache use this skill to format ObjectScript, review code against basic project conventions, and receive suggested fixes for naming, lock, transaction, formatting, and comment issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill declares read, exec, and write capabilities, so formatting or validation work could affect local project files or run commands if the agent is allowed to proceed. <br>
Mitigation: Keep use scoped to intended project files, review proposed edits before applying them, and allow command execution only when compile or environment validation is explicitly needed. <br>
Risk: ObjectScript formatting and review recommendations may not match every team's IRIS conventions or business-specific constraints. <br>
Mitigation: Treat review output as guidance, confirm changes against local standards, and validate important code in the target IRIS environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/iris-formatter-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with ObjectScript code blocks and optional JSON summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose edits, IRIS compile validation, or environment checks when explicitly requested; review before applying changes.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
