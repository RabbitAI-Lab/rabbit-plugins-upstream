## Description: <br>
Helps software maintainers, QA engineers, contributors, and product teams add useful unit tests and raise coverage for existing codebases through a repeatable, locally feasible workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, QA engineers, maintainers, and product teams use this skill to plan or implement practical unit-test and coverage improvements for existing codebases. It helps clarify constraints, propose test and verification steps, produce checklists or code changes, and call out remaining risks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can auto-run for broad testing or regression terms, which may trigger when the user did not intend a coverage workflow. <br>
Mitigation: Narrow implicit invocation to explicit unit-test, coverage, or regression-test requests before installation or deployment. <br>
Risk: Generated test plans or code changes may miss project-specific behavior or introduce brittle assertions. <br>
Mitigation: Review proposed tests against project requirements and run the repository's normal test and coverage commands before merging. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/unit-test-coverage-helper) <br>
- [[Campaign] Daily documentation quality and repair](https://github.com/equinor/neqsim/issues/2499) <br>
- [Add notifications and action-items dashboard workflow](https://github.com/fderuiter/cadence-clinical/issues/382) <br>
- [Writing Great Unit Tests: Best and Worst Practices](https://segmentfault.com/a/1190000009709754) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with optional code, command, checklist, and verification sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are tailored to the user's codebase and should include assumptions, limits, and verification notes when relevant.] <br>

## Skill Version(s): <br>
0.20260730.10356 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
