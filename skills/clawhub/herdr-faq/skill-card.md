## Description:

Launch and drive coding agents (codex, claude, agy) through the Herdr CLI. Use before starting or prompting a subagent via herdr agent or pane commands, and when a herdr command fails or an agent seems stuck or silently lost a prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and operators use this skill to launch, prompt, monitor, and troubleshoot Herdr-managed coding agents across Codex, Claude Code, and Antigravity/agy sessions. It provides command recipes, state-reading guidance, and failure triage for multi-agent terminal workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill teaches agents how to launch other coding agents and automate agent prompts, which can amplify unintended actions if used in an unreviewed workspace.

Mitigation: Review the planned Herdr commands before execution and use explicit status reads, prompt waits, and artifact-based completion checks.

Risk: Some recipes pre-trust workspaces or enable automatic edit approval for child agents.

Mitigation: Prefer temporary or manually approved trust where possible, review trust-configuration changes before use, and remove Antigravity trusted workspace entries that should not persist.

Risk: Agent state detection can report idle or done while work is still running or while prompts have not actually taken effect.

Mitigation: Read the pane or detection source before prompting, confirm effects rather than relying only on exit status, and wait on expected output files for non-trivial tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/herdr-faq)
- [ClawHub publisher profile](https://clawhub.ai/user/tenequm)
- [Herdr documentation](https://herdr.dev)
- [OpenClaw homepage](https://github.com/tenequm/skills/tree/main/skills/herdr-faq)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown guidance with bash command blocks and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes operational recipes, state checks, and troubleshooting notes for Herdr agent workflows.]

## Skill Version(s):

0.3.3 (source: evidence.release.version and SKILL.md metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
