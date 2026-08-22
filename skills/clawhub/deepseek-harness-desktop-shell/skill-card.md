## Description:

Guides an agent through wrapping an already-running local DeepSeek Harness Web UI in an Electron desktop application, covering prerequisites, a minimal desktop shell, local URL loading, packaging, and distribution boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[potfromsky](https://clawhub.ai/user/potfromsky)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill when they already have DeepSeek Harness running locally and want agent guidance to create an Electron desktop wrapper that loads the local Harness Web UI while preserving Harness features and plugins.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install, packaging, distribution, and auto-launch steps may change local projects, install npm dependencies, or create distributable application artifacts.

Mitigation: Review proposed npm install, packaging, distribution, auto-launch, and filesystem actions with the user before execution.

Risk: Preserving Harness plugin behavior means the resulting desktop app allows the local Harness instance and its plugins to operate normally.

Mitigation: Keep plugin management in Harness, disclose that plugin capabilities remain active, and review installed Harness plugins before distributing or using the wrapped app.

Risk: Loading arbitrary remote URLs or exposing Node capabilities to page content would increase the Electron shell attack surface.

Mitigation: Keep the shell scoped to the local Harness URL, use context isolation, keep nodeIntegration disabled, and expose only a minimal preload bridge.

## Reference(s):

- [Desktop shell scaffolding and packaging prompt](artifact/references/desktop-shell-prompt.md)
- [DeepSeek Harness project](https://github.com/deepseek-ai/deepseek-harness)
- [ClawHub skill page](https://clawhub.ai/potfromsky/skills/deepseek-harness-desktop-shell)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with code snippets, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended as agent-facing implementation guidance; high-impact install, packaging, distribution, and filesystem changes should be confirmed with the user before execution.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
