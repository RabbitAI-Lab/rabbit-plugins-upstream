## Description:

Space Duck Kimi Relay lets a self-hosted Space Duck use a local Kimi device-code sign-in and localhost proxy to route inference through the owner's Kimi membership, with optional daily-capped OpenRouter fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[askegor](https://clawhub.ai/user/askegor)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to sign in to Kimi locally, keep credentials on their own machine, and expose a localhost OpenAI-compatible proxy for self-hosted Space Duck inference.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores persistent Kimi OAuth credentials on the local machine.

Mitigation: Install only on trusted machines, keep the default local file permissions, and use logout when credentials should no longer remain available.

Risk: Inference content is sent to Moonshot/Kimi infrastructure in China.

Mitigation: Do not use this relay for conversations or workloads that require Western data residency.

Risk: The optional OpenRouter fallback can create metered billing activity.

Mitigation: Configure OPENROUTER_API_KEY only when fallback billing is intended, keep the daily cap enabled, and monitor fallback usage.

Risk: Endpoint override variables can redirect authentication or inference traffic.

Mitigation: Avoid KIMI_AUTH_HOST and KIMI_CODING_BASE overrides unless the destination is fully trusted.

Risk: Disabling proxy authentication lets local processes use the relay without the bearer secret.

Mitigation: Keep default proxy authentication enabled, and use KIMI_RELAY_NO_AUTH only on single-user systems where local process access is acceptable.

Risk: Installing the relay as a service creates a persistent credential-bearing background process.

Mitigation: Review captured service environment variables and uninstall the service when persistent relay access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/askegor/skills/space-duck-kimi-relay)
- [Security manifest](artifact/SECURITY-MANIFEST.md)
- [Kimi authorization endpoint](https://auth.kimi.com)
- [Kimi inference endpoint](https://api.kimi.com/coding/v1)
- [OpenRouter fallback endpoint](https://openrouter.ai/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell command snippets and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local command sequences for login, proxy service management, status checks, and logout.]

## Skill Version(s):

0.9.7 (source: server release evidence and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
