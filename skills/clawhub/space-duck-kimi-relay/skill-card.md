## Description:

space-duck-kimi-relay helps a self-hosted Space Duck deployment sign in to Kimi locally, store credentials on the user's machine, and run a localhost OpenAI-compatible proxy with an optional capped OpenRouter fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[askegor](https://clawhub.ai/user/askegor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators running Space Duck on their own infrastructure use this skill to configure local Kimi membership authentication, token refresh, proxy serving, service installation, status checks, fallback behavior, and logout workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores Kimi access and refresh tokens locally and can print a fresh access token.

Mitigation: Keep credential files private, avoid pasting tokens into logs or shared terminals, use the proxy for normal operation, and run logout when local custody is no longer needed.

Risk: Endpoint override variables can repoint token or inference traffic.

Mitigation: Use KIMI_AUTH_HOST, KIMI_CODING_BASE, and KIMI_CLIENT_ID only for trusted destinations and review environment variables before starting or installing the service.

Risk: The install-service workflow can persist captured configuration and secrets across sessions.

Mitigation: Review the persisted service environment before enabling autostart and uninstall or refresh the service when secrets or endpoints change.

Risk: Inference through the Kimi lane is processed by Moonshot AI infrastructure in China.

Mitigation: Do not route workloads through this lane when Western data residency or a different processing region is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/askegor/skills/space-duck-kimi-relay)
- [Security manifest](artifact/SECURITY-MANIFEST.md)
- [Skill source](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples and local Python script usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces setup and operational guidance for a local proxy; the included script can emit access tokens, health/status text, and OpenAI-compatible proxy responses when run by the user.]

## Skill Version(s):

0.9.1 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
