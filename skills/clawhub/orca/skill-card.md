## Description:

Launch and coordinate agent sessions inside the Orca IDE runtime by finding running terminals, delivering prompts after target confirmation, launching new sessions, and guiding installation of Orca skill bundles into supported agent harnesses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to coordinate multi-agent work inside Orca: selecting a live terminal, confirming the exact handoff target and prompt, launching a new agent session when needed, and installing Orca's bundled skills into Claude Code, OpenClaw, or Antigravity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send prompts to other active Orca agent sessions, so a wrong target could cause unrelated work to start acting on the delivered prompt.

Mitigation: Confirm the exact destination terminal and prompt text before every terminal send; use the documented list, filter, disambiguate, and deliver flow, and keep the send-confirmation guard enabled.

Risk: The skill can install persistent plugin or skill configuration into other harnesses.

Mitigation: Prefer project-scoped installs or reviewed, pinned plugin content, and report only the installation state that was verified by the harness list or inspect command.

Risk: The security review notes that one send-confirmation guard may miss documented Orca command aliases.

Mitigation: Treat sends through orca, orca-dev, orca-ide, and ORCA_CLI_COMMAND as requiring the same user confirmation even if a local guard does not intercept the command.

Risk: Registering repositories or creating independent worktrees changes Orca's durable workspace state.

Mitigation: Use already registered workspaces and split-first launch behavior by default; require explicit approval before project registration or independent workspace creation.

## Reference(s):

- [ClawHub skill page: orca](https://clawhub.ai/drumrobot/skills/orca)
- [ClawHub publisher profile: drumrobot](https://clawhub.ai/user/drumrobot)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON-oriented CLI checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include guard-script recommendations, confirmation steps, terminal handles, worktree selectors, and harness-specific installation instructions.]

## Skill Version(s):

0.4.0 (source: server release metadata, changelog released 2026-09-24)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
