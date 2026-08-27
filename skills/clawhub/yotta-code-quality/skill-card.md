## Description:

Pair-style code quality reviewer for agent-assisted code, PR, architecture, test, release-safety, and first-paint UX reviews using Iron Law findings and a 0-100 Health Score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to review code, diffs, pull requests, tests, architecture health, technical debt, and release readiness before merging or shipping. The skill is read-only by default and produces structured findings with symptoms, source, consequence, and remedy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can be installed globally across multiple agent environments, which may activate review behavior more broadly than intended.

Mitigation: Install it only into the agent environments where this review behavior is desired, and avoid the global installer when narrower availability is needed.

Risk: Optional fix mode, triage, history, AGENTS templates, and hooks can change workflow behavior beyond read-only review.

Mitigation: Enable optional behavior only intentionally and review proposed remedies before applying changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-code-quality)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-code-quality)
- [Repository](https://github.com/YottaMeta/yotta-code-quality)
- [Common review configuration and report template](references/common.md)
- [Production decay risks](references/decay-risks.md)
- [Test decay risks](references/test-decay-risks.md)
- [Release and first-paint review extensions](references/editorial-extensions.md)
- [Source coverage matrix](references/source-coverage.md)
- [PR review guide](references/pr-review-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown review reports with structured findings, health score summaries, and optional configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are read-only by default; code edits, triage, history, AGENTS templates, and hooks are opt-in.]

## Skill Version(s):

0.3.3 (source: SKILL.md frontmatter, package.json, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
