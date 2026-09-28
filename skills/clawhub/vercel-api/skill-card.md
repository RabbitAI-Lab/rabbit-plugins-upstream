## Description:

Vercel API integration with managed OAuth for managing projects, deployments, domains, teams, and environment variables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an agent to their Vercel account through Maton and perform approved Vercel API tasks such as checking deployments, managing projects, configuring domains, and updating environment variables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide actions that modify Vercel projects, deployments, domains, environment variables, functions, triggers, or destinations.

Mitigation: Prefer read-only calls first and require explicit user confirmation before any write, deployment, domain, environment-variable, function, trigger, or destination change.

Risk: OAuth or API-key access may expose Vercel account data beyond the immediate task if scopes or connections are too broad.

Mitigation: Review OAuth scopes, choose the least-privilege connection available, and revoke unused connections when work is complete.

Risk: Raw API responses and logs can contain user business data.

Mitigation: Return only the fields needed for the task and avoid writing raw responses to logs or files unless the user specifically asks for them.

## Reference(s):

- [Vercel REST API Documentation](https://vercel.com/docs/rest-api)
- [Vercel API Reference](https://vercel.com/docs/rest-api/endpoints)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)
- [Time Trigger Reference](references/time/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with shell, HTTP, JSON, and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a user-approved Vercel connection; responses may contain user business data.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
