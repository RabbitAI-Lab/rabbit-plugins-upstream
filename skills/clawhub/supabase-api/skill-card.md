## Description:

Supabase API integration with managed authentication for database tables via PostgREST, auth users, and storage buckets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with Supabase projects through Maton-managed authentication, including querying database tables, managing auth users, and handling storage buckets. It is suited to read-first project inspection and user-approved data changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and modify live Supabase project data, auth users, and storage through the connected Maton account.

Mitigation: Connect only the intended project, prefer read-only scopes, and require explicit confirmation before any write or deletion.

Risk: Long-lived API keys or surfaced provider tokens could expose account access if printed, logged, or persisted.

Mitigation: Use OAuth when possible and keep credentials in the Maton or operating system credential store rather than command lines, files, or logs.

## Reference(s):

- [Supabase Skill on ClawHub](https://clawhub.ai/byungkyu/skills/supabase-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Supabase REST API Guide](https://supabase.com/docs/guides/api)
- [PostgREST Documentation](https://postgrest.org/en/stable/)
- [Supabase Auth API](https://supabase.com/docs/reference/javascript/auth-api)
- [Supabase Storage API](https://supabase.com/docs/reference/javascript/storage-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Maton CLI commands and API request examples that affect the connected Supabase project only after user confirmation.]

## Skill Version(s):

1.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
