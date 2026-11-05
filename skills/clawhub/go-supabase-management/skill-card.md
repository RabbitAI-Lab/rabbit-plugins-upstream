## Description:

Unofficial Go client for the Supabase Management API (`github.com/psyb0t/go-supabase-management`, package `supabase`), generated with oapi-codegen from Supabase's OpenAPI document. Typed methods on `supabase.ClientWithResponses` cover every path of `https://api.supabase.com`, among them organizations, projects, branches, database and pooler config, auth config, edge functions, secrets, API keys, custom domains, network restrictions, billing add-ons, analytics and OAuth. Requests authenticate with a Bearer personal access token or OAuth access token set in a request editor. Use when Go code needs to list or manage Supabase projects, organizations, branches or project settings, or already imports go-supabase-management. Not for the per-project data API (PostgREST, Auth, Storage).

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate Go code with the Supabase Management API, including listing organizations, projects, and branches or managing project settings. It helps them configure authentication, find typed client methods, and check API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A personal access token can act with the user's full rights across their organizations, and management operations can change live project state.

Mitigation: Prefer OAuth credentials scoped to the needed operations; keep tokens in environment variables, never log or commit credentials or returned secrets, and confirm the requested project or branch before write operations.

Risk: The Go module is an external dependency.

Mitigation: Review and pin the dependency before production use.

## Reference(s):

- [Project repository](https://github.com/psyb0t/go-supabase-management)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-supabase-management)
- [Setup and reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with Go examples, shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers the Supabase Management API client and its authentication and response handling.]

## Skill Version(s):

0.4.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
