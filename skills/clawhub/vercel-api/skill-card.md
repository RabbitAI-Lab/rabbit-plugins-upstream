## Description:

Vercel API integration with managed OAuth for managing projects, deployments, domains, teams, and environment variables through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect and manage Vercel accounts from an agent workflow, including projects, deployments, domains, teams, and environment variables. It is suited for Vercel administration tasks that can be performed through authenticated Maton API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make authenticated changes to Vercel projects, deployments, domains, teams, and environment variables.

Mitigation: Prefer read and list calls first, specify the intended Maton connection or profile, and require explicit user confirmation before any write or connection-creation action.

Risk: Broad OAuth scopes or ambiguous accounts can expose or modify unintended Vercel resources.

Mitigation: Review OAuth scopes during connection setup, prefer read-only access when available, and pin requests to the intended connection when more than one account is available.

Risk: Credentials and provider-issued tokens may leak if printed, logged, persisted, or passed through commands.

Mitigation: Use Maton OAuth and OS credential storage when possible, avoid inspecting stored credentials, and keep any API-key fallback limited to the current process environment.

## Reference(s):

- [Vercel REST API Documentation](https://vercel.com/docs/rest-api)
- [Vercel API Reference](https://vercel.com/docs/rest-api/endpoints)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/vercel-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and API guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Vercel connection.]

## Skill Version(s):

1.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
