## Description:

Manage AI coding agent sessions via Agent of Empires (aoe)

This skill is ready for commercial/non-commercial use.

## Publisher:

[njbrake](https://clawhub.ai/user/njbrake)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to launch, organize, monitor, and manage coding agent sessions in tmux, including worktree-based workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: YOLO mode skips permission prompts, so a coding agent may take actions within the project without the usual approval checks.

Mitigation: Keep permission prompts enabled unless you intentionally need YOLO mode, and choose the project directory carefully.

Risk: Permanent purge options can remove sessions, worktrees, or branches.

Mitigation: Review the target and deletion flags before running permanent-deletion commands.

Risk: The documented sandbox includes agent credentials and does not isolate them from the agent.

Mitigation: Treat credentials available in the sandbox as accessible to the agent and avoid exposing credentials the task does not need.

Risk: aoe, tmux, and coding agent tools are installed separately and are not bundled with this skill.

Mitigation: Install these tools from sources you trust.

## Reference(s):

- [Agent of Empires project homepage](https://github.com/agent-of-empires/agent-of-empires)
- [Sandbox guide](https://github.com/agent-of-empires/agent-of-empires/blob/main/docs/guides/sandbox.md)
- [ClawHub skill page](https://clawhub.ai/njbrake/skills/aoe)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides command examples and operational guidance for coding agent sessions.]

## Skill Version(s):

1.22.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
