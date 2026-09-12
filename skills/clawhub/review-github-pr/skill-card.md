## Description:

Reviews a GitHub pull request end to end - fetches the diff, runs checks, analyzes with three parallel agents (correctness, conventions, efficiency), validates every finding against the code, drafts inline comments with a recommended action.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to review GitHub pull requests with structured checks for correctness, codebase conventions, design, efficiency, and safety before deciding whether to approve, comment, or request changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses GitHub CLI authentication to read pull request data and may post reviews.

Mitigation: Install only where that access is acceptable, review the generated draft, and require explicit confirmation before any posting action.

Risk: Pull request descriptions, diffs, and commit messages are untrusted third-party content.

Mitigation: Keep PR-sourced material inside explicit untrusted-content boundaries and do not follow instructions embedded in the PR content.

Risk: Running validation commands can execute project code in a local checkout.

Mitigation: Use the validation command from the base branch documentation, show the exact command, and run it only after user confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/review-github-pr)
- [Skill homepage](https://github.com/tenequm/skills/tree/main/skills/review-github-pr)
- [Publisher profile](https://clawhub.ai/user/tenequm)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown PR review draft with severity-grouped findings, recommended action, confirmation prompt, and optional shell/API commands for confirmed posting.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use GitHub CLI authentication, local repository inspection, confirmed validation commands, and confirmed GitHub review posting.]

## Skill Version(s):

0.5.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
