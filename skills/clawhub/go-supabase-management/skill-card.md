## Description:

Unofficial Go client for the Supabase Management API (`github.com/psyb0t/go-supabase-management`, package `supabase`), generated with oapi-codegen from Supabase's OpenAPI document. Typed methods on `supabase.ClientWithResponses` cover every path of `https://api.supabase.com`, among them organizations, projects, branches, database and pooler config, auth config, edge functions, secrets, API keys, custom domains, network restrictions, billing add-ons, analytics and OAuth. Requests authenticate with a Bearer personal access token or OAuth access token set in a request editor. Use when Go code needs to list or manage Supabase projects, organizations, branches or project settings, or already imports go-supabase-management. Not for the per-project data API (PostgREST, Auth, Storage).

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this Go client to list and manage Supabase organizations, projects, branches, and project settings through the Management API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Supabase personal access token can have broad rights across the user's organizations.

Mitigation: Read the token from SUPABASE_ACCESS_TOKEN, keep it out of source control and logs, and use an OAuth token with narrower approved scopes when suitable.

Risk: The security assessment notes an unresolved local reference and incomplete analysis.

Mitigation: Review the unresolved reference and its target, then rerun security analysis before relying on the assessment.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-supabase-management)
- [Project homepage](https://github.com/psyb0t/go-supabase-management)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.5.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
