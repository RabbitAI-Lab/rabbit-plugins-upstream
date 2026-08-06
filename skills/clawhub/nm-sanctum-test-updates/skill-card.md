## Description: <br>
Updates, generates, and validates tests using git-workspace context and TDD/BDD methodology. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to discover test gaps, generate or update pytest-oriented tests, and validate test quality after code changes. It is intended for test maintenance, TDD/BDD workflows, refactoring support, and CI-oriented quality checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may lead an agent to scan repository contents, create or edit tests, and run pytest or mutation-testing workflows with workspace side effects. <br>
Mitigation: Use targeted paths where possible, review proposed file changes before accepting them, and run validation in trusted repositories or disposable worktrees/containers when side effects matter. <br>
Risk: Generated tests or test-maintenance guidance can be incorrect, brittle, or misaligned with intended design invariants. <br>
Mitigation: Review generated tests, preserve human review for invariant changes, and verify results with the repository's normal test and quality gates. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-test-updates) <br>
- [Project homepage from ClawHub metadata](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and example test code; referenced workflows may also describe JSON report output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can propose targeted test updates, generated test scaffolding, validation steps, and quality-review findings for repository paths.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
