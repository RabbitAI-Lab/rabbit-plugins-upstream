## Description:

space-duck-kimi-relay lets self-hosted Space Duck users run a local Kimi device-code sign-in and localhost proxy so their duck can use their own Kimi membership for inference, with optional OpenRouter fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[askegor](https://clawhub.ai/user/askegor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and self-hosted Space Duck operators use this skill to authenticate locally with Kimi, refresh tokens, run a localhost inference proxy, and configure an optional capped OpenRouter fallback.

### Deployment Geography for Use:

Global, with Kimi inference processed by Moonshot AI infrastructure in China.

## Known Risks and Mitigations:

Risk: The skill stores Kimi access and refresh credentials locally.

Mitigation: Install only on a machine where local credential storage is acceptable, keep credential files private, and use logout when credentials should be removed.

Risk: Disabling proxy authentication can let other local processes use the relay.

Mitigation: Keep bearer authentication enabled unless running on a trusted single-user machine.

Risk: The optional OpenRouter fallback uses a pay-per-token API key.

Mitigation: Keep OPENROUTER_API_KEY and relay.env private and rely on the configured daily fallback cap to limit unintended spend.

Risk: Endpoint overrides can redirect token or inference traffic.

Mitigation: Change KIMI_AUTH_HOST or KIMI_CODING_BASE only when the replacement endpoints are fully trusted.

Risk: Kimi inference is processed by Moonshot AI infrastructure in China.

Mitigation: Do not route workloads through this lane when Western data residency is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/askegor/skills/space-duck-kimi-relay)
- [Publisher profile](https://clawhub.ai/user/askegor)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local setup and operating guidance for Kimi login, token refresh, localhost proxy use, service install, status checks, fallback limits, and logout.]

## Skill Version(s):

0.8.5 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
