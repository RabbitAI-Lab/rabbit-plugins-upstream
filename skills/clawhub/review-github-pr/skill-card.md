## Description:

Reviews a GitHub pull request end to end. Fetches the diff, runs automated checks, analyzes the changes with three parallel review agents (correctness, convention compliance, efficiency), validates every finding against the actual code, and drafts a GitHub review that posts findings as inline diff comments with a recommended action of approve, request changes, or comment only.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to review GitHub pull requests by gathering PR metadata and diffs, running the repository's configured validation command, coordinating focused review agents, and preparing a confirmed GitHub review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill checks out pull request code and runs local repository validation commands.

Mitigation: Use it on repositories where running local project checks is acceptable, and run only validation commands explicitly configured by the repository.

Risk: Pull request descriptions, diffs, and commit messages are untrusted input that may contain misleading instructions.

Mitigation: Treat PR-sourced content as data, preserve boundary markers for sub-agent review, and validate every finding against the actual changed files.

Risk: Posting reviews uses the user's GitHub credentials and can affect a real pull request.

Mitigation: Require explicit user confirmation before posting and use appropriately scoped GitHub credentials.

## Reference(s):

- [review-github-pr ClawHub page](https://clawhub.ai/tenequm/skills/review-github-pr)
- [review-github-pr source homepage](https://github.com/tenequm/skills/tree/main/skills/review-github-pr)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown review draft with recommended action, confirmation prompt, and optional GitHub review command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May prepare inline review comments and a GitHub review payload only after user confirmation.]

## Skill Version(s):

0.4.2 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
