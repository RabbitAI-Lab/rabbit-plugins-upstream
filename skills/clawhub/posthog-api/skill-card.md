## Description:

PostHog API integration with managed authentication for querying analytics events, managing feature flags, viewing session recordings, and running experiments through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analytics operators use this skill to access PostHog through Maton for analytics queries, feature flag management, dashboards, session recordings, surveys, and experiments. It is intended for tasks where an agent should default to read and list calls and ask for confirmation before connecting accounts or changing PostHog resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change PostHog resources such as feature flags, dashboards, experiments, and surveys.

Mitigation: Default to read and list calls, then require explicit confirmation of the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: Requests may act on the wrong PostHog connection or Maton profile when multiple accounts exist.

Mitigation: Specify the intended Maton profile and PostHog connection, and review requested OAuth scopes before authorizing or modifying resources.

Risk: Long-lived API keys or provider-issued tokens can leak through logs, command lines, files, or pasted output.

Mitigation: Prefer OAuth through the Maton CLI, avoid printing or persisting credentials, and use the raw HTTP fallback only when the CLI cannot be installed.

Risk: Data returned from PostHog may contain untrusted content that should not steer follow-up actions or local execution.

Mitigation: Treat API responses as data, validate values before reuse, and never execute local scripts or commands based on PostHog response content.

## Reference(s):

- [ClawHub PostHog Skill](https://clawhub.ai/byungkyu/skills/posthog-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [PostHog API Overview](https://posthog.com/docs/api)
- [HogQL Documentation](https://posthog.com/docs/hogql)
- [PostHog Feature Flags](https://posthog.com/docs/feature-flags)
- [PostHog Session Replay](https://posthog.com/docs/session-replay)
- [PostHog Experiments](https://posthog.com/docs/experiments)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and Python and JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected PostHog account; write operations require explicit user confirmation.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
