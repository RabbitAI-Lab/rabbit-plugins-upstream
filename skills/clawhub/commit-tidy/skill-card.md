## Description:

Helps developers review staged changes and commit history, then plan focused commits, clearer messages, and safe history cleanup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to inspect staged changes and commit history, plan split or squash decisions, draft commit messages, and review changes before rewriting history or pushing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reset, amend, rebase, or force-push can alter or replace commit history.

Mitigation: Review the planned changes and verify the target branch before approving any history rewrite or force-with-lease push.

Risk: Enabling a Claude hook or post-commit review trigger can introduce persistent commit-time behavior.

Mitigation: Leave hooks disabled unless explicitly needed, and review their behavior before enabling them.

Risk: Local agent configuration may affect commit workflows beyond the immediate request.

Mitigation: Review local agent rules and their scope before using the skill to change commit behavior.

## Reference(s):

- [Commit Tidy on ClawHub](https://clawhub.ai/drumrobot/skills/commit-tidy)
- [Staging discipline](staging-discipline.md)
- [Commit message discipline](message-discipline.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with Git command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations and approval checkpoints before commit or push operations.]

## Skill Version(s):

0.7.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
