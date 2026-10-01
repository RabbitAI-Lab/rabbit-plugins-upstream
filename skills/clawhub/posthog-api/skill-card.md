## Description:

Helps agents query PostHog analytics, inspect user behavior and session recordings, and manage feature flags, surveys, and experiments through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and product teams use this skill to answer analytics questions and manage PostHog features through their authorized connection. It also describes optional, user-approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Maton connection can expose sensitive PostHog analytics and session recordings.

Mitigation: Trust Maton to broker the account, grant the narrowest available access, prefer aggregates, and retrieve recordings only when specifically requested.

Risk: Writes, hosted functions, triggers, and destinations can change data or run persistent automations.

Mitigation: Approve each write, function, trigger, and destination separately, especially automations involving non-PostHog event sources.

Risk: Fallback raw HTTP use handles a long-lived Maton API key.

Mitigation: Use the CLI when possible; otherwise keep the key in a secret-managed environment and do not print, persist, or expose it in command arguments.

## Reference(s):

- [PostHog skill on ClawHub](https://clawhub.ai/byungkyu/skills/posthog-api)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [PostHog API documentation](https://posthog.com/docs/api)
- [PostHog HogQL documentation](https://posthog.com/docs/hogql)
- [Trigger reference: time](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Text or Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize authorized PostHog results; outputs can contain sensitive analytics data.]

## Skill Version(s):

1.2.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
