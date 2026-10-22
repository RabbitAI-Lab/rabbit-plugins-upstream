## Description:

Enables a self-hosted Space Duck runtime to sign in to a Kimi membership locally and use it through a localhost-only inference proxy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[askegor](https://clawhub.ai/user/askegor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and self-hosters use this optional add-on to authenticate with a Kimi membership and configure a localhost OpenAI-compatible proxy for a self-hosted Space Duck runtime.

### Deployment Geography for Use:

Global; Kimi inference is processed in China, with no Western data residency.

## Known Risks and Mitigations:

Risk: The optional paid fallback may exceed its intended spending limit.

Mitigation: Leave the fallback disabled until its limit is enforced atomically, or set a separate spending limit with the provider.

Risk: Installing the background service on macOS can alter its configuration unsafely.

Mitigation: Use foreground mode on macOS until service configuration is safely serialized.

Risk: Kimi inference is processed in China, and enabling fallback sends prompts to the configured OpenRouter service.

Mitigation: Do not route conversations through these services when their data handling or residency does not meet your requirements; keep fallback disabled unless its provider is approved.

Risk: Service installation retains selected credentials across reboots.

Mitigation: Restrict access to the local machine and remove the service and stored credentials when they are no longer needed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/askegor/skills/space-duck-kimi-relay)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell-command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions for local device-code sign-in and a localhost inference proxy; does not generate a separate artifact.]

## Skill Version(s):

0.9.11 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
