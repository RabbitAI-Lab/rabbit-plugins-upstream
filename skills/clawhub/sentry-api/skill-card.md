## Description:

Sentry API integration with managed authentication for monitoring errors, issues, application performance, and managing Sentry organizations, projects, teams, releases, issues, and events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to inspect Sentry organizations, projects, issues, events, teams, and releases through authenticated Maton-mediated Sentry API calls. They can also create approved Sentry-related functions or scheduled/event-driven automations when ongoing checks are required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Sentry connection can access the user's Sentry account data and any Sentry resources allowed by the authorized scopes.

Mitigation: Prefer OAuth, use least-privilege scopes, specify the intended connection when multiple connections exist, and default to read/list operations before proposing changes.

Risk: Write operations, connection creation or deletion, functions, triggers, and destinations can make persistent changes or continue running after setup.

Mitigation: Require explicit user approval for each write or automation step, disclose the target resource and intended effect, and remove functions or destinations when they are no longer needed.

Risk: Raw HTTP fallback with MATON_API_KEY uses a long-lived credential that may leak through logs, shell history, child processes, or copied output.

Mitigation: Use the Maton CLI with OAuth when possible; if fallback is necessary, keep the key in the process environment only, never print or persist it, and rotate it if exposed.

Risk: Trigger destinations can forward event payloads containing business data or personal data continuously to another URL.

Mitigation: Keep destinations on api.maton.ai or *.maton.app when possible, obtain separate approval for any third-party host, and forward only the minimum fields needed.

## Reference(s):

- [ClawHub Sentry Skill](https://clawhub.ai/byungkyu/skills/sentry-api)
- [Maton Homepage](https://maton.ai)
- [Sentry API Documentation](https://docs.sentry.io/api/)
- [Sentry API Authentication](https://docs.sentry.io/api/auth/)
- [Sentry Events API](https://docs.sentry.io/api/events/)
- [Sentry Projects API](https://docs.sentry.io/api/projects/)
- [Sentry Organizations API](https://docs.sentry.io/api/organizations/)
- [Sentry Teams API](https://docs.sentry.io/api/teams/)
- [Sentry Releases API](https://docs.sentry.io/api/releases/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Maton-authenticated Sentry API calls; write operations, connection changes, functions, triggers, and destinations require explicit user approval.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
