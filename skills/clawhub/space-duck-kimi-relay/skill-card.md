## Description:

space-duck-kimi-relay helps self-hosted Space Duck users run a local Kimi device-code sign-in and localhost proxy so their runtime can use their own Kimi membership for inference, with optional capped OpenRouter fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[askegor](https://clawhub.ai/user/askegor)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to connect a self-hosted Space Duck runtime to their own Kimi membership through a local proxy. It supports local credential custody, token refresh, service installation, health checks, and an optional daily-capped OpenRouter fallback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores Kimi refresh credentials locally and can optionally store an OpenRouter API key for fallback.

Mitigation: Install only when local credential custody is acceptable; keep the generated credential files user-readable only and prefer local login on each machine.

Risk: Disabling localhost bearer authentication or overriding KIMI_* endpoints can expose quota or redirect auth and inference traffic.

Mitigation: Keep the default localhost bearer protection enabled, avoid KIMI_RELAY_NO_AUTH except on a truly single-user machine, and set endpoint overrides only intentionally.

Risk: Kimi inference is processed by Moonshot AI in China, and optional OpenRouter fallback is metered.

Mitigation: Do not use this lane for workloads requiring Western data residency; configure OpenRouter fallback only when pay-per-token use and the daily cap are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/askegor/skills/space-duck-kimi-relay)
- [Security Manifest](artifact/SECURITY-MANIFEST.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local credential, bearer-secret, service, and proxy configuration guidance for the user's machine.]

## Skill Version(s):

0.8.2 (source: server release evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
