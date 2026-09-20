## Description:

Pair-style code quality reviewer for code, PR, test, architecture, release-safety, and first-paint UX reviews using Iron Law findings and a 0-100 Health Score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to review code, pull requests, tests, architecture, technical debt, release readiness, and first-paint UX. It produces concise findings with symptoms, sources, consequences, remedies, severity, and a per-review Health Score.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can auto-trigger conversational code-review behavior in agents where it is installed.

Mitigation: Install it only in agents where that review behavior is desired, and review optional AGENTS templates, hooks, and history settings before enabling them.

Risk: Unpinned installer commands can fetch newer package contents than the reviewed release.

Mitigation: For higher-assurance environments, pin the npm package version instead of using unpinned latest-style install commands.

Risk: Review findings and remedies may be incomplete or incorrect for the local codebase context.

Mitigation: Treat the output as review guidance, verify findings against the scoped code, and require explicit user approval before applying fixes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-code-quality)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-code-quality)
- [Skill homepage](https://github.com/YottaMeta/yotta-code-quality)
- [Shared framework](references/common.md)
- [Production decay risks](references/decay-risks.md)
- [Test decay risks](references/test-decay-risks.md)
- [Editorial extensions](references/editorial-extensions.md)
- [PR review guide](references/pr-review-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, code, configuration]

**Output Format:** [Markdown review report with structured findings, severity tiers, remedies, summary, and optional configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report-only by default; code edits occur only when the user explicitly asks for fix mode.]

## Skill Version(s):

0.4.1 (source: server release evidence, SKILL.md frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
