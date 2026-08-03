## Description: <br>
Manage AI coding agent sessions via Agent of Empires (aoe). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[njbrake](https://clawhub.ai/user/njbrake) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding-agent operators use this skill to launch, organize, monitor, capture, and clean up Agent of Empires sessions for coding work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: High-impact agent launch examples can skip permission prompts or run unattended. <br>
Mitigation: Use YOLO mode only in tightly controlled environments and review proposed agent actions before relying on session output. <br>
Risk: Forced cleanup and delete-worktree commands can remove worktree state or uncommitted changes. <br>
Mitigation: Verify session IDs, worktree paths, and uncommitted changes before running force cleanup or delete-worktree commands. <br>


## Reference(s): <br>
- [Agent of Empires homepage](https://github.com/agent-of-empires/agent-of-empires) <br>
- [ClawHub skill page](https://clawhub.ai/njbrake/skills/aoe) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text, markdown] <br>
**Output Format:** [Markdown with inline bash commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Provides command-oriented guidance for aoe and tmux-based agent session workflows.] <br>

## Skill Version(s): <br>
1.13.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
