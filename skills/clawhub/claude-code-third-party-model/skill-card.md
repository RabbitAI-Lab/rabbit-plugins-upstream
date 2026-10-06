## Description:

Helps developers connect Claude Code to third-party models, switch configurations, and troubleshoot model and connection issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oracis](https://clawhub.ai/user/oracis)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to configure Claude Code with third-party Anthropic-compatible endpoints or a local gateway for OpenAI-compatible models, switch profiles, and diagnose configuration and performance issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Switching profiles changes sensitive Claude Code settings and may expose API keys if configuration files are shared.

Mitigation: Review profiles before switching, keep API keys out of shared files, and retain backups of existing settings.

Risk: Prompts routed through third-party endpoints or the local gateway are sent to the configured provider.

Mitigation: Choose providers with acceptable data policies and avoid sending sensitive work to anonymous or unclear-data-policy models.

Risk: A running local gateway can handle model traffic and access configured upstream credentials.

Mitigation: Keep the gateway bound to loopback, use its client-token authentication, and stop it when not needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/oracis/skills/claude-code-third-party-model)
- [Claude Code settings JSON schema](https://json.schemastore.org/claude-code-settings.json)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Shell commands, Code]

**Output Format:** [Markdown with JSON and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes example model profiles and optional local gateway and profile-switching scripts.]

## Skill Version(s):

1.1.3 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
