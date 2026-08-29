## Description:

Detects codebase bloat via dead code, duplication, complexity, and doc bloat scans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to scan repositories for dead code, duplication, stale files, dependency bloat, documentation bloat, and growth trends before cleanup, release, or refactoring work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository scans may run shell and git commands over the working tree and may create temporary or report files.

Mitigation: Run from a clean working tree, inspect commands and generated reports, and remove temporary artifacts after review.

Risk: Dependency validation examples may query package registries.

Mitigation: Use registry checks only when network access and package-name disclosure are acceptable for the repository.

Risk: Heuristic cleanup recommendations can misclassify live code, documentation, or dependencies as bloat.

Mitigation: Treat findings as proposals, use dry-run previews where available, and approve any deletion or refactor only after human review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-bloat-detector)
- [Source homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conserve)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown analysis with inline shell commands and optional scan or audit report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce temporary scan artifacts or report files when requested; recommendations require user review before cleanup.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter reports 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
