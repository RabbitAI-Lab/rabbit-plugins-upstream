## Description:

Provides Go developers with installation, authentication, and usage guidance for an unofficial typed client of the Supabase Management API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to install and work with the typed Supabase Management API client for organization, project, branch, and project-setting tasks. It helps them choose endpoints, configure authentication, and handle API responses safely.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Personal access tokens can grant broad access, and write operations can change or delete live Supabase resources.

Mitigation: Use narrowly scoped credentials where possible, name the intended project or branch and action, and make live changes only when explicitly requested.

Risk: Tokens and API responses can contain credentials or other secrets.

Mitigation: Read tokens from the environment and keep tokens, request headers, and returned secrets out of logs.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-supabase-management)
- [Supabase API authentication guidance](https://supabase.com/docs/reference/api/introduction)
- [Project homepage](https://github.com/psyb0t/go-supabase-management)

## Skill Output:

**Output Type(s):** [Technical guidance, Go code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Text guidance and examples for adapting the client to a Go project.]

## Skill Version(s):

0.3.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
