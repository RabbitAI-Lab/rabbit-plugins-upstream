## Description:

Space Duck Kimi Relay lets self-hosted Space Duck users sign in locally with Kimi, store credentials on their machine, and run a localhost proxy that refreshes Kimi tokens for inference with optional capped OpenRouter fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[askegor](https://clawhub.ai/user/askegor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators running Space Duck on their own infrastructure use this skill to authenticate with Kimi through a local device-code flow and expose a localhost OpenAI-compatible proxy for inference.

### Deployment Geography for Use:

Global, with a documented data residency limitation that Kimi inference is processed by Moonshot AI in China.

## Known Risks and Mitigations:

Risk: Kimi refresh tokens, proxy bearer secrets, and optional OpenRouter credentials are handled on the local machine.

Mitigation: Install only where local credential storage is acceptable, keep generated credential files private, and use logout or uninstall-service when the relay is no longer needed.

Risk: Endpoint overrides such as KIMI_AUTH_HOST and KIMI_CODING_BASE can redirect token or inference traffic.

Mitigation: Leave endpoint overrides unset unless the replacement endpoint is fully trusted.

Risk: Disabling proxy auth with KIMI_RELAY_NO_AUTH=1 can allow other local processes to use the proxy quota.

Mitigation: Keep proxy authentication enabled except on controlled single-user systems.

Risk: Kimi inference is processed by Moonshot AI in China and may not satisfy Western data residency requirements.

Mitigation: Do not route workloads through this lane when those residency requirements apply.

Risk: Optional OpenRouter fallback is pay-per-token and can incur spend if membership calls fail.

Mitigation: Use the default daily cap or set KIMI_RELAY_FALLBACK_DAILY_CAP to an appropriate limit; omit OPENROUTER_API_KEY when fallback is not desired.

## Reference(s):

- [Security Manifest](SECURITY-MANIFEST.md)
- [ClawHub Skill Page](https://clawhub.ai/askegor/skills/space-duck-kimi-relay)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can guide local credential creation, localhost proxy operation, optional service installation, and capped OpenRouter fallback configuration.]

## Skill Version(s):

0.8.4 (source: server release evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
