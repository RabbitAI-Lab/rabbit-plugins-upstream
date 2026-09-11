## Description:

Vercel API integration with managed OAuth for managing projects, deployments, domains, teams, and environment variables through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect and manage Vercel resources through authenticated Maton gateway calls, including deployments, projects, domains, teams, and environment variables. It is intended for read-first API workflows with explicit confirmation before connection creation or write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing the Maton connection grants access to the intended Vercel account.

Mitigation: Review OAuth scopes, prefer read-only access when possible, and create a Vercel connection only after explicit user approval.

Risk: Write operations can affect production deployments, domains, teams, or environment variables.

Mitigation: Confirm the target connection, resource identifier, request payload, and expected production impact before any POST, PUT, PATCH, or DELETE call.

Risk: Credentials or provider-issued tokens could be exposed if printed, persisted, or passed through shell commands.

Mitigation: Use the Maton CLI credential store, avoid inspecting stored secrets, and keep raw API keys only in the process environment when the CLI cannot be used.

## Reference(s):

- [Vercel REST API Documentation](https://vercel.com/docs/rest-api)
- [Vercel API Reference](https://vercel.com/docs/rest-api/endpoints)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/vercel-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output may include Maton CLI commands, Vercel API paths, request payloads, and operational guidance.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
