## Description:

Generate conventional commit messages from staged git changes, including suggested type, optional scope, subject, and explanatory body when appropriate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when they have staged git changes and need a clear conventional commit message before committing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Staged diffs may contain secrets or sensitive files.

Mitigation: Review staged files before using the skill and unstage any sensitive material.

Risk: The assistant may offer to create a git commit after drafting the message.

Mitigation: Approve commit execution only when you intend to create the commit.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/commit-helper)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown commit message with optional explanatory body and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the staged git diff as context and should only commit after explicit user approval.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
