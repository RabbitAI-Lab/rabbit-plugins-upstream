## Description:

code-polish is a pre-release code-review workflow that runs lint and type checks, reviews diffs for cleanliness, design, efficiency, and side-effect ordering, validates findings, and proposes approval-gated fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use code-polish before committing, pushing, or releasing changes to catch validated issues in changed code and decide which fixes to apply.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow reads changed repository files, runs the repository validation command, and creates a temporary local copy of the diff.

Mitigation: Use it only in repositories where that access is acceptable, and avoid sensitive diffs unless local temporary copies are permitted.

Risk: Approval-gated fixes can still be incorrect if the reviewer accepts a bad proposal.

Mitigation: Review proposed fixes and rerun the project's validation command before committing or releasing changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/code-polish)
- [Metadata homepage](https://github.com/tenequm/skills/tree/main/skills/polish)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown review report with file and line findings, recommendations, and optional targeted code edits after approval]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs local repository validation when configured, reports validated findings first, and waits for explicit approval before modifying code.]

## Skill Version(s):

2.5.1 (source: frontmatter, changelog, and server release evidence; released 2026-08-21)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
