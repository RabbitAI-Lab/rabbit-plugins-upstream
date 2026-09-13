## Description:

Supabase API integration with managed authentication for accessing database tables through PostgREST, managing auth users, and working with storage buckets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query Supabase database tables, manage authentication users, handle storage buckets, and set up approved Maton-hosted automation against a connected Supabase project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can affect Supabase databases, auth users, storage buckets, functions, and triggers through a connected Maton account.

Mitigation: Install only if comfortable granting Maton access to the selected project, prefer least-privilege or staging projects for experiments, and confirm writes, auth-admin actions, bucket visibility changes, functions, and triggers before execution.

Risk: Long-lived credentials or raw response data can be exposed if copied into environment variables, command lines, logs, or files.

Mitigation: Prefer OAuth and the operating system credential store, avoid exporting MATON_API_KEY unless the CLI cannot be installed, rotate any exposed key, and extract only task-relevant response fields.

Risk: PostgREST writes can unintentionally update or delete more rows than intended if filters are missing or incorrect.

Mitigation: Default to read and list calls, verify identifiers and filters with a GET first, and proceed with POST, PUT, PATCH, or DELETE only after explicit user approval.

## Reference(s):

- [ClawHub Supabase Skill](https://clawhub.ai/byungkyu/skills/supabase-api)
- [Maton Homepage](https://maton.ai)
- [Supabase REST API Guide](https://supabase.com/docs/guides/api)
- [PostgREST Documentation](https://postgrest.org/en/stable/)
- [Supabase Auth API](https://supabase.com/docs/reference/javascript/auth-api)
- [Supabase Storage API](https://supabase.com/docs/reference/javascript/storage-api)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, configuration examples, and API guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Supabase API request guidance and safety checks for reads, writes, connections, functions, and triggers.]

## Skill Version(s):

1.2.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
