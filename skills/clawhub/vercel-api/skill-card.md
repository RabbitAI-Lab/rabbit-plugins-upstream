## Description:

Helps agents manage Vercel projects, deployments, domains, teams, and environment variables through a connected Maton account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Vercel resources and, with approval, manage deployments, projects, domains, and configuration for a connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changes to deployments, domains, projects, or environment variables can affect live services or expose sensitive configuration.

Mitigation: Inspect the current state, confirm the exact account and resource, and obtain explicit approval before each write.

Risk: Hosted functions, triggers, and destinations can persist actions or route data to other services.

Mitigation: Review the handler, destination, and event source with the user before enabling automation; avoid sending credentials to destinations.

Risk: A copied or exposed Maton API key can grant access to the connected account.

Mitigation: Prefer device login and the system credential store; never print or embed the key, and rotate it if exposed.

## Reference(s):

- [ClawHub Vercel skill release](https://clawhub.ai/byungkyu/skills/vercel-api)
- [Maton](https://maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Vercel REST API documentation](https://vercel.com/docs/rest-api)
- [Vercel API reference](https://vercel.com/docs/rest-api/endpoints)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions require an authorized Vercel connection through Maton.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
