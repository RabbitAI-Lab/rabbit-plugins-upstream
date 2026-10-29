## Description:

Connect coding agents and other agent runtimes to withHuman with the withhuman CLI so their tool calls wait for human approval. Covers installing the CLI, guided onboarding, connecting a runtime to an existing agent, checking the connection, refreshing the tool catalogue, upgrading, and removing the adapter. Use for Claude Code, Codex, OpenClaw, Pi, Hermes and DeepSeek on macOS or Linux, hosted or self-hosted.

This skill is ready for commercial/non-commercial use.

## Publisher:

[withhuman](https://clawhub.ai/user/withhuman)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to install and connect a supported runtime to a withHuman organization, apply its human approval workflow to tool calls, and manage or troubleshoot the connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The selected approval server receives tool-call information, and its rules may approve some actions automatically.

Mitigation: Use a trusted approval server and check which actions its rules approve automatically.

Risk: The installer may request administrator access.

Mitigation: Review the installer before running it, especially if administrator access is requested.

Risk: A disconnected runtime may retain a usable instance credential.

Mitigation: When permanently disconnecting, remove the adapter and revoke its instance credential.

## Reference(s):

- [withHuman CLI skill on ClawHub](https://clawhub.ai/withhuman/skills/withhuman-cli)
- [withHuman Quickstart](https://withhuman.ai/docs/getting-started/quickstart.md)
- [withHuman Agents guide](https://withhuman.ai/docs/web-app/agents.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
