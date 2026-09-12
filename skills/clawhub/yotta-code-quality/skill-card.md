## Description:

Pair-style code quality reviewer for agents that diagnoses production, test, release-safety, and first-paint UX risks using structured findings and a 0-100 review-index Health Score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to review code, pull requests, tests, architecture, technical debt, and release-readiness before merging or shipping. It produces diagnosis-first findings with concrete consequences and remedies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer behavior can overwrite or delete through unsafe destination paths or pre-existing yotta-code-quality symlinks.

Mitigation: Install only into a controlled skill directory, verify the source and version first, and ensure no unexpected yotta-code-quality symlink exists at the destination.

Risk: Global installation can persist the skill broadly across supported agent skill folders.

Mitigation: Prefer a pinned package version and a specific target directory unless broad user-level installation is intended.

## Reference(s):

- [Skill source](artifact/SKILL.md)
- [README](artifact/README.md)
- [Common review configuration and report template](artifact/references/common.md)
- [Production decay risks](artifact/references/decay-risks.md)
- [Test decay risks](artifact/references/test-decay-risks.md)
- [Release and UX review extensions](artifact/references/editorial-extensions.md)
- [PR review guide](artifact/references/pr-review-guide.md)
- [Source coverage matrix](artifact/references/source-coverage.md)
- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-code-quality)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown review report with structured findings and optional code, shell, or configuration snippets when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings use Symptom, Source, Consequence, and Remedy; reports include a 0-100 review-index Health Score.]

## Skill Version(s):

0.4.0 (source: frontmatter, package.json, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
