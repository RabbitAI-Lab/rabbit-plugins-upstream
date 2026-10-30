## Description:

Provides Go developers with a typed client and usage guidance for managing Supabase organizations, projects, branches, and settings through the Supabase Management API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add and work with a Go client for listing or managing Supabase organizations, projects, branches, and project settings. It does not cover the per-project data APIs for PostgREST, Auth, or Storage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A personal access token can grant access across all organizations available to its user, and API responses may contain secrets.

Mitigation: Prefer a narrowly scoped token where possible, read it from the environment, and never hardcode, commit, or log tokens or returned secrets.

Risk: Write operations can change live Supabase projects, including destructive or hard-to-reverse changes.

Mitigation: Name the exact project or branch and intended change, and call write operations only when that change was requested.

Risk: This is an unofficial Go dependency used to access project management operations.

Mitigation: Pin a reviewed dependency version before relying on it.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [go-supabase-management on GitHub](https://github.com/psyb0t/go-supabase-management)
- [go-supabase-management on pkg.go.dev](https://pkg.go.dev/github.com/psyb0t/go-supabase-management)
- [Supabase Management API authentication](https://supabase.com/docs/reference/api/introduction)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.3.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
