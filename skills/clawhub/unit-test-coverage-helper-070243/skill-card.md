## Description: <br>
Helps software maintainers, QA engineers, open-source contributors, and product teams add useful unit tests and improve test coverage for existing codebases. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, QA engineers, maintainers, and product teams use this skill to plan, implement, and verify unit tests that protect existing behavior and raise coverage. It is most useful when a codebase needs a practical testing workflow, checklist, code change, or verification note. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad testing and quality triggers may activate the skill for adjacent requests where another testing workflow is more specific. <br>
Mitigation: Review or narrow trigger wording if precise routing is required. <br>
Risk: Generated test plans or code changes may not match the repository's actual behavior or testing conventions. <br>
Mitigation: Review proposed tests against local code, run the suggested verification commands, and keep assumptions visible. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/unit-test-coverage-helper-070243) <br>
- [Requirement plan](references/requirement-plan.md) <br>
- [Preventing LLM unit test spam](https://blog.larah.me/test-slop/) <br>
- [Skillgrade: Unit tests for your agent skills](https://github.com/mgechev/skillgrade) <br>
- [Writing Great Unit Tests: Best and Worst Practices](https://segmentfault.com/a/1190000009709754) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with optional code blocks, shell commands, checklists, and verification notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only helper; outputs are tailored to the user's codebase and constraints.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
