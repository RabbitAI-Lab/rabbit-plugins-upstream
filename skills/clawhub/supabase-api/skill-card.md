## Description:

Helps agents access connected Supabase projects to query tables, manage authentication users, and work with storage through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other authorized users can ask an agent to inspect or manage data, authentication users, and storage in a connected Supabase project. With separate approval, they can also set up hosted functions and scheduled or event-driven actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected Supabase access can change project data, users, or storage.

Mitigation: Prefer read-only or staging access where possible and confirm each write, authentication, storage, or administrative action.

Risk: Hosted functions, schedules, and trigger destinations may keep acting after setup.

Mitigation: Require explicit approval before creating them and review the function's behavior, permissions, and destination first.

## Reference(s):

- [Supabase skill release](https://clawhub.ai/byungkyu/skills/supabase-api)
- [Maton](https://maton.ai)
- [Supabase REST API guide](https://supabase.com/docs/guides/api)
- [Supabase Auth API](https://supabase.com/docs/reference/javascript/auth-api)
- [Supabase Storage API](https://supabase.com/docs/reference/javascript/storage-api)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Guidance]

**Output Format:** [Markdown with commands and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions are limited by the connected user's authorization; writes and new connections require user confirmation.]

## Skill Version(s):

1.2.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
