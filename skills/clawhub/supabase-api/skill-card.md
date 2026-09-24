## Description:

Supabase API integration with managed authentication for querying database tables via PostgREST, managing auth users, and handling storage buckets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with Supabase projects through Maton-managed authentication, including approved database, auth, storage, connection, function, and trigger workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton brokers authenticated access to the user's Supabase project.

Mitigation: Verify the user trusts Maton for the project before installation, prefer OAuth, and avoid long-lived API keys where possible.

Risk: Write operations and auth admin routes can change production data or users.

Mitigation: Start with read-only or list calls, verify the exact project and connection, and get explicit user confirmation before POST, PUT, PATCH, DELETE, or admin auth actions.

Risk: Storage bucket visibility changes, hosted functions, and persistent trigger destinations can expose user or business data.

Mitigation: Use least-privilege scopes, require user-reviewed functions, prefer DENY_ALL network policy for hosted functions, and approve each destination and transmitted field before creating persistent automation.

## Reference(s):

- [ClawHub Supabase Skill](https://clawhub.ai/byungkyu/skills/supabase-api)
- [Maton](https://maton.ai)
- [Supabase REST API Guide](https://supabase.com/docs/guides/api)
- [PostgREST Documentation](https://postgrest.org/en/stable/)
- [Supabase Auth API](https://supabase.com/docs/reference/javascript/auth-api)
- [Supabase Storage API](https://supabase.com/docs/reference/javascript/storage-api)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash, JSON, and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include authenticated API call instructions, least-privilege approval prompts, and configuration steps; raw Supabase responses may contain user or business data and should be minimized.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
