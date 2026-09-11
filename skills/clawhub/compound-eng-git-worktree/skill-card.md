## Description:

Manage Git worktrees for isolated parallel development. Use when creating, listing, switching, or cleaning up git worktrees, or when needing isolated branches for concurrent reviews or feature work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to create, list, switch to, and clean up Git worktrees for isolated reviews or parallel feature work while preserving other sessions' branches and files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill copies local .env files into newly created worktrees, which can duplicate secrets into additional filesystem locations.

Mitigation: Use it only in trusted repositories and remove, template, or rotate sensitive .env values before creating worktrees.

Risk: The workflow encourages dependency installation inside new worktrees, which may run package install scripts from the checked-out project.

Mitigation: Avoid untrusted branches and review dependency install scripts before allowing package managers to run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-git-worktree)
- [Workflow Examples](artifact/references/workflow-examples.md)
- [Troubleshooting and Technical Details](artifact/references/troubleshooting.md)
- [Hooks and Local Excludes](artifact/references/hooks-and-excludes.md)
- [Worktree Integration](artifact/references/worktree-integration.md)
- [Worktree Manager Script](artifact/scripts/worktree-manager.sh)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance, configuration]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include worktree paths, command examples, and cleanup choices depending on the task.]

## Skill Version(s):

4.5.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
