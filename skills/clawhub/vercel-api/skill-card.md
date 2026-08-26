## Description:

Vercel API integration with managed OAuth for managing projects, deployments, domains, teams, and environment variables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect and manage Vercel projects, deployments, domains, teams, and environment variables through Maton-managed OAuth and Vercel API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected Vercel account can be used for account-management actions affecting projects, deployments, domains, teams, and environment variables.

Mitigation: Use OAuth with the narrowest available scopes, default to read/list calls, and confirm the target resource, payload, and intended effect before any write action.

Risk: Multiple Maton or Vercel connections can cause operations to run against the wrong account.

Mitigation: Specify the intended connection when more than one account exists and revoke unused connections after use.

Risk: Long-lived or provider-issued credentials can be exposed if printed, persisted, or passed through shell history.

Mitigation: Prefer OAuth and the CLI credential store; never print, log, persist, or pass credentials on command lines.

## Reference(s):

- [Vercel REST API Documentation](https://vercel.com/docs/rest-api)
- [Vercel API Reference](https://vercel.com/docs/rest-api/endpoints)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, API Calls]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected Vercel account.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
