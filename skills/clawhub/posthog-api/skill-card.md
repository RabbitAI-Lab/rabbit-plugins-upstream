## Description:

PostHog API integration with managed authentication for querying product analytics, managing feature flags, analyzing user behavior, viewing session recordings, and running experiments through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analytics operators use this skill to query PostHog product analytics, inspect persons and session recordings, and manage dashboards, feature flags, cohorts, surveys, and experiments through authenticated Maton API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PostHog analytics data, person profiles, and session recordings can contain personal or sensitive user information.

Mitigation: Use the narrowest project, person, event, and time range needed; prefer aggregate results; retrieve session recordings only when explicitly requested; and avoid copying identifiers or recording contents outside the immediate answer.

Risk: Write operations can change dashboards, feature flags, cohorts, annotations, surveys, experiments, or other PostHog resources.

Mitigation: Default to read and list calls, then obtain explicit user confirmation for the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: A Maton API key is a long-lived credential that can leak through logs, shell history, process listings, or persisted environment files.

Mitigation: Prefer OAuth through the Maton CLI; if raw HTTP is required, read the key from the environment inside the process, never print or persist it, and rotate it if exposure occurs.

Risk: Multiple Maton accounts or PostHog connections can cause requests to run against the wrong account.

Mitigation: Specify the intended connection or profile when more than one exists, especially before write operations.

Risk: Deleting a Maton connection revokes stored authorization and may break automation using that connection.

Mitigation: List connections first, match the exact connection identifier with the user, and avoid bypassing confirmation unless the user already confirmed the specific deletion.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/posthog-api)
- [Maton](https://maton.ai)
- [PostHog API Overview](https://posthog.com/docs/api)
- [HogQL Documentation](https://posthog.com/docs/hogql)
- [PostHog Feature Flags](https://posthog.com/docs/feature-flags)
- [PostHog Session Replay](https://posthog.com/docs/session-replay)
- [PostHog Experiments](https://posthog.com/docs/experiments)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include PostHog API paths, Maton CLI commands, request bodies, jq filters, and minimized API response excerpts.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
