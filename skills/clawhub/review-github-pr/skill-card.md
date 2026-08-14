## Description:

Reviews a GitHub pull request end to end. Fetches the diff, runs automated checks, analyzes the changes with three parallel review agents (correctness, convention compliance, efficiency), validates every finding against the actual code, and drafts a GitHub review that posts findings as inline diff comments with a recommended action of approve, request changes, or comment only.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review GitHub pull requests by fetching PR context, running the repository's declared validation checks, analyzing changed files for correctness, conventions, design, efficiency, and safety, and preparing a review draft for user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes untrusted pull request diffs, descriptions, and commit messages that may contain prompt-like instructions.

Mitigation: The artifact instructs agents to wrap PR-sourced content in explicit boundary markers and treat that content as untrusted data.

Risk: The skill may use git and gh against repositories, run repository validation commands, and post GitHub review comments.

Mitigation: Evidence.security advises installation only when the user is comfortable with those actions; the artifact limits automated checks to commands declared in the local repository and requires explicit user confirmation before posting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/review-github-pr)
- [Skill homepage](https://github.com/tenequm/skills/tree/main/skills/review-github-pr)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown review draft with inline code references and optional GitHub review API payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation before posting a GitHub review.]

## Skill Version(s):

0.4.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
