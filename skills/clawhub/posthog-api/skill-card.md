## Description:

PostHog API integration with managed authentication for querying product analytics, managing feature flags, analyzing user behavior, viewing session recordings, and running experiments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product analysts, and operators use this skill to access PostHog through a managed Maton connection for analytics queries, feature flag management, session recording review, dashboards, cohorts, surveys, annotations, and experiments. It defaults to read and list workflows, with explicit approval expected before connection changes, writes, hosted functions, or trigger-based automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive PostHog analytics data, including person profiles, event streams, identifiers, and session recordings.

Mitigation: Query the narrowest project, person, event, and time range needed; prefer aggregates; avoid retrieving session recordings unless specifically requested; and do not copy raw identifiers or recording contents outside the immediate answer.

Risk: Long-lived API keys and raw HTTP usage can expose credentials through environment variables, logs, shell history, or child processes.

Mitigation: Prefer OAuth through the Maton CLI, avoid exporting API keys, keep credentials in the operating system credential store, and rotate any key that was printed, committed, or pasted.

Risk: Write operations or connection changes can modify PostHog state or grant new account access.

Mitigation: Default to read and list calls, verify target identifiers first, and require explicit user approval for connection creation, POST, PUT, PATCH, DELETE, function deploys, and trigger changes.

Risk: Hosted functions and triggers can run persistently and can use the deploying Maton account's connected services.

Mitigation: Use dedicated Maton accounts or connection sets, deploy only user-authored or user-reviewed handlers, prefer DENY_ALL network policy, keep destinations inside Maton unless explicitly approved, and remove automation when it is no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/posthog-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [PostHog API Overview](https://posthog.com/docs/api)
- [HogQL Documentation](https://posthog.com/docs/hogql)
- [PostHog Feature Flags](https://posthog.com/docs/feature-flags)
- [PostHog Session Replay](https://posthog.com/docs/session-replay)
- [PostHog Experiments](https://posthog.com/docs/experiments)
- [Calendly Trigger Reference](artifact/references/calendly/triggers.md)
- [GitHub Trigger Reference](artifact/references/github/triggers.md)
- [Google Mail Trigger Reference](artifact/references/google-mail/triggers.md)
- [HubSpot Trigger Reference](artifact/references/hubspot/triggers.md)
- [Linear Trigger Reference](artifact/references/linear/triggers.md)
- [Notion Trigger Reference](artifact/references/notion/triggers.md)
- [Slack Trigger Reference](artifact/references/slack/triggers.md)
- [Stripe Trigger Reference](artifact/references/stripe/triggers.md)
- [Time Trigger Reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, JSON API examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API request paths, JSON payloads, Python or JavaScript SDK snippets, and least-privilege approval prompts.]

## Skill Version(s):

1.2.3 (source: server release metadata; artifact frontmatter metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
