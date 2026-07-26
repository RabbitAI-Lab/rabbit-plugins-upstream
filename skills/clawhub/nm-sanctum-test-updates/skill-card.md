## Description: <br>
Updates, generates, and validates tests using git-workspace context and TDD/BDD methodology. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to discover test gaps, generate or update test scaffolding, apply TDD/BDD patterns, and validate test quality after code or execution-markdown changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may inspect repository code and propose generated or edited tests. <br>
Mitigation: Review proposed changes before keeping them and scope agent access to the intended workspace. <br>
Risk: Validation workflows may run tests or shell commands from the target project. <br>
Mitigation: Run untrusted tests in an isolated workspace when possible and approve commands before execution. <br>
Risk: Generated tests can initially fail by design under the TDD workflow. <br>
Mitigation: Confirm failures are expected RED-phase failures, then complete implementation and rerun validation before merging. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-test-updates) <br>
- [Original plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline code blocks and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose generated or edited tests, validation commands, quality checklists, and review guidance for developer approval.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
