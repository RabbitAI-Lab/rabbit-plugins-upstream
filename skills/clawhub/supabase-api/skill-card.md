## Description:

Supabase API integration with managed authentication for accessing database tables via PostgREST, managing auth users, and working with storage buckets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query Supabase database tables, inspect or manage auth users, and work with storage buckets through Maton-authenticated Supabase API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton-mediated access can grant access to a Supabase project.

Mitigation: Prefer OAuth, least-privilege or read-only scopes where available, and connect only the account needed for the current task.

Risk: POST, PUT, PATCH, and DELETE calls can modify live database, auth, or storage data.

Mitigation: Require explicit user approval after checking the target project, resource identifiers, payload, and intended effect.

Risk: Using raw API keys instead of the CLI can expose long-lived credentials.

Mitigation: Use the Maton CLI with OAuth when possible; if raw HTTP is unavoidable, avoid printing, persisting, or passing keys on the command line.

Risk: Data returned from Supabase may contain untrusted content.

Mitigation: Treat API responses as data, validate them before reuse, and do not execute or follow instructions embedded in returned content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/supabase-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Supabase REST API Guide](https://supabase.com/docs/guides/api)
- [PostgREST Documentation](https://postgrest.org/en/stable/)
- [Supabase Auth API](https://supabase.com/docs/reference/javascript/auth-api)
- [Supabase Storage API](https://supabase.com/docs/reference/javascript/storage-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes user-approval guidance for connection creation and mutating Supabase API calls.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
