## Description:

TinkerClaw Subagent Overseer monitors OpenClaw sub-agents with a local Bash daemon, checks process and filesystem activity, and writes a status file that heartbeat agents can read without repeated model/tool polling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to monitor OpenClaw sub-agents from the operating system side, detect idle or stuck sessions, and let heartbeat agents read a local status file instead of repeatedly polling with model/tool calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a local background daemon that monitors OpenClaw sub-agents and writes daemon state to disk.

Mitigation: Install it only when local sub-agent monitoring is desired, use a private user-owned status directory, and stop or clean up the daemon with the documented lifecycle commands when monitoring is no longer needed.

Risk: The status file can include basenames of recently changed files under the watched work directory.

Mitigation: Scope --workdir narrowly for the active task and use --no-filenames for sensitive projects.

Risk: The fallback status directory is under /tmp, which may be less appropriate on shared machines.

Mitigation: Prefer XDG_RUNTIME_DIR or pass a private --status-dir with user-only permissions.

Risk: The optional --voice-files mode can speak changed filenames aloud.

Mitigation: Use default voice alerts or --voice without --voice-files unless filename disclosure to people nearby is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/subagent-overseer)
- [TinkerClaw repository link from skill materials](https://github.com/globalcaos/tinkerclaw)
- [agent-superpowers related ClawHub skill](https://clawhub.ai/globalcaos/agent-superpowers)
- [smart-model-router related ClawHub skill](https://clawhub.ai/globalcaos/smart-model-router)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands; the daemon writes JSON status files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Status output includes process health, sub-agent counts, staleness state, filesystem change counts, and optionally recent file basenames.]

## Skill Version(s):

1.1.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
