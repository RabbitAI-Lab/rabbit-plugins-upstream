## Description:

A Chinese-language Git CLI helper that guides agents through repository inspection, staging, Conventional Commits, branch operations, remote synchronization, conflict resolution, and history review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to inspect Git repositories, stage changes, draft standardized commit messages, manage branches, synchronize remotes, and resolve merge or rebase conflicts from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact Git operations can delete local work or rewrite shared remote history.

Mitigation: Require manual confirmation before branch deletion, reset, rebase, push, tag push, force-with-lease, or any operation touching shared branches.

Risk: The artifact includes broad command-execution guidance and generic API key setup that is not clearly required for Git CLI use.

Mitigation: Use the skill only for explicit Git tasks, run commands in the intended repository, and do not provide API keys unless the publisher clearly documents why they are needed and what repository data is sent externally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/git-cli)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Artifact skill definition](artifact/SKILL.md)
- [Declared homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and occasional JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Git commands that inspect, stage, commit, branch, merge, rebase, fetch, pull, push, tag, or review repository history.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
