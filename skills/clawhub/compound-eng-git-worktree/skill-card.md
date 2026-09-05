## Description:

Manage Git worktrees for isolated parallel development when creating, listing, switching, or cleaning up worktrees, or when needing isolated branches for concurrent reviews or feature work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to create, list, switch, and clean up isolated Git worktrees for parallel feature development, code review, and branch work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The worktree manager automatically copies .env files into new worktrees, which can duplicate API keys, database passwords, tokens, or other secrets.

Mitigation: Review before installation in repositories that store secrets in .env files; prefer making environment copying opt-in, warning before copies, restricting copied files to an allowlist, and avoiding backup copies of secret files by default.

Risk: Cleanup and discard workflows can remove worktrees or branches if used against the wrong checkout.

Mitigation: Confirm the active worktree, branch ownership, and git status before cleanup or discard operations; require explicit user confirmation for destructive choices.

## Reference(s):

- [Workflow Examples](references/workflow-examples.md)
- [Troubleshooting and Technical Details](references/troubleshooting.md)
- [Hooks and Local Excludes](references/hooks-and-excludes.md)
- [Worktree Manager Script](scripts/worktree-manager.sh)
- [ClawHub Skill Page](https://clawhub.ai/iliaal/skills/compound-eng-git-worktree)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide an agent to run the bundled worktree manager script, update local git ignore settings, copy environment files, install dependencies, and report structured change summaries.]

## Skill Version(s):

4.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
