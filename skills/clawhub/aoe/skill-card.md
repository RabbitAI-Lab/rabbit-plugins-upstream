## Description:

Manage AI coding agent sessions via Agent of Empires (aoe).

This skill is ready for commercial/non-commercial use.

## Publisher:

[njbrake](https://clawhub.ai/user/njbrake)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to launch, organize, monitor, capture, and manage AI coding agent sessions running through Agent of Empires and tmux.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Powerful session commands can start, stop, remove, or alter coding-agent workspaces, including worktrees.

Mitigation: Use exact session IDs, inspect sessions with list or info commands before destructive actions, and avoid forceful removal unless intended.

Risk: Captured agent output may contain incomplete, incorrect, or misleading work.

Mitigation: Review captured session output before acting on it or using it to make project changes.

Risk: YOLO mode can skip normal permission prompts for agent sessions.

Mitigation: Keep normal permission prompts enabled for routine work and enable YOLO mode only for explicitly trusted workflows.

## Reference(s):

- [Agent of Empires project homepage](https://github.com/agent-of-empires/agent-of-empires)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the aoe and tmux command-line tools.]

## Skill Version(s):

1.15.1 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
