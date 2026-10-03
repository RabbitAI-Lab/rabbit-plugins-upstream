## Description:

Helps developers connect Claude Code to third-party models and troubleshoot model selection, configuration, streaming, and performance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oracis](https://clawhub.ai/user/oracis)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to configure Claude Code for third-party Anthropic-compatible endpoints or a local gateway for OpenAI-compatible endpoints, switch model profiles, and diagnose connection issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Switching profiles changes user-level Claude Code settings across projects.

Mitigation: Review the active profile and back up existing settings before switching.

Risk: Profile and gateway configuration can contain provider API keys.

Mitigation: Inspect profile files before use and avoid sharing files containing real keys.

Risk: Prompts are sent to third-party model providers.

Mitigation: Use non-sensitive test prompts first and select only providers you trust.

Risk: A local gateway can remain running after a profile switch.

Mitigation: Stop the gateway and remove unneeded backups when finished.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/oracis/skills/claude-code-third-party-model)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown with shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide model profile and local gateway setup instructions.]

## Skill Version(s):

1.1.1 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
