## Description:

Optional add-on for Space Duck that helps a self-hosted duck sign in with Kimi, keep Kimi membership credentials on the owner's machine, and expose a local OpenAI-compatible relay for Kimi models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[askegor](https://clawhub.ai/user/askegor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators running Space Duck on their own infrastructure use this skill to authenticate a local Kimi membership relay, refresh tokens, run a local proxy, and optionally install it as a background service.

### Deployment Geography for Use:

Global, with Kimi inference processed by Moonshot AI on infrastructure in China.

## Known Risks and Mitigations:

Risk: The skill stores and refreshes local Kimi credentials and can print fresh access tokens.

Mitigation: Keep credentials on trusted machines only, avoid pasting access tokens into less-trusted systems, and use logout or re-login when credential lineage changes.

Risk: Disabling proxy authentication with KIMI_RELAY_NO_AUTH allows local processes to use the owner's Kimi quota.

Mitigation: Leave proxy authentication enabled except on a trusted single-user machine.

Risk: Optional OpenRouter fallback may route failed Kimi requests to a pay-per-token third-party service.

Mitigation: Configure OPENROUTER_API_KEY only when fallback is desired, keep the daily fallback cap enabled, and monitor fallback status.

Risk: Installed service files can capture environment variables such as API keys.

Mitigation: Review installed systemd or launchd service files and refresh or remove captured secrets when configuration changes.

Risk: Kimi inference is processed by Moonshot AI on infrastructure in China.

Mitigation: Do not use this relay for conversations that require Western data residency.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/askegor/skills/space-duck-kimi-relay)
- [Publisher profile](https://clawhub.ai/user/askegor)
- [Kimi authorization host](https://auth.kimi.com)
- [Kimi coding API base](https://api.kimi.com/coding/v1)
- [OpenRouter API fallback](https://openrouter.ai/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May emit local status text, local proxy URLs, Kimi access tokens, and service setup instructions depending on the command.]

## Skill Version(s):

0.5.1 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
