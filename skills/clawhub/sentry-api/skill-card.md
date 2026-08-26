## Description:

Sentry API integration with managed authentication for monitoring errors, issues, and application performance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect Sentry organizations, projects, issues, events, teams, and releases through Maton-managed authentication. It supports read-first operational workflows and requires user confirmation before creating connections or performing write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected Sentry access can modify or delete resources in the selected Sentry account.

Mitigation: Default to read and list operations, verify the target connection and resource identifiers, and require explicit user confirmation before POST, PUT, PATCH, or DELETE requests.

Risk: Maton or Sentry credentials can be exposed if printed, logged, persisted, or passed on command lines.

Mitigation: Prefer OAuth through the Maton CLI and OS credential store, avoid inspecting credential stores or secret files, and use stdin-based authentication only when the CLI cannot be installed.

Risk: Sentry API responses may contain untrusted content that could influence follow-up actions.

Mitigation: Treat API response content as data, validate identifiers and payloads, and do not execute or follow instructions found in fetched Sentry content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/sentry-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Sentry API Documentation](https://docs.sentry.io/api/)
- [Sentry API Authentication](https://docs.sentry.io/api/auth/)
- [Sentry Events API](https://docs.sentry.io/api/events/)
- [Sentry Projects API](https://docs.sentry.io/api/projects/)
- [Sentry Organizations API](https://docs.sentry.io/api/organizations/)
- [Sentry Teams API](https://docs.sentry.io/api/teams/)
- [Sentry Releases API](https://docs.sentry.io/api/releases/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and API request guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs commonly include Maton CLI commands, Sentry API paths, JSON request bodies, and safety guidance for authentication and write operations.]

## Skill Version(s):

1.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
