## Description:

Guides an interactive Git bisect to find the commit that introduced a regression between known good and bad revisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmahmadcs](https://clawhub.ai/user/hmahmadcs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to trace a reproducible regression to its first bad commit through guided Git bisect checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bisect checks out older commits and can disrupt uncommitted work.

Mitigation: Begin with a clean worktree and run git bisect reset when finished or stopping early.

## Reference(s):

- [Git Bisect Coach on ClawHub](https://clawhub.ai/hmahmadcs/skills/git-bisect-coach)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires local Git and a reproducible pass/fail check.]

## Skill Version(s):

1.0.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
