## Description:

Pair-style code quality reviewer that diagnoses production, test, release-safety, and first-paint UX risks using Iron Law findings and a 0-100 Health Score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to review code, pull requests, architecture changes, test quality, technical debt, and release readiness before merging or shipping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional installers can copy the skill into multiple agent skill folders or overwrite an existing yotta-code-quality target folder.

Mitigation: Install only into intended skill directories, prefer an explicit --agent or --dir target, and avoid broad or shared directories.

Risk: Review findings and remedy guidance may be inaccurate or mis-scoped if the agent applies the skill without respecting the requested files, diff, or project configuration.

Mitigation: Keep the default report-only posture, apply .code-quality.yaml when present, and require explicit user approval before making code edits.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-code-quality)
- [npm Package](https://www.npmjs.com/package/@yottameta/yotta-code-quality)
- [Code Quality Reviewer Shared Framework](references/common.md)
- [Decay Risk Reference](references/decay-risks.md)
- [Test Decay Risk Reference](references/test-decay-risks.md)
- [Editorial Extensions](references/editorial-extensions.md)
- [PR Review Guide](references/pr-review-guide.md)
- [Source Coverage Matrix](references/source-coverage.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance, Configuration]

**Output Format:** [Markdown review report with findings, Health Score, summary, and optional remedy guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report-only by default; code edits are produced only when explicitly requested.]

## Skill Version(s):

0.3.2 (source: SKILL.md frontmatter, package.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
