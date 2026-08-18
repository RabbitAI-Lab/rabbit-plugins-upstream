## Description:

Space Duck Kimi Relay lets self-hosted Space Duck users sign in locally with Kimi membership, store credentials on their own machine, and run a localhost OpenAI-compatible proxy for Kimi inference with optional capped OpenRouter fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[askegor](https://clawhub.ai/user/askegor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators self-hosting Space Duck use this skill to authenticate locally with Kimi and route local runtime inference through a localhost proxy while keeping Kimi credentials off hosted services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores Kimi refresh tokens and a proxy bearer secret under ~/.kimi-code on the user's machine.

Mitigation: Use it only on trusted machines, preserve restrictive file permissions, and avoid pasting printed access tokens into logs, chat, or shared terminals.

Risk: Kimi inference is routed to Moonshot AI infrastructure in China, and optional OpenRouter fallback can create metered usage.

Mitigation: Do not use this lane for workloads that require Western data residency; omit OPENROUTER_API_KEY to disable fallback or monitor the daily fallback cap when enabled.

Risk: KIMI_RELAY_NO_AUTH disables the localhost proxy bearer check, and endpoint overrides can re-point token traffic.

Mitigation: Keep proxy authentication enabled by default and use endpoint overrides only when the operator understands the effect.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/askegor/skills/space-duck-kimi-relay)
- [Publisher profile](https://clawhub.ai/user/askegor)
- [Security manifest](artifact/SECURITY-MANIFEST.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide users through local credential storage, localhost proxy setup, optional service installation, and optional capped OpenRouter fallback.]

## Skill Version(s):

0.8.6 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
