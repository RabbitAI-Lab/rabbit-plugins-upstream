## Description:

Pair-style code quality reviewer that diagnoses production, test, release-safety, and first-paint UX risks using Iron Law findings and a 0-100 Health Score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to review code, pull requests, architecture, test quality, technical debt, and release readiness. It produces scoped findings with symptoms, sources, consequences, remedies, severity, and a per-run Health Score.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad conversational triggers could activate code-quality review in sensitive repositories or when the intended scope is unclear.

Mitigation: Prefer direct invocation or explicit file, diff, or repository scope when reviewing sensitive work.

Risk: Optional extras such as --fix, history tracking, AGENTS-template installation, hooks.json, or all-agent installation can change code or agent behavior if enabled unintentionally.

Mitigation: Keep the default report-only posture unless the user intentionally enables fixes or installation extras.

Risk: Review guidance can be incorrect or incomplete when the agent lacks enough code context.

Mitigation: Treat findings as review proposals and confirm the referenced source, consequence, and remedy before applying changes.

## Reference(s):

- [README](README.md)
- [Chinese README](README.zh-CN.md)
- [Shared Framework](references/common.md)
- [Production Decay Risk Reference](references/decay-risks.md)
- [Test Decay Risk Reference](references/test-decay-risks.md)
- [Editorial Extensions](references/editorial-extensions.md)
- [Source Coverage Matrix](references/source-coverage.md)
- [PR Review Guide](references/pr-review-guide.md)
- [Examples](references/examples.md)
- [AGENTS.md Drop-in Template](references/AGENTS-template.md)
- [Optional Safety Hooks](references/hooks.json)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, code, configuration]

**Output Format:** [Markdown review report with scoped findings, severity labels, Health Score, and concrete remedies; optional code or configuration changes only when explicitly requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report-only by default; language follows the user while fixed review labels and source names remain in English.]

## Skill Version(s):

0.3.4 (source: SKILL.md frontmatter, package.json, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
