## Description: <br>
Delegates coding tasks from an agent to a local code CLI so developers can run asynchronous implementation, debugging, and independent test-verification workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to delegate scoped code-writing, bug-fixing, and test-verification tasks to a local CLI while keeping the primary agent responsive. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill recommends running a local coding CLI with permission bypass for automatic file edits. <br>
Mitigation: Remove permission-bypass flags from examples and workflows, and require explicit approval before delegated CLI tasks edit files. <br>
Risk: Delegated CLI tasks can use an authenticated local session in the selected project directory. <br>
Mitigation: Run the skill only in a disposable or clearly scoped project directory, verify the working directory before execution, and avoid repositories containing sensitive data. <br>
Risk: Asynchronous delegation can produce code or test results that are not immediately reviewed by the primary agent. <br>
Mitigation: Poll delegated sessions, review outputs before relying on them, and run independent verification before accepting generated changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/code-delegate-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and structured status/result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include delegated CLI session status, execution logs, generated code changes, test results, and retry guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
