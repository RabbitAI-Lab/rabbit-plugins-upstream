## Description:

Space Duck Kimi Relay lets self-hosted Space Duck users sign in to Kimi locally and run a localhost OpenAI-compatible proxy for Kimi inference, with an optional metered OpenRouter fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[askegor](https://clawhub.ai/user/askegor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators running Space Duck on their own infrastructure use this skill to connect their own Kimi membership for inference while keeping Kimi credentials in local custody.

### Deployment Geography for Use:

Global; Kimi inference is processed by Moonshot AI infrastructure in China, so users with Western data residency requirements should not use this lane.

## Known Risks and Mitigations:

Risk: Kimi access and refresh tokens are stored locally, and optional OPENROUTER_API_KEY or KIMI_* variables can be persisted for the service.

Mitigation: Install only on machines where local credential storage is acceptable, review environment variables before install-service, and keep generated credential and environment files permission-restricted.

Risk: Prompts and inference traffic are routed through Moonshot/Kimi infrastructure in China, with optional OpenRouter fallback when configured.

Mitigation: Use this relay only when that data path fits policy, and avoid it for conversations requiring Western data residency.

Risk: Printed access tokens or proxy secrets can be exposed if pasted into logs, chats, or shared terminals.

Mitigation: Prefer the localhost proxy over copying tokens, keep proxy authentication enabled, and avoid sharing printed token or secret values.

Risk: OpenRouter fallback can incur metered spend if OPENROUTER_API_KEY is configured.

Mitigation: Keep the fallback daily cap enabled, monitor fallback usage, and adjust KIMI_RELAY_FALLBACK_DAILY_CAP only intentionally.

Risk: KIMI_RELAY_NO_AUTH=1 disables the localhost proxy bearer check.

Mitigation: Leave proxy authentication enabled except on trusted single-user machines where disabling it is an explicit choice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/askegor/skills/space-duck-kimi-relay)
- [Security manifest](artifact/SECURITY-MANIFEST.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide use of a local OpenAI-compatible proxy, local credential files, optional service installation, and optional OpenRouter fallback configuration.]

## Skill Version(s):

0.8.21 (source: server release evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
