## Description:

Helps agents plan, implement, and verify useful unit tests and coverage improvements for existing codebases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, software maintainers, QA engineers, open-source contributors, and product teams use this skill to create repeatable workflows for adding meaningful unit tests, raising coverage, and checking changes against regression risk.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation wording may cause the skill to be invoked for general testing or quality requests.

Mitigation: Confirm the user wants unit-test coverage planning or implementation before making broad code changes.

Risk: Generated testing recommendations or edits can introduce incorrect assumptions in large or sensitive repositories.

Mitigation: Review proposed tests and run the repository's normal verification commands before accepting changes.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/unit-test-coverage-helper)
- [GitHub issue: ORG-002 - Build local Commander Runner](https://github.com/haitao5867gg-cpu/LandlordEasy/issues/17)
- [GitHub issue: targeted tests while iterating](https://github.com/benmarte/talos/issues/195)
- [Hacker News: User-guide-driven development with coding agents](https://news.ycombinator.com/item?id=49579372)
- [Writing Great Unit Tests: Best and Worst Practices](https://segmentfault.com/a/1190000009709754)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with optional code blocks and verification commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include checklists, implementation steps, assumptions, limits, and follow-up risks.]

## Skill Version(s):

0.20260908.51704 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
