## Description:

Reviews code, pull requests, tests, and release readiness for maintainability risks, with evidence-based findings and a per-review health score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to review scoped code, diffs, tests, or architecture for quality risks and actionable remedies before merging or releasing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned package installation can make a later installation differ from the reviewed release.

Mitigation: Pin the npm version or use a reviewed tarball when repeatable installation matters.

Risk: Global installation or optional integrations can apply review behavior more broadly or persistently than intended.

Mitigation: Choose a single target with --agent or --dir; enable hooks, history tracking, and the AGENTS template only when needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yottameta/skills/yotta-code-quality)
- [Project homepage (listed in ClawHub metadata)](https://github.com/YottaMeta/yotta-code-quality)
- [Review framework and report format](artifact/references/common.md)
- [PR review guide](artifact/references/pr-review-guide.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Code]

**Output Format:** [Markdown review report; optional code edits when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings follow Symptom → Source → Consequence → Remedy and include a 0–100 per-review deduction index; reports do not change code by default.]

## Skill Version(s):

0.4.3 (source: ClawHub release, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
