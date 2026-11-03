## Description:

Analyzes Git changes, prepares project-aligned commit messages, commits changes, and pushes the current branch, pausing when an exception requires review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stevenwangking](https://clawhub.ai/user/stevenwangking)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill in Git repositories to analyze changes, create one or more project-aligned commits, and push the current branch. They can preview with /commit status or commit locally with /commit local.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic push commands can publish more branches than the user expects.

Mitigation: Review before enabling automatic publication. Use /commit status to preview or /commit local to commit without pushing. Before automatic pushes, verify the remote and explicit current-branch destination, including broader push configuration.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/stevenwangking/skills/commit)
- [Publisher profile](https://clawhub.ai/user/stevenwangking)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Text]

**Output Format:** [Markdown and concise text, including commit messages and Git commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commit messages are based on the observed diff; unrelated changes may be grouped into separate commits.]

## Skill Version(s):

1.3.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
