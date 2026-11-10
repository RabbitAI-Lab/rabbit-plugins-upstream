## Description:

Provides Go developers with a typed client for managing Supabase organizations, projects, branches, and project settings through the Supabase Management API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the Go client to list and manage Supabase organizations, projects, branches, and project settings through the Management API. It is intended for Go applications and does not cover the per-project data API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Supabase personal access token can grant broad rights across the user's organizations, and API responses may contain secrets.

Mitigation: Prefer an OAuth token with only the required scopes when practical; read credentials from SUPABASE_ACCESS_TOKEN and never hardcode, log, or print credentials, headers, or returned secrets.

Risk: Write operations can change live projects, including deleting, pausing, resetting, merging, or changing secrets and configuration.

Mitigation: Run a write operation only when requested, and confirm the named project reference or branch before making the call.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-supabase-management)
- [Source repository](https://github.com/psyb0t/go-supabase-management)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-supabase-management)
- [Setup and reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.5.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
