## Description:

Installs Codex Desktop or Codex CLI, configures Codex to use the Juxingyi gateway, and exposes Codex status and session context to agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaobod1](https://clawhub.ai/user/zhaobod1)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to install or verify Codex, configure a Juxingyi-compatible model gateway, and produce status or session context reports for agent handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The configuration script rewrites ~/.codex/config.toml and changes the Codex model provider, base URL, model, and reasoning settings.

Mitigation: Back up and inspect ~/.codex/config.toml before running configure.sh, then verify the gateway URL, selected model, and retained project or plugin sections after configuration.

Risk: The status, sessions, and context scripts can print Codex conversation history, working directories, project names, tool-call summaries, and configuration values.

Mitigation: Run these scripts only in trusted terminals and workspaces, and review output before sharing it with agents, logs, or external systems.

Risk: API keys supplied through shell commands or environment variables may be captured in shell history, process listings, or logs.

Mitigation: Prefer interactive secret entry or a secret manager, and avoid embedding real API keys in commands that may be logged.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaobod1/skills/huo15-codex-juxingyi-setup)
- [Juxingyi console](https://fireworks-simulator.huo15.com/app/)
- [ChatGPT download](https://chatgpt.com/download)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports with shell command snippets and TOML configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read local Codex configuration, project paths, gateway status, and recent session summaries when context scripts are run.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
