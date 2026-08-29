## Description:

Runs a local browser-approved Kimi device-code sign-in and localhost proxy so a self-hosted Space Duck can use the owner's Kimi membership for inference, with optional OpenRouter fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[askegor](https://clawhub.ai/user/askegor)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to configure local Kimi membership authentication and an OpenAI-compatible localhost proxy for self-hosted Space Duck deployments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local Kimi refresh tokens and proxy bearer secrets are persistent credentials.

Mitigation: Install only when local credential storage is acceptable, keep files permissioned to the owner, and use logout or service removal when access is no longer needed.

Risk: The localhost proxy can be exposed to other local processes if proxy authentication is disabled.

Mitigation: Keep proxy auth enabled by default and avoid KIMI_RELAY_NO_AUTH except on tightly controlled single-user machines.

Risk: Kimi inference is processed by Moonshot AI infrastructure in China, which may not satisfy data-residency requirements.

Mitigation: Do not route conversations through this skill when Western or other specific data residency is required.

Risk: Service mode can persist credential-bearing relay access across sessions, and macOS launchd may embed captured environment secrets in the plist.

Mitigation: Review generated service files before enabling persistent service mode and prefer foreground serve mode for initial validation.

Risk: Optional OpenRouter fallback is metered and can incur pay-per-token spend.

Mitigation: Use the default daily fallback cap or set an appropriate KIMI_RELAY_FALLBACK_DAILY_CAP before enabling fallback.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/askegor/skills/space-duck-kimi-relay)
- [Security manifest](SECURITY-MANIFEST.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local credential paths, localhost proxy settings, environment variables, and operational cautions.]

## Skill Version(s):

0.8.9 (source: ClawHub release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
