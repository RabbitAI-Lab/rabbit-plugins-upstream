## Description:

Analyzes Git changes, drafts project-appropriate commit messages, and creates one or more local commits grouped by feature.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stevenwangking](https://clawhub.ai/user/stevenwangking)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this Chinese-language helper to review repository changes, draft commit messages that follow project conventions, and create local commits, optionally split by feature. A status mode previews the proposed commits without staging or committing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commit-oriented requests can automatically stage and commit normal repository changes.

Mitigation: Use /commit status or ask to inspect changes first, and review the proposed files and messages before requesting an automatic commit.

Risk: Sensitive files, dependency changes, or large deletions could be included in a commit.

Mitigation: Review these changes before invoking the automatic flow; the skill pauses for confirmation when it detects an exception.

## Reference(s):

- [ClawHub commit skill](https://clawhub.ai/stevenwangking/skills/commit)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Chinese-language commit messages and Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports commit hashes and file statistics; status mode returns a preview without creating commits.]

## Skill Version(s):

1.0.0 (source: skill metadata and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
