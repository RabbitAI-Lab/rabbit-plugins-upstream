## Description:

Supabase API integration with managed authentication for database tables, auth users, and storage buckets through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect to Supabase projects through Maton, inspect database tables, manage auth users, and work with storage buckets. It is intended for API-assisted project operations where read/list calls are preferred and mutations require explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorized calls can affect real Supabase production data.

Mitigation: Prefer staging for experimentation, default to read/list requests, and confirm the target connection, resource, payload, and intended effect before any write or delete.

Risk: Stored or exposed credentials could grant long-lived access.

Mitigation: Use OAuth where possible, let the Maton CLI use the operating system credential store, avoid printing or persisting credentials, and revoke unused connections.

Risk: Deleting a connection or Supabase resource can be irreversible.

Mitigation: List and match exact identifiers first, avoid bypassing prompts unless the user has already confirmed the specific target, and require explicit approval before destructive operations.

Risk: API responses may contain personal or sensitive project data.

Mitigation: Return only the fields needed for the task and avoid dumping full responses into logs, files, or chat unless the user specifically requests them.

## Reference(s):

- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Supabase REST API guide](https://supabase.com/docs/guides/api)
- [PostgREST documentation](https://postgrest.org/en/stable/)
- [Supabase Auth API](https://supabase.com/docs/reference/javascript/auth-api)
- [Supabase Storage API](https://supabase.com/docs/reference/javascript/storage-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Maton CLI commands, raw HTTP examples, SDK snippets, endpoint guidance, and operational cautions.]

## Skill Version(s):

1.2.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
