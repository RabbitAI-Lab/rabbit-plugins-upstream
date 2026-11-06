## Description:

Reviews code changes for correctness, regression risk, compatibility, security, and downstream impact, then returns structured, actionable findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-zihan](https://clawhub.ai/user/z-zihan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to review diffs, files, commits, GitHub pull requests, and GitLab merge requests for defects and regression risks. It returns an actionable, structured review and can prepare minimal fixes when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Undo guidance in fix mode may erase unrelated unfinished work if applied broadly.

Mitigation: Save unfinished work first, review the rollback steps, and undo only approved changes rather than checking out whole files.

## Reference(s):

- [Project homepage (listed in skill metadata)](https://github.com/z-Zihan/awesome-skills)
- [ClawHub skill page](https://clawhub.ai/z-zihan/skills/code-review-promax)

## Skill Output:

**Output Type(s):** [Markdown, Code, Guidance]

**Output Format:** [Structured Markdown review report; optional code diffs for approved fixes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Language follows the user's language; requested fixes are minimal and require confirmation.]

## Skill Version(s):

2.1.2 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
