## Description:

A code review skill that helps agents review pull requests and code changes for quality, security, performance, maintainability, tests, and CI/CD status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to perform structured reviews of pull requests or local code changes, including CI/CD checks, security issues, test coverage, performance concerns, and maintainability feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses GitHub CLI and local Git credentials to inspect pull requests, CI status, checks, diffs, and workflow logs.

Mitigation: Install and run it only in repositories where that access is intended, and confirm the target repository, branch, pull request, and authentication context before allowing GitHub CLI commands.

Risk: The artifact includes a workflow for modifying code, committing, and pushing when CI failures occur on the user's own pull request.

Mitigation: Treat the skill as read-only unless fixes are explicitly requested; before any commit or push, review git status, the staged diff, the target branch, and the remote.

Risk: Review output can include concrete remediation guidance or code changes that may be incorrect for the project context.

Mitigation: Validate suggested fixes with the project's tests, linters, type checks, and reviewer judgment before merging or deploying changes.

## Reference(s):

- [Code Review Reference Guide](artifact/reference.md)
- [Code Review Examples](artifact/examples.md)
- [ClawHub Skill Page](https://clawhub.ai/terrycarter1985/skills/code-review)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown review feedback with optional code snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include prioritized findings, CI/CD status summaries, suggested fixes, and verification commands.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
