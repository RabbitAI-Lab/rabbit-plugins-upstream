## Description:

Keep a PR merge-ready by triaging comments, resolving clear conflicts, and fixing CI in a loop.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eohmig](https://clawhub.ai/user/eohmig)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to keep pull requests merge-ready by refreshing live PR state, resolving clear merge conflicts, triaging unresolved comments, and fixing CI failures within the PR scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make and push scoped pull request fixes, which can affect repository history.

Mitigation: Install it only in repositories where the agent is allowed to make scoped PR changes, require fresh PR state before each pass, and rely on the skill's rule against force-pushes or unrelated changes.

Risk: The skill may reply to review threads, creating reviewer-visible discussion.

Mitigation: Use it where automated triage replies are acceptable, and require blockers involving security, privacy, auth, billing, data, migration, or concurrency to be escalated to the user.

Risk: CI fixes or conflict resolutions could be incorrect if based on stale state or insufficient evidence.

Mitigation: Refresh live PR state at the start of each pass, read failing check logs before changing code, and run the narrowest relevant verification before pushing.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown status updates with inline shell commands, code changes, and GitHub review replies when permitted]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May push scoped PR fixes and reply to review threads when permitted; does not merge PRs, enable auto-merge, or mark draft PRs ready.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
