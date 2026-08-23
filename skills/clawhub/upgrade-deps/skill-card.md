## Description:

Guides agents through evidence-based dependency upgrades by inventorying package versions, reading changelogs for major bumps, searching for affected APIs, running tests and builds between batches, and reporting verified changes and residual risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when upgrading project dependencies, reviewing dependency-update pull requests, or fixing audit findings while preserving evidence about changelogs, migration edits, tests, and unresolved risk.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent to edit manifests, lockfiles, project code, configuration, and commits during dependency upgrades.

Mitigation: Review diffs before accepting changes and require the reported test and build evidence before treating an upgrade as safe.

Risk: Dependency conflict workarounds such as force installs, legacy peer dependency modes, or overrides can hide compatibility problems.

Mitigation: Require explicit approval for conflict overrides and document the dependency conflict and revisit condition in the final report.

Risk: Repositories with missing or failing tests provide limited evidence for runtime safety after dependency upgrades.

Mitigation: Treat compile-only verification as limited, preserve the red baseline when present, and ask for baseline tests or a narrowed upgrade scope before broad changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dennisrongo/skills/upgrade-deps)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline command output, code snippets, and per-package report tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include proposed or applied manifest, lockfile, configuration, and migration edits, plus quoted test and build results.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
