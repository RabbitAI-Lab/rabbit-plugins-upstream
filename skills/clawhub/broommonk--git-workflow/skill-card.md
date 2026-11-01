## Description:

Git Workflow helps agents inspect repository changes, stage files, generate commit messages, commit changes, push to remotes, manage multiple repositories, and provide common Git troubleshooting guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[broommonk](https://clawhub.ai/user/broommonk)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to automate common Git repository workflows such as checking status, preparing commits, pushing changes, coordinating multiple repositories, and troubleshooting configuration, authentication, or merge-conflict issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may stage, commit, or push unrelated changes if repository scope and diffs are not reviewed.

Mitigation: Require explicit repository selection, inspect git status and staged diffs before committing, and avoid broad staging commands unless the full change set has been reviewed.

Risk: A push can publish secrets, private files, or unintended commits to a remote repository.

Mitigation: Approve git push as a separate step after confirming the target remote, branch, and committed contents.

## Reference(s):

- [Git Workflow on ClawHub](https://clawhub.ai/broommonk/skills/git-workflow)
- [Publisher profile](https://clawhub.ai/user/broommonk)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated Git commit messages, repository status summaries, and troubleshooting steps.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter, skill.yaml, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
