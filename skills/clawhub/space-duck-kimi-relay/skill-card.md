## Description:

Provides a local, browser-approved Kimi sign-in relay for self-hosted Space Duck instances, with optional metered OpenRouter fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[askegor](https://clawhub.ai/user/askegor)

### License/Terms of Use:

MIT-0

## Use Case:

External developers running Space Duck on self-managed infrastructure use this skill to sign in to Kimi with browser-approved device authorization and connect their runtime to a local inference relay.

### Deployment Geography for Use:

Global; Kimi inference is processed in China, so this lane is unsuitable when Western data residency is required.

## Known Risks and Mitigations:

Risk: Paid fallback can exceed the advertised daily limit.

Mitigation: Keep fallback disabled until calls are reserved atomically; if enabled, set provider-side spending limits.

Risk: Custom authentication or inference endpoints can receive Kimi login tokens.

Mitigation: Keep the default endpoints and proxy authentication; only override endpoints you trust, and protect printed tokens and proxy secrets.

Risk: Kimi inference is processed in China, without Western data residency.

Mitigation: Do not route conversations through this lane when Western data residency is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/askegor/skills/space-duck-kimi-relay)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Command-line instructions and local relay configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Interactive device-code sign-in; credentials remain local to the self-hosted machine.]

## Skill Version(s):

0.10.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
