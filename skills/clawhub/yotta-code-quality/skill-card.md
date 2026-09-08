## Description:

A pair-style code review skill that diagnoses production, test, release-safety, and first-paint UX risks using Iron Law findings and a 0-100 Health Score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to review code, PRs, tests, architecture, technical debt, and release readiness with structured findings and evidence-based remedies. It is report-only by default and can apply fixes only when the user explicitly opts in.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer scripts can copy the skill into user-level or project-level agent skill directories, including a multi-agent global install option.

Mitigation: Install only trusted, preferably pinned package versions, choose a specific agent or directory when possible, and use the global option only when broad installation is intended.

Risk: Opt-in fix, triage, history, and hook features can write files or alter agent behavior.

Mitigation: Keep the default report-only workflow unless file changes are explicitly desired, and review generated edits, suppressions, history files, and hook configuration before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-code-quality)
- [README](README.md)
- [Shared framework](references/common.md)
- [Production decay risks](references/decay-risks.md)
- [Test decay risks](references/test-decay-risks.md)
- [Editorial extensions](references/editorial-extensions.md)
- [PR review guide](references/pr-review-guide.md)
- [Source coverage](references/source-coverage.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown review reports with structured findings, optional code edits, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a per-run Health Score and report-only findings by default; fix, triage, history, and hooks are opt-in.]

## Skill Version(s):

0.3.5 (source: server release metadata; artifact frontmatter, package.json, and changelog list 0.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
