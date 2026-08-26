## Description:

Helps software teams add useful unit tests, raise coverage, and validate changes with practical workflows, checklists, analysis, code changes, and verification guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, maintainers, open-source contributors, and product teams use this skill to plan or implement unit tests, improve test coverage, and check that code changes preserve expected behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate for broad testing or quality-related requests where the user did not intend to use a unit-test workflow helper.

Mitigation: Invoke it intentionally for unit test or coverage work, and review generated test plans, code changes, and verification commands before applying them.

Risk: Generated tests or coverage plans can miss project-specific behavior or encode incorrect assumptions.

Mitigation: Validate outputs against the repository's existing test conventions, run the suggested verification commands, and keep assumptions and remaining risks visible in the final response.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [Writing Great Unit Tests: Best and Worst Practices](https://segmentfault.com/a/1190000009709754)
- [We had a unit test once which only failed on Sundays](https://qntm.org/unit)
- [Spend Missing Merchant regression issue](https://github.com/Expensify/App/issues/99500)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with optional code blocks, shell commands, checklists, and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompt-only helper; outputs should state assumptions, limits, required inputs, checks performed, and remaining follow-up work when relevant.]

## Skill Version(s):

0.20260826.40329 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
