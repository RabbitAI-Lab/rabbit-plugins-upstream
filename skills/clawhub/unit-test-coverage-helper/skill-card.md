## Description:

Helps software teams add useful unit tests, improve test coverage, and produce practical workflows, checklists, analysis, implementation support, and verification notes for existing codebases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, software maintainers, QA engineers, open-source contributors, and product teams use this skill to plan and add regression-focused unit tests, raise coverage, and document how the result was verified.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad implicit activation may trigger the skill during unrelated developer conversations about testing.

Mitigation: Review and narrow implicit triggers or invocation policy before deployment when tighter routing is required.

Risk: Generated unit tests or coverage plans may miss project-specific behavior when repository context is incomplete.

Mitigation: Require the agent to restate assumptions, inspect available constraints, and provide verification commands for code changes.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [Coding Agents killed my identity. How do you feel?](https://news.ycombinator.com/item?id=49389408)
- [We had a unit test once which only failed on Sundays (2015)](https://qntm.org/unit)
- [Writing Great Unit Tests: Best and Worst Practices](https://segmentfault.com/a/1190000009709754)
- [Scaffold Dramula parseSeries Strategy](https://github.com/titanaprilian/private-movie/issues/243)
- [SQA V2 Meta: Unit Tests for Test Utilities, Factories & Mock Handlers](https://github.com/arslan9024/White-Caves/issues/2327)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with optional code blocks, shell commands, checklists, and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tailored to the user's repository context, constraints, assumptions, and success criteria.]

## Skill Version(s):

0.20260830.92238 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
