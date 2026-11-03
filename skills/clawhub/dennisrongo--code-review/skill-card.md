## Description:

Reviews working-tree or branch changes for production readiness, DRY and design issues, correctness, tests, security, and build health, then reports categorized findings before applying any approved fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to review uncommitted changes, pull requests, or branches before shipping. It checks implementation intent, runs detected tests and builds, and produces actionable findings without editing code until fixes are explicitly approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may run repository tests and builds, fetch branch refs, create temporary worktrees, and inspect source diffs during review.

Mitigation: Use it in trusted workspaces and review command scope before allowing review activity on repositories with sensitive code or external side effects.

Risk: The skill can propose fixes or GitHub review replies after it reports findings.

Mitigation: Require explicit approval for each fix batch or reply; the documented workflow reports first and waits before editing code or responding on GitHub.

Risk: Parallel review helpers may receive repository diffs and related source context for non-trivial changes.

Mitigation: Run it only where the active agent and review helpers are permitted to inspect the relevant repository content.

## Reference(s):

- [Branch Review Workflow](references/branch-review.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Code, Guidance]

**Output Format:** [Markdown review report with categorized findings, command results, file-line references, and optional approved code changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run detected tests and builds, inspect diffs, use sub-agents for larger reviews, and wait for explicit approval before editing code.]

## Skill Version(s):

1.0.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
