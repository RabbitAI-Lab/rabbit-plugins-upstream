## Description:

Manage AI coding agent sessions via Agent of Empires (aoe).

This skill is ready for commercial/non-commercial use.

## Publisher:

[njbrake](https://clawhub.ai/user/njbrake)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, monitor, inspect, organize, and clean up AI coding agent sessions managed by the Agent of Empires CLI in tmux.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some referenced aoe options can bypass prompts or force actions, including -y, --force, and --delete-worktree.

Mitigation: Review generated commands before execution and use force or deletion options only when the affected session, profile, or worktree is clearly identified.

Risk: Session capture can expose tmux pane contents, including sensitive project output or agent conversation text.

Mitigation: Inspect captured output before sharing it and avoid capturing sessions that may contain secrets or private data.

Risk: Profile deletion and worktree cleanup can remove local state.

Mitigation: Confirm the active profile and repository state before running cleanup or delete commands, and keep important work committed or backed up.

## Reference(s):

- [Agent of Empires GitHub repository](https://github.com/agent-of-empires/agent-of-empires)
- [Agent of Empires ClawHub skill page](https://clawhub.ai/njbrake/skills/aoe)
- [njbrake ClawHub publisher profile](https://clawhub.ai/user/njbrake)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the aoe and tmux binaries.]

## Skill Version(s):

1.14.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
