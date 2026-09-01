## Description:

Vercel API integration with managed OAuth for managing projects, deployments, domains, teams, and environment variables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect and manage Vercel accounts through Maton-managed OAuth, including projects, deployments, domains, teams, and environment variables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing Vercel access can expose projects, deployments, domains, teams, and environment variables in the connected account.

Mitigation: Use OAuth when possible, choose the narrowest Vercel scopes available, and specify the intended connection or account before acting.

Risk: Write operations can change live deployments, domains, team settings, or environment variables.

Mitigation: Default to read and list calls, then review the target, payload, and intended effect before approving any POST, PUT, PATCH, or DELETE request.

Risk: API-key fallback can expose a long-lived Maton credential if handled carelessly.

Mitigation: Prefer OAuth and CLI-managed credential storage; if raw HTTP is necessary, avoid printing or persisting the key and send it only to api.maton.ai.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/vercel-api)
- [Maton Homepage](https://maton.ai)
- [Vercel REST API Documentation](https://vercel.com/docs/rest-api)
- [Vercel API Reference](https://vercel.com/docs/rest-api/endpoints)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user approval for new connections or write operations.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
