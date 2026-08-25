## Description:

Space Duck Kimi Relay helps self-hosted Space Duck users run a local Kimi device-code sign-in flow and localhost OpenAI-compatible proxy so their duck can use their Kimi membership, with optional metered OpenRouter fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[askegor](https://clawhub.ai/user/askegor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and self-hosted Space Duck operators use this skill to sign in to Kimi locally, run a protected localhost proxy, and configure their runtime to use Kimi membership inference without sending Kimi credentials to Spaceduckling.

### Deployment Geography for Use:

Global; Kimi inference is processed by Moonshot AI infrastructure in China, so users with data residency requirements should evaluate this lane before use.

## Known Risks and Mitigations:

Risk: The skill stores Kimi access and rotating refresh credentials locally.

Mitigation: Keep the credential files private, rely on the documented 0600 file permissions, avoid pasting tokens into logs or shared terminals, and run logout when the local credential should be removed.

Risk: The localhost proxy can spend the user's Kimi quota, and disabling proxy authentication allows any local process to use it.

Mitigation: Use the generated proxy bearer secret by default and only set KIMI_RELAY_NO_AUTH=1 on single-user systems where that exposure is acceptable.

Risk: Optional OpenRouter fallback can create metered usage when OPENROUTER_API_KEY is configured.

Mitigation: Leave OPENROUTER_API_KEY unset unless paid fallback is intended, and keep the daily fallback cap configured to an acceptable limit.

Risk: Kimi inference is processed on Moonshot AI infrastructure in China.

Mitigation: Do not route conversations through this lane when the user requires Western data residency or has incompatible regional data-handling requirements.

Risk: Service installation can persist selected environment values for the relay, with documented macOS plist residual handling.

Mitigation: Review installed user services after install-service, remove them when no longer needed, and inspect or rotate captured environment values if service configuration changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/askegor/skills/space-duck-kimi-relay)
- [Security Manifest](artifact/SECURITY-MANIFEST.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include localhost proxy URLs, credential-handling guidance, service setup steps, fallback configuration, and status or troubleshooting output.]

## Skill Version(s):

0.8.7 (source: server release evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
