## Description:

Manage Git worktrees for isolated parallel development when creating, listing, switching, or cleaning up worktrees, or when using isolated branches for concurrent reviews or feature work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to create and manage isolated Git worktrees for parallel feature work, code review, branch switching, and cleanup while preserving session ownership boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can copy local .env-style files, which may contain secrets, into newly created worktrees and backup files.

Mitigation: Install only where copied environment files are acceptable; verify those files remain ignored, treat copies as secrets, and avoid use with repositories containing production credentials or highly sensitive tokens.

## Reference(s):

- [Workflow Examples](references/workflow-examples.md)
- [Troubleshooting & Technical Details](references/troubleshooting.md)
- [Hooks and Local Excludes](references/hooks-and-excludes.md)
- [Worktree Integration](references/worktree-integration.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces worktree management guidance and command invocations for the bundled shell manager.]

## Skill Version(s):

4.6.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
