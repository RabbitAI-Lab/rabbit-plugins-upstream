## Description:

Optional Lane A / BYOB add-on for Space Duck that runs a local RFC 8628 device-code sign-in flow for Kimi, stores Kimi credentials locally, and exposes a localhost OpenAI-compatible proxy with optional OpenRouter fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[askegor](https://clawhub.ai/user/askegor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when running Space Duck on their own infrastructure and want a local Kimi membership relay instead of static pay-per-token API keys. It helps configure login, token refresh, proxy service management, health checks, and optional capped fallback behavior.

### Deployment Geography for Use:

Global; Kimi inference is processed on Moonshot AI infrastructure in China, so users with Western data residency requirements should avoid this lane.

## Known Risks and Mitigations:

Risk: Environment overrides can redirect authentication, token refresh, prompts, and persistent service configuration away from the intended Kimi endpoints.

Mitigation: Before login, serve, or install-service, confirm KIMI_AUTH_HOST and KIMI_CODING_BASE are unset or set only to the intended Kimi HTTPS endpoints.

Risk: The local machine holds and refreshes Kimi access and refresh credentials for the relay.

Mitigation: Install and run the relay only on machines where persistent local credential custody is acceptable; avoid printing tokens except for brief manual tests and never paste them into logs, chats, or shared terminals.

Risk: Optional OpenRouter fallback can create pay-per-token spend if OPENROUTER_API_KEY is configured.

Mitigation: Use the documented daily cap and monitor fallback status; leave OPENROUTER_API_KEY unset if paid fallback is not intended.

Risk: Disabling proxy bearer authentication allows any local process to spend the user's Kimi quota through the localhost proxy.

Mitigation: Keep proxy authentication enabled by default and use KIMI_RELAY_NO_AUTH=1 only on single-user machines where that local exposure is acceptable.

Risk: Kimi inference is processed on Moonshot AI infrastructure in China.

Mitigation: Do not route conversations through this lane when Western data residency or other incompatible residency controls are required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/askegor/skills/space-duck-kimi-relay)
- [Publisher profile](https://clawhub.ai/user/askegor)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides local credential setup, localhost proxy use, service installation, status checks, and fallback limits.]

## Skill Version(s):

0.9.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
