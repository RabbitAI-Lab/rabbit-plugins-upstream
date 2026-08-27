## Description:

Helps software teams add useful unit tests and raise test coverage for existing codebases with a repeatable workflow, concrete artifacts, and verification notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, maintainers, and product teams use this skill to plan and implement targeted unit-test coverage improvements for existing codebases. It helps clarify constraints, propose local-friendly implementation steps, produce checklists or code changes, and identify verification commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The activation wording is mildly broad and may be invoked for general testing or quality requests where a narrower skill would fit better.

Mitigation: Confirm the user is asking for unit-test or coverage work before applying the workflow.

Risk: Coverage-focused work can encourage tests that increase metrics without protecting important behavior.

Mitigation: Prioritize tests around observable behavior, regressions, edge cases, and explicit success criteria before treating coverage percentage as the goal.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/unit-test-coverage-helper)
- [Writing Great Unit Tests: Best and Worst Practices](https://segmentfault.com/a/1190000009709754)
- [We had a unit test once which only failed on Sundays](https://qntm.org/unit)
- [Configurable Issue Implementation-Readiness Gate](https://github.com/accidental-hedge-fund/agent-pipeline/issues/1238)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with optional inline code blocks and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include checklists, workflows, implementation steps, code changes, and verification notes.]

## Skill Version(s):

0.20260827.40448 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
