## Description:

Generate conventional commit messages from git diffs and staged changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect staged or unstaged git diffs, classify the change, and draft a Conventional Commit message before presenting it or using it with git commit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Git diffs can include proprietary source code or secrets accidentally present in local changes.

Mitigation: Review the diff content and generated commit message before sharing output outside the workspace.

Risk: A generated commit command or message may be inaccurate for the intended change.

Mitigation: Review the proposed Conventional Commit text before allowing an agent to run `git commit -m`.

## Reference(s):

- [Conventional Commits Reference](references/conventional-commits.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown commit-message text with optional shell command and JSON diff-analysis snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read git diff content; review generated commit commands before execution.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
