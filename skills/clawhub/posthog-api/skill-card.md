## Description:

PostHog API integration with managed authentication for querying analytics events, managing feature flags, analyzing user behavior, viewing session recordings, and running A/B experiments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, data teams, and product teams use this skill to access PostHog analytics through Maton-managed authentication, including HogQL queries, feature flags, dashboards, session recordings, surveys, and experiments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access PostHog analytics data and modify PostHog resources after authorization.

Mitigation: Prefer OAuth, grant the narrowest available PostHog scopes, default to read/list calls, and require explicit user approval before POST, PUT, PATCH, or DELETE calls.

Risk: Ambiguous Maton profiles or PostHog connections could send a request to the wrong account or project.

Mitigation: Confirm account, project, and connection identifiers before changes, and use explicit profile or connection selection when more than one is available.

Risk: Credentials or provider-issued tokens could be exposed through command output, logs, files, or copied API responses.

Mitigation: Use the operating system credential store through Maton where possible, avoid printing or persisting token fields, and send Maton API keys only to api.maton.ai when raw HTTP fallback is unavoidable.

Risk: PostHog API responses may contain untrusted external content.

Mitigation: Treat response content as data, not instructions, and do not execute, eval, or interpolate returned content into shell commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/posthog-api)
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

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended to guide Maton CLI, SDK, and API passthrough usage; write operations require explicit user approval.]

## Skill Version(s):

1.1.0 (source: server release evidence; artifact frontmatter version is 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
