## Description:

Helps developers decide when a separate Git worktree is warranted, including for concurrent agents, active work, and shared-resource constraints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clarezoe](https://clawhub.ai/user/clarezoe)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to decide whether concurrent or interrupted Git work needs a separate worktree, check for shared-resource conflicts, and plan cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Removing the wrong worktree can affect a local checkout that is still needed.

Mitigation: Check the worktree list and remove only worktrees intentionally created and no longer needed.

Risk: Parallel worktrees can interfere through shared ports, databases, or containers.

Mitigation: Isolate shared resources before running in parallel, or sequence the work instead.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/clarezoe/skills/git-worktree-decision)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Decision guidance includes a shared-resource check and a worktree teardown plan.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
