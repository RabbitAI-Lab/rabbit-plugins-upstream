## Description:

Provides a typed Go client for managing Supabase organizations, projects, branches, and project settings through the Supabase Management API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add and configure the Go client, then write Go code that reads or manages Supabase organizations, projects, branches, and project settings through the Management API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A personal access token can carry the user's full rights across organizations.

Mitigation: Consider token access before use; use an OAuth token with only the approved scopes needed when possible.

Risk: Write operations can change live projects, including deleting, pausing, resetting, merging, or changing secrets and configuration.

Mitigation: Run a write operation only when requested, and confirm it targets the project ref or branch named by the user.

Risk: Tokens and API responses may contain credentials or secret values.

Mitigation: Read tokens from the environment; never hardcode, commit, or log tokens, request headers, or returned secrets.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Project repository](https://github.com/psyb0t/go-supabase-management)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-supabase-management)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples may include authenticated API requests and project or branch identifiers.]

## Skill Version(s):

0.5.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
