## Description:

Enables self-hosted Space Duck agents to sign in to Kimi through a browser-approved device flow and use a local inference proxy with optional metered fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[askegor](https://clawhub.ai/user/askegor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers running self-hosted Space Duck agents can use their Kimi membership for inference through a locally authenticated proxy instead of configuring a static access token. An optional OpenRouter fallback supports metered inference when membership calls fail.

### Deployment Geography for Use:

Global; Kimi inference is processed in China and is unsuitable where Western data residency is required.

## Known Risks and Mitigations:

Risk: Local Kimi tokens and an optional OpenRouter key grant access to accounts or metered usage.

Mitigation: Protect local credential files, prefer the authenticated localhost proxy, and avoid printing or sharing tokens.

Risk: Disabling proxy authentication can expose membership quota to other users or processes on a shared machine.

Mitigation: Do not enable KIMI_RELAY_NO_AUTH on shared machines.

Risk: Optional fallback can incur pay-per-token charges when membership requests fail.

Mitigation: Enable fallback only when needed and set an appropriate daily call cap.

Risk: Endpoint overrides can redirect token traffic, and service installation can persist secrets in a macOS launchd plist.

Mitigation: Avoid endpoint overrides unless the destination is trusted; review service installation and protect the macOS plist.

Risk: Kimi inference is processed in China rather than under Western data residency.

Mitigation: Do not route conversations requiring Western data residency through this relay.

## Reference(s):

- [Space Duck Kimi Relay on ClawHub](https://clawhub.ai/askegor/skills/space-duck-kimi-relay)
- [Security manifest](SECURITY-MANIFEST.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local sign-in, token refresh, proxy setup, and optional paid fallback.]

## Skill Version(s):

0.9.8 (source: ClawHub release metadata and _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
