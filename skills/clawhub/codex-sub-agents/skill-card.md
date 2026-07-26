## Description: <br>
OpenAI Codex Sub Agents helps Clawdbot delegate code review, refactoring, CI fixes, and feature implementation to OpenAI Codex CLI as a coding subagent or direct CLI tool. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[adamsardo](https://clawhub.ai/user/adamsardo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineering agents use this skill to route coding tasks to Codex CLI for code review, bug fixes, refactoring, CI repair, and feature implementation. It also documents Clawdbot integration patterns for direct exec calls, coding subagents, CLI fallback, and MCP server mode. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can delegate broad coding authority to Codex CLI, including file edits and command execution. <br>
Mitigation: Use trusted repositories, set the working directory explicitly, and prefer read-only or approval-gated modes for unfamiliar code. <br>
Risk: Full-access or no-approval modes can allow changes outside the intended project or environment. <br>
Mitigation: Avoid `--yolo` and `danger-full-access` outside disposable environments; use workspace-scoped sandboxing and review changes before relying on them. <br>
Risk: Codex authentication and token sync may expose sensitive session material if enabled without review. <br>
Mitigation: Review Codex auth/session storage, token sync behavior, and feedback logs before enabling the integration. <br>


## Reference(s): <br>
- [Codex CLI Overview](https://developers.openai.com/codex/cli) <br>
- [Codex CLI Features](https://developers.openai.com/codex/cli/features) <br>
- [Codex CLI Reference](https://developers.openai.com/codex/cli/reference) <br>
- [Slash Commands Guide](https://developers.openai.com/codex/cli/slash-commands) <br>
- [AGENTS.md Spec](https://agents.md) <br>
- [Codex GitHub](https://github.com/openai/codex) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash, JSON5, and TOML examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes command examples, integration patterns, approval-mode guidance, and troubleshooting notes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
