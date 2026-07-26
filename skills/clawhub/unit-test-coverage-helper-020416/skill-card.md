## Description: <br>
Helps developers improve unit test coverage by identifying gaps and suggesting focused tests, code snippets, and commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineering teams use this skill to inspect unit test coverage, prioritize missing cases, and draft tests or commands that improve confidence in code changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Suggested tests can overfit implementation details or miss important behavior. <br>
Mitigation: Review proposed tests against the intended behavior and run the full relevant test suite before relying on them. <br>
Risk: Suggested shell commands or configuration changes may not match the local project tooling. <br>
Mitigation: Inspect commands and diffs before execution, then apply them in a clean branch or disposable workspace. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with inline code and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include proposed test files, coverage commands, configuration adjustments, and review notes.] <br>

## Skill Version(s): <br>
0.1.0 (source: target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
