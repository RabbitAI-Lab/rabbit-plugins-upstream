## Description:

Provides Go developers with a typed client and usage guidance for managing Supabase organizations, projects, branches, and settings through the Supabase Management API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to add and use a typed Go client for the Supabase Management API. It helps them inspect organizations and projects and manage project settings, branches, and related services without confusing the Management API with Supabase's per-project data APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Personal access tokens can grant broad access, and write operations can change live projects.

Mitigation: Prefer a scoped OAuth token where suitable; specify the intended project and changes, and perform writes only when requested.

Risk: Tokens and API responses may contain credentials or other secrets.

Mitigation: Read tokens from the environment and never hardcode, commit, log, or print tokens, request headers, or returned secret values.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-supabase-management)
- [Supabase Management API authentication](https://supabase.com/docs/reference/api/introduction)
- [ClawHub release](https://clawhub.ai/psyb0t/skills/go-supabase-management)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use an environment variable for credentials and typed API response fields.]

## Skill Version(s):

0.3.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
