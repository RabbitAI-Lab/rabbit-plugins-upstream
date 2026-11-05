## Description:

Reviews code changes in diffs, files, commits, GitHub pull requests, and GitLab merge requests, producing structured, regression-focused findings and actionable merge guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-zihan](https://clawhub.ai/user/z-zihan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review proposed code changes before merge, assess regression and compatibility risks, and receive structured findings with actionable recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The repair workflow's whole-file undo command can erase unrelated unfinished work.

Mitigation: Save a recoverable copy before repair, inspect each proposed edit, and reverse only the approved repair.

Risk: Remote code reviews may use repository credentials.

Mitigation: Use repository-scoped credentials for remote reviews.

## Reference(s):

- [Project homepage](https://github.com/z-Zihan/awesome-skills)
- [Code Review ProMax on ClawHub](https://clawhub.ai/z-zihan/skills/code-review-promax)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code]

**Output Format:** [Structured Markdown code review reports with proposed code changes when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Language follows the user's input; findings are organized by severity and include actionable recommendations.]

## Skill Version(s):

2.1.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
