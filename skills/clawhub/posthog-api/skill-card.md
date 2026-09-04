## Description:

PostHog API integration with managed authentication for product analytics, feature flags, session recordings, experiments, and related PostHog workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operators use this skill to query PostHog analytics, inspect projects and users, manage feature flags, review session recordings, and run experiments through Maton-managed authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected PostHog accounts can expose sensitive analytics, person records, and session recording data.

Mitigation: Prefer OAuth through the Maton CLI, choose the narrowest PostHog scopes available, and avoid pulling person records or session recordings unless they are needed for the task.

Risk: Write operations can modify dashboards, feature flags, cohorts, actions, annotations, surveys, experiments, or related PostHog resources.

Mitigation: Default to read and list calls, then require explicit confirmation of the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: Multiple Maton or PostHog connections can route a request to the wrong account.

Mitigation: Specify the intended Maton profile and PostHog connection when more than one exists.

Risk: Long-lived API keys or provider-issued tokens can leak through logs, files, command lines, or copied output.

Mitigation: Use CLI-managed OAuth where possible, never print or persist credentials, and send any required Maton API key only to api.maton.ai.

## Reference(s):

- [PostHog Skill on ClawHub](https://clawhub.ai/byungkyu/skills/posthog-api)
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

**Output Format:** [Markdown with inline shell commands, code snippets, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Maton CLI commands, API request examples, configuration guidance, and PostHog response interpretation.]

## Skill Version(s):

1.2.0 (source: ClawHub release metadata; artifact frontmatter version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
