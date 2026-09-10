## Description:

TinkerClaw Subagent Overseer monitors OpenClaw sub-agent sessions with a local bash daemon, writes status JSON, and helps heartbeat agents detect stalled or exited workers without model polling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to supervise OpenClaw sub-agents with local process and filesystem checks, reducing model polling while surfacing stuck or exited workers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence flags unsafe state-file and PID-file handling for review before installation.

Mitigation: Use a trusted private --status-dir until the state-directory and PID-file validation issues are fixed.

Risk: Status files can record basenames of recently changed files, which may reveal sensitive work context.

Mitigation: Scope --workdir narrowly and use --no-filenames when filenames are sensitive.

Risk: Voice alerts may disclose filenames in shared spaces when --voice-files is enabled.

Mitigation: Avoid --voice-files in shared spaces; default voice alerts speak counts only.

Risk: The skill runs a local background daemon.

Mitigation: Do not run it as root, and use --stop or --cleanup when monitoring is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/subagent-overseer)
- [TinkerClaw repository](https://github.com/globalcaos/tinkerclaw)
- [Agent Superpowers companion skill](https://clawhub.ai/globalcaos/agent-superpowers)
- [Smart Model Router companion skill](https://clawhub.ai/globalcaos/smart-model-router)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with bash commands and status JSON references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The daemon writes local status JSON under the configured status directory; voice alerts are optional.]

## Skill Version(s):

1.1.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
