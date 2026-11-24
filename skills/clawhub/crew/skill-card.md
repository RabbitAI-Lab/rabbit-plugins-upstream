## Description:

Splits the current iTerm2 session to launch and coordinate Codex, agy, or Claude agents in tmux, run anonymous three-round reviews, and save or restore agent groups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[garmanwu](https://clawhub.ai/user/garmanwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using Claude Code, Codex, or agy use this skill to start and message agents in a tmux-based group, coordinate anonymous three-round reviews, and save or restore agent sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports launcher injection risk and defaults that weaken agent safeguards.

Mitigation: Review the setup and launcher behavior before use; keep sandboxing and approval prompts enabled where possible.

Risk: Using multiple model providers may expose project context to providers or agents that receive it.

Mitigation: Avoid sharing confidential project information across providers unless you understand what will be sent, and check group recipients before messaging.

Risk: The security review was marked partial because some local references could not be resolved.

Mitigation: Review the skill files and setup instructions before running the workflow.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/garmanwu/skills/crew)
- [Publisher profile](https://clawhub.ai/user/garmanwu)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [JSON command results and concise usage guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can launch, message, inspect, save, restore, or coordinate agent sessions.]

## Skill Version(s):

1.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
