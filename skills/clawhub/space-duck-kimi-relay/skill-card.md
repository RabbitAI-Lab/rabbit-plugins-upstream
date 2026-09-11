## Description:

Space Duck Kimi Relay lets self-hosted Space Duck users sign in to Kimi locally and run a localhost proxy that injects fresh Kimi membership tokens for inference, with an optional daily-capped OpenRouter fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[askegor](https://clawhub.ai/user/askegor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and self-hosted Space Duck operators use this skill to connect a local agent runtime to a Kimi membership without handing credentials to Spaceduckling. It supports local sign-in, token refresh, proxy service setup, health checks, fallback configuration, and logout.

### Deployment Geography for Use:

Global; Kimi inference is processed by Moonshot AI infrastructure in China, so users with Western data residency requirements should avoid this lane.

## Known Risks and Mitigations:

Risk: The relay stores Kimi access and refresh credentials plus a local proxy bearer secret on the user's machine.

Mitigation: Install only on trusted local machines, keep the default 0600 credential files, and remove credentials or the service when the relay is no longer needed.

Risk: Overridable Kimi endpoints can redirect credential-bearing traffic if set to untrusted hosts.

Mitigation: Avoid KIMI_AUTH_HOST and KIMI_CODING_BASE unless the target endpoint is fully trusted.

Risk: KIMI_RELAY_NO_AUTH disables the localhost proxy bearer check.

Mitigation: Leave proxy authentication enabled except on explicitly single-user systems.

Risk: Kimi inference is processed in China, and the optional OpenRouter fallback sends prompts to third-party infrastructure and can incur metered spend.

Mitigation: Do not use this lane for workloads requiring Western data residency, and configure the OpenRouter fallback only intentionally with an appropriate daily cap.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/askegor/skills/space-duck-kimi-relay)
- [Security Manifest](artifact/SECURITY-MANIFEST.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes local service commands, credential handling guidance, endpoint disclosures, and fallback limits.]

## Skill Version(s):

0.9.0 (source: server release metadata and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
